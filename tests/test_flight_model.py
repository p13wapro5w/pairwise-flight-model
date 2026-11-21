import pytest
import math
from gameplay import flight_model as mod

CASES = [
    ("lift", 'm.lift(0.1, 2, 3) == approx(0.6)'),
    ("plate", 'm.stall_plate(0.5, 0.3) == 0.3'),
    ("authority", 'm.control_authority(2, 3) == 6'),
    ("cross", 'm.crosswind_roll(2, 3) == 6'),
    ("ground", 'm.ground_effect(0, 2) == approx(1.0)'),
    ("windup", 'm.anti_windup(5, 3) == 3'),
    ("fuel", 'm.fuel_flow(2, 0.5) == approx(1.0)'),
    ("sync", 'm.sync_state(1, 2) == 2'),
    ("camera", 'm.camera_roll(0.2) == 0.2'),
    ("touch", 'm.touchdown_ok(1, 0.5, 2) is True'),
    ("shear", 'm.windshear_warn(0.5, 0.2) is True'),
    ("q", 'm.dynamic_pressure(2, 3) == approx(9.0)'),
    ("key", 'm.flight_key(3, 2) == "3:2"'),
    ("clamp", 'm.clamp_alpha(0.5, 0.3) == 0.3'),
    ("stall", 'm.is_stalled(0.4, 0.3) is True')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx, "math": math})
