from manimlib.imports import *
import math

#自定义arctan的算法
def arctan(start, end):
    start_x, start_y, end_x, end_y = start[0], start[1], end[0], end[1]
    mode = 1
    if start_x < end_x and start_y < end_y:
        mode = 1
    elif start_x > end_x and start_y < end_y:
        mode = 2
    elif start_x > end_x and start_y > end_y:
        mode = 3
    elif start_x < end_x and start_y > end_y:
        mode = 4
    else:
        pass
    delta_x = end_x - start_x
    delta_y = end_y - start_y
    theta = math.atan(delta_y / delta_x)
    if mode == 1:
        pass
    elif mode == 2:
        theta += PI
    elif mode == 3:
        theta += PI
    elif mode == 4:
        theta += 2 * PI
    return theta

def MyArrow(start, end, color):
    ARC = PI / 180
    AB = 1 / 3
    BQ = CQ = AB * np.sin(17 * ARC)
    PQ = BQ / np.tan(50 * ARC)
    AQ = AB * np.cos(17 * ARC)
    AP = AQ - PQ
    #设A点坐标为(0, 0)
    A, B, P, C = np.array([0., 0., 0.]), np.array(
        [-AQ, BQ, 0.]), np.array([-AP, 0., 0.]), np.array([-AQ, -CQ, 0.])

    #平移箭头
    arrow_len = get_len(start, end)
    print(arrow_len)
    A[0] += arrow_len
    B[0] += arrow_len
    P[0] += arrow_len
    C[0] += arrow_len

    #旋转箭头
    theta = arctan(start, end)
    rotate_matrix = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 0]
    ])
    A = np.inner(rotate_matrix, A.T).T + start
    B = np.inner(rotate_matrix, B.T).T + start
    P = np.inner(rotate_matrix, P.T).T + start
    C = np.inner(rotate_matrix, C.T).T + start

    return VGroup(
        Line(start, end + (P - A), color=color),
        Polygon(A, B, P, C, color=color, fill_opacity=1).set_stroke(
            width=DEFAULT_STROKE_WIDTH/4),
    )
