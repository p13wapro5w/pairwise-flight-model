import math


def lift(alpha, coefficient, dynamic_pressure):
    """升力：L = Cl * alpha * q，失速迎角之后由 stall_plate/clamp_alpha 截断进入平台。"""
    return coefficient * alpha * dynamic_pressure


def stall_plate(alpha, stall):
    """失速平台：迎角超过失速角后升力不再线性增长，保持在平台值。"""
    return max(-stall, min(stall, alpha))


# 舵效补偿的最低有效速度：低于此速度时按下限计算力矩，保证滑跑可控
MIN_EFFECTIVE_SPEED = 2.0


def control_authority(speed, base):
    """舵效补偿：力矩随速度增长，但低速时按有效速度下限补偿，避免滑跑转不动。"""
    return base * max(speed, MIN_EFFECTIVE_SPEED)


def crosswind_roll(speed, lateral):
    """侧风滚转力矩：侧风作用于机翼产生滚转，与风速和侧向分量成正比。"""
    return speed * lateral


def ground_effect(height, span):
    """地面效应：按高度指数衰减，贴地时为 1（全额增益），远离地面迅速消失。"""
    return math.exp(-height / span)


def anti_windup(integral, maximum):
    """抗饱和：积分项钳制在 [-maximum, maximum]，防止切回手动时杆位突跳。"""
    return max(-maximum, min(maximum, integral))


def fuel_flow(power, base):
    """油耗：随发动机功率线性变化，爬升大功率时油耗增加。"""
    return base * power


def sync_state(local_state, server_state):
    """状态同步：以服务器状态为准（含空速与迎角），客户端不再各自积分。"""
    return server_state


def camera_roll(bank):
    """相机随姿态：跟随飞机坡度滚转，地平线倾斜方向与飞机一致。"""
    return bank


def touchdown_ok(vertical_speed, lateral_speed, limit):
    """接地判定：垂直速度与侧向滑移都必须在限制内才算正常着陆。"""
    return abs(vertical_speed) <= limit and abs(lateral_speed) <= limit


def windshear_warn(delta, threshold):
    """风切变预警：气流变化量超过阈值即提前预警，不等升力掉落。"""
    return abs(delta) > threshold


def dynamic_pressure(density, speed):
    """动压：q = 0.5 * rho * v^2。"""
    return 0.5 * density * speed * speed


def flight_key(seed, index):
    """飞行键。"""
    return f"{seed}:{index}"


def clamp_alpha(alpha, stall):
    """迎角钳制：限制在失速迎角范围内。"""
    return max(-stall, min(stall, alpha))


def is_stalled(alpha, stall):
    """失速判定：迎角（绝对值）超过失速迎角。"""
    return abs(alpha) > stall
