from manimlib.imports import *

class Hypocycloid(VMobject):

    CONFIG = {
        'R': 3,
        'r': 1,
        'd': 0.5,
        'theta_max': TAU,
        'stroke_width': 2,
    }

    def __init__(self, **kwargs):

        VMobject.__init__(self, **kwargs)

        t = np.linspace(0, self.theta_max, 10000)
        curve_points = self.parameter_func(t)
        self.set_points_as_corners(
            [*curve_points, curve_points[0]]
        )

    def parameter_func(self, t):
        R, r, d = self.R, self.r, self.d
        x, y = (R-r) * np.cos(t) + d * np.cos((R-r) * t/r), (R-r) * np.sin(t) - d * np.sin((R-r) * t/r)
        return np.concatenate((x.reshape(-1, 1), y.reshape(-1, 1), x.reshape(-1, 1) * 0), axis=1)

class Show_hypocycloid(Scene):

    def construct(self):
        R = 3.6
        r = R * 5/13
        d = np.linspace(-r * 0.95, r * 0.95, 20)
        curve_group = VGroup()
        color_list = color_gradient([RED, ORANGE, YELLOW, GREEN, BLUE, PINK], len(d))

        circle_big = Circle(radius=R, color=BLUE, fill_opacity=0)
        circle_small = Circle(radius=r, color=BLUE, fill_opacity=0).shift((R-r) * RIGHT)

        for i in range(len(d)):
            curve_i = Hypocycloid(R=R, r=r, d=d[i], theta_max=5 * TAU, color=color_list[i])
            curve_group.add(curve_i)

        self.add(circle_big)
        self.wait()
        self.add(curve_group)
        self.wait(2)
