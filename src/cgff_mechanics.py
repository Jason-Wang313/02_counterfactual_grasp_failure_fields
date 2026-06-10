"""Planar mechanics for counterfactual grasp failure fields.

The model is intentionally small: two opposing point contacts on a planar
object must resist a vertical load and an external torque.  It is useful as a
counterexample to scalar failure labels, not as a full robot simulator.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Tuple


@dataclass(frozen=True)
class PinchParams:
    """Parameters for a symmetric two-finger pinch grasp."""

    half_width: float = 0.5
    normal_force: float = 1.0
    friction_coeff: float = 0.72
    weight: float = 0.82
    finger_y_limit: float = 1.0

    @property
    def stable_error_radius(self) -> float:
        """Allowed error in contact-height difference, in object-length units."""

        radius = self.half_width * (
            2.0 * self.friction_coeff * self.normal_force - self.weight
        ) / self.normal_force
        return max(0.0, radius)


@dataclass(frozen=True)
class GraspState:
    """A realized tactile/contact state for the planar pinch."""

    y_left: float
    y_right: float
    torque_over_normal: float

    @property
    def contact_difference(self) -> float:
        return self.y_right - self.y_left


@dataclass(frozen=True)
class FailureField:
    """Minimum-norm contact displacement that repairs a failed state."""

    dy_left: float
    dy_right: float
    delta_difference: float
    margin_before: float
    margin_after: float
    feasible_within_limits: bool

    @property
    def l2_norm(self) -> float:
        return math.sqrt(self.dy_left * self.dy_left + self.dy_right * self.dy_right)

    @property
    def repair_sign(self) -> int:
        if self.delta_difference > 0.0:
            return 1
        if self.delta_difference < 0.0:
            return -1
        return 0


def error_coordinate(state: GraspState) -> float:
    """Return the wrench-balance error e = tau/N - (y_R - y_L)."""

    return state.torque_over_normal - state.contact_difference


def stability_margin(state: GraspState, params: PinchParams) -> float:
    """Positive means feasible tangential forces exist; negative means failure."""

    return params.stable_error_radius - abs(error_coordinate(state))


def failure_score(state: GraspState, params: PinchParams, sharpness: float = 16.0) -> float:
    """A calibrated scalar failure probability derived only from the margin."""

    margin = stability_margin(state, params)
    z = -sharpness * margin
    if z >= 0:
        ez = math.exp(-z)
        return 1.0 / (1.0 + ez)
    ez = math.exp(z)
    return ez / (1.0 + ez)


def is_success(state: GraspState, params: PinchParams) -> bool:
    return stability_margin(state, params) >= -1e-12


def apply_field(state: GraspState, dy_left: float, dy_right: float) -> GraspState:
    return GraspState(
        y_left=state.y_left + dy_left,
        y_right=state.y_right + dy_right,
        torque_over_normal=state.torque_over_normal,
    )


def counterfactual_failure_field(state: GraspState, params: PinchParams) -> FailureField:
    """Compute the minimum L2 contact-height displacement that reaches success.

    Success is the interval |tau/N - (y_R-y_L)| <= h.  For a failed state, the
    nearest successful point is the projection onto the closest boundary of that
    interval.  Since only y_R-y_L matters, the minimum L2 displacement splits
    the required difference change equally across the two contacts.
    """

    e = error_coordinate(state)
    h = params.stable_error_radius
    margin_before = h - abs(e)
    if margin_before >= 0.0:
        dy_left = 0.0
        dy_right = 0.0
        delta_difference = 0.0
    else:
        target_error = math.copysign(h, e)
        delta_difference = e - target_error
        dy_right = 0.5 * delta_difference
        dy_left = -0.5 * delta_difference

    repaired = apply_field(state, dy_left, dy_right)
    feasible = (
        abs(repaired.y_left) <= params.finger_y_limit
        and abs(repaired.y_right) <= params.finger_y_limit
    )
    return FailureField(
        dy_left=dy_left,
        dy_right=dy_right,
        delta_difference=delta_difference,
        margin_before=margin_before,
        margin_after=stability_margin(repaired, params),
        feasible_within_limits=feasible,
    )


def scalar_only_repair(
    state: GraspState,
    params: PinchParams,
    sign_guess: int,
) -> Tuple[float, float]:
    """Use only scalar failure distance and an externally guessed direction."""

    e = error_coordinate(state)
    magnitude = max(0.0, abs(e) - params.stable_error_radius)
    delta_difference = float(sign_guess) * magnitude
    return -0.5 * delta_difference, 0.5 * delta_difference

