################################################################################################
#--coding:utf-8--
# Notes:
# 此代码由b站UP主Cigar666（UID:66806831）编写上传，对应b站视频av69391597，av74425370中的数学动画
# 此代码由python3.7.3结合老版manim编写而成（新版会有些许差异）
# 此代码仅供交流学习使用。使用其中生成的视频结果用来制作自己的视频无需授权
# 由于水平有限，代码质量并不算太高，仅供参考。若有不足之处，敬请谅解。
################################################################################################

from manimlib.imports import * # 若为新版请将这句改为from manimlib.imports import *
from numpy import sqrt, sin, cos

QING, QING_A, QING_0 = '#1984D6', '#19B5ED', '#99D7FF'
ZHU, ZHU_A, ZHU_0 = '#D44712', '#F46C1B', '#FFA952'

class Test(Scene):

    CONFIG = {
        'bg_color': BLACK,
        'text_color': WHITE,
    }

    def reverse_color_style(self):
        self.bg_color, self.text_color = self.text_color, self.bg_color

    def construct(self):

        bg_rect = Rectangle(fill_color=self.bg_color, fill_opacity=1).scale(20)
        self.add(bg_rect)
        self.wait(0.25)

        triangle_01 = Polygon(LEFT, RIGHT, UP * 2, fill_color=BLUE, fill_opacity=0.6)

        self.play(ShowCreation(triangle_01))
        self.always_continually_update = True

        dt = 1/14.5
        time = 2
        n = int(time/dt)
        for i in range(n):

            # triangle_01.set_points(LEFT, RIGHT, UP * 2 + RIGHT * 0.025)
            # triangle_01.reset_points(LEFT, RIGHT, UP * 2 + RIGHT * 0.025)
            self.remove(triangle_01)
            triangle_01 = Polygon(LEFT, RIGHT, UP * 2 + RIGHT * 0.05 * i, fill_color=BLUE, fill_opacity=0.6)
            self.add(triangle_01)
            self.wait(dt)

        self.wait(2)

class Pythagoras_intro(Scene):

    def construct(self):

        triangle_abc = Polygon(np.array([-1.2, 0, 0]), np.array([1.2, 0, 0]), np.array([-1.2, 2.4/sqrt(3), 0]), color=WHITE, stroke_width=2.4)
        cube = Cube(fill_opacity=0, stroke_width=1.2).scale(0.2).shift(RIGHT * 0.2 + UP * 0.2).shift(np.array([-1.2, 0, 0]))

        triangle = VGroup(triangle_abc, cube).shift(DOWN * 0.5)

        a = TextMobject('a', color=QING).shift(LEFT * 1.6 + UP * 0.18)
        b = TextMobject('b', color=ZHU).shift(DOWN * 0.8)
        c = TextMobject('c', color=PINK).scale(1.1).shift(RIGHT * 0.2 + UP * 0.45)

        cube_kwargs = {
            "color": WHITE,
            "stroke_width": 1.8,
            "fill_opacity": 0.12,
        }

        cube_a = Cube(fill_color=QING, **cube_kwargs).scale(2.4/sqrt(3)/2).shift(1.2 * LEFT + 2.4/sqrt(3)/2 * (LEFT + UP) + DOWN *0.5)
        cube_b = Cube(fill_color=ZHU, **cube_kwargs).scale(2.4/2).shift(1.2 * DOWN + DOWN * 0.5)
        cube_c = Cube(fill_color=PINK, **cube_kwargs).scale(2.4/sqrt(3)).rotate(PI/3).shift(1.2/sqrt(3) * UP + (RIGHT/2 + UP * sqrt(3)/2) * 2.4/sqrt(3) + DOWN * 0.5)

        a2 = TextMobject('$a^{2}$', color=QING).scale(1.2).move_to(cube_a)
        b2 = TextMobject('$b^{2}$', color=ZHU).scale(1.2 * sqrt(3)).move_to(cube_b)
        c2 = TextMobject('$c^{2}$', color=PINK).scale(1.2 * 2).move_to(cube_c).shift(UP * 0.08)

        a_squqre = VGroup(cube_a, a2)
        b_squqre = VGroup(cube_b, b2)
        c_squqre = VGroup(cube_c, c2)

        self.play(FadeIn(triangle))
        self.wait(0.4)

        self.play(Write(a), Write(b), Write(c))

        self.wait(0.6)
        self.play(FadeIn(cube_a), FadeIn(cube_b), FadeIn(cube_c),
                  ReplacementTransform(a, a2),
                  ReplacementTransform(b, b2),
                  ReplacementTransform(c, c2), run_time=1.2
                  )
        self.wait()

        self.play(FadeOut(triangle), run_time=0.2)
        self.play(ApplyMethod(a_squqre.shift, LEFT * 2.8),
                  ApplyMethod(b_squqre.shift, UP * 1.85 + LEFT * 0.6),
                  ApplyMethod(c_squqre.shift, RIGHT * 3.5 + DOWN * 1.2), run_time=1.5)
        self.wait(0.8)
        self.play(Write(TextMobject('+').scale(2).next_to(a_squqre, RIGHT * 3)))
        self.wait(0.5)
        self.play(Write(TextMobject('=').scale(2).next_to(b_squqre, RIGHT * 2.5)))
        self.wait(0.5)
        self.always_continually_update = True
        t = 0.6
        dt = 1/29.5
        n = int(t/dt)
        for i in range(n):
            cube_c.rotate(PI/6/n)
            self.wait(dt)

        self.wait(5)

class Pythagoras_01(Scene):

    CONFIG = {
        'scale_all': 0.75,
    }

    def construct(self):

        cube_kwargs = {
            "color": WHITE,
            "stroke_width": 1,
            "fill_opacity": 0.6,
        }

        O_a = (1 + sqrt(3)) * (LEFT * sqrt(3)/2 + UP * 0.5)
        O_b = (1 + sqrt(3)) * (RIGHT * 0.5 + UP * sqrt(3)/2)
        O_c = DOWN * 2

        triangle_abc = Polygon(np.array([-2, 0, 0]), np.array([2, 0, 0]), np.array([-1, sqrt(3), 0]), color=WHITE, stroke_width=2)
        cube = Cube(fill_opacity=0, stroke_width=1).scale(0.2).shift(RIGHT * 0.2 + DOWN * 0.2).rotate_about_origin(-PI/6).shift(np.array([-1, sqrt(3), 0]))
        triangle = VGroup(triangle_abc, cube)

        cube_a = Cube(fill_color=BLUE, **cube_kwargs).scale(1).move_to(O_a).rotate(PI/3)
        cube_b = Cube(fill_color=RED, **cube_kwargs).scale(sqrt(3)).move_to(O_b).rotate(-PI/6)
        cube_c = Cube(fill_color=GREEN, **cube_kwargs).scale(2).move_to(O_c)

        poly_kwargs = {
            "color": WHITE,
            "stroke_width": 2,
            "fill_opacity": 0.9,
        }
        poly_01 = Polygon(O_b, O_b + DOWN * 2, RIGHT * 2, O_b + RIGHT * 2, fill_color=PINK, **poly_kwargs)
        poly_02 = Polygon(O_b, O_b + RIGHT * 2, (2 + sqrt(3)) * RIGHT + 3 * UP, O_b + UP * 2, fill_color=ORANGE, **poly_kwargs)
        poly_03 = Polygon(O_b, O_b + DOWN * 2, RIGHT * 2, O_b + RIGHT * 2, fill_color=PINK, **poly_kwargs).scale_about_point(-1, O_b)
        poly_04 = Polygon(O_b, O_b + RIGHT * 2, (2 + sqrt(3)) * RIGHT + 3 * UP, O_b + UP * 2, fill_color=ORANGE, **poly_kwargs).scale_about_point(-1, O_b)

        poly_group = VGroup(poly_01, poly_02, poly_03, poly_04)

        group_all = VGroup(triangle, cube_a, cube_b, cube_c, poly_group).scale_about_point(self.scale_all, ORIGIN)

        self.play(FadeIn(triangle))
        self.wait()
        self.play(FadeIn(cube_a), FadeIn(cube_b), FadeIn(cube_c))
        self.wait()
        self.play(FadeIn(poly_group))
        self.wait()

        self.play(ApplyMethod(poly_01.copy().shift, (LEFT * 2 - O_b) * self.scale_all))
        self.wait(0.5)
        self.play(ApplyMethod(poly_02.copy().shift, (LEFT * 2 + DOWN * 4 - O_b) * self.scale_all))
        self.wait(0.5)
        self.play(ApplyMethod(poly_03.copy().shift, (RIGHT * 2 + DOWN * 4 - O_b) * self.scale_all))
        self.wait(0.5)
        self.play(ApplyMethod(poly_04.copy().shift, (RIGHT * 2 - O_b) * self.scale_all))
        self.wait(0.5)
        self.play(ApplyMethod(cube_a.copy().shift, (O_c - O_a) * self.scale_all))

        self.wait(2)

class Pythagoras_02(Scene):

    CONFIG = {
        'scale_all': 0.8,
        'dt': 1/29.5,
    }

    def construct(self):

        cube_kwargs = {
            "color": WHITE,
            "stroke_width": 1.8,
            "fill_opacity": 0.6,
        }

        O_a = (1 + sqrt(3)) * (LEFT * sqrt(3)/2 + UP * 0.5)
        O_b = (1 + sqrt(3)) * (RIGHT * 0.5 + UP * sqrt(3)/2)
        O_c = DOWN * 2

        triangle_abc = Polygon(np.array([-2, 0, 0]), np.array([2, 0, 0]), np.array([-1, sqrt(3), 0]), color=WHITE, stroke_width=2)
        cube = Cube(fill_opacity=0, stroke_width=1).scale(0.2).shift(RIGHT * 0.2 + DOWN * 0.2).rotate_about_origin(-PI/6).shift(np.array([-1, sqrt(3), 0]))
        triangle = VGroup(triangle_abc, cube)

        cube_a = Cube(fill_color=BLUE_B, **cube_kwargs).scale(1).move_to(O_a).rotate(PI/3)
        cube_b = Cube(fill_color=BLUE_B, **cube_kwargs).scale(sqrt(3)).move_to(O_b).rotate(-PI/6)
        cube_c = Cube(fill_color=BLUE_B, **cube_kwargs).scale(2).move_to(O_c)

        line_kwargs = {
            'color': WHITE,
            "stroke_width": 1.6,
        }

        line_01 = Line(O_a + (DOWN * sin(15/180 * PI) + LEFT * cos(15/180 * PI)) * sqrt(2), O_b - (DOWN * sin(15/180 * PI) + LEFT * cos(15/180 * PI)) * sqrt(2) * sqrt(3), **line_kwargs)
        line_02 = Line(O_a + (LEFT * sin(15/180 * PI) + UP * cos(15/180 * PI)) * sqrt(2), O_a + (DOWN * sin(15/180 * PI) + LEFT * cos(15/180 * PI)) * sqrt(2) * sin(15/180 * PI), **line_kwargs)
        line_03 = Line(O_a - (LEFT * sin(15/180 * PI) + UP * cos(15/180 * PI)) * sqrt(2), O_a - (DOWN * sin(15/180 * PI) + LEFT * cos(15/180 * PI)) * sqrt(2) * sin(15/180 * PI), **line_kwargs)
        line_04 = Line(O_b + (LEFT * sin(15/180 * PI) + UP * cos(15/180 * PI)) * sqrt(2) * sqrt(3), O_b + (DOWN * sin(15/180 * PI) + LEFT * cos(15/180 * PI)) * sqrt(2) * sin(15/180 * PI) * sqrt(3), **line_kwargs)
        line_05 = Line(O_b - (LEFT * sin(15/180 * PI) + UP * cos(15/180 * PI)) * sqrt(2) * sqrt(3), O_b - (DOWN * sin(15/180 * PI) + LEFT * cos(15/180 * PI)) * sqrt(2) * sin(15/180 * PI) * sqrt(3), **line_kwargs)
        lines = VGroup(line_01, line_02, line_03, line_04, line_05)

        poly_kwargs = {
            "color": WHITE,
            "stroke_width": 2.,
            "fill_opacity": 0.95,
        }

        poly_01 = Polygon(O_a + (DOWN * sin(15/180 * PI) + LEFT * cos(15/180 * PI)) * sqrt(2), O_a + (DOWN * sin(15/180 * PI) + LEFT * cos(15/180 * PI)) * sqrt(2) * sin(15/180 * PI),
                          O_a + (LEFT * sin(15/180 * PI) + UP * cos(15/180 * PI)) * sqrt(2), fill_color=ORANGE, **poly_kwargs)
        poly_02 = Polygon(O_a - (DOWN * sin(15/180 * PI) + LEFT * cos(15/180 * PI)) * sqrt(2), O_a + (DOWN * sin(15/180 * PI) + LEFT * cos(15/180 * PI)) * sqrt(2) * sin(15/180 * PI),
                          O_a + (LEFT * sin(15/180 * PI) + UP * cos(15/180 * PI)) * sqrt(2), fill_color=GREEN, **poly_kwargs)
        poly_03 = Polygon(O_a + (DOWN * sin(15/180 * PI) + LEFT * cos(15/180 * PI)) * sqrt(2), O_a - (DOWN * sin(15/180 * PI) + LEFT * cos(15/180 * PI)) * sqrt(2) * sin(15/180 * PI),
                          O_a - (LEFT * sin(15/180 * PI) + UP * cos(15/180 * PI)) * sqrt(2), fill_color=GREEN, **poly_kwargs)
        poly_04 = Polygon(O_a - (DOWN * sin(15/180 * PI) + LEFT * cos(15/180 * PI)) * sqrt(2), O_a - (DOWN * sin(15/180 * PI) + LEFT * cos(15/180 * PI)) * sqrt(2) * sin(15/180 * PI),
                          O_a - (LEFT * sin(15/180 * PI) + UP * cos(15/180 * PI)) * sqrt(2), fill_color=ORANGE, **poly_kwargs)
        polys_01 = VGroup(poly_04, poly_03, poly_01, poly_02)

        poly_11 = Polygon(O_b + (DOWN * sin(15/180 * PI) + LEFT * cos(15/180 * PI)) * sqrt(2) * sqrt(3), O_b + (DOWN * sin(15/180 * PI) + LEFT * cos(15/180 * PI)) * sqrt(2) * sin(15/180 * PI) * sqrt(3),
                          O_b + (LEFT * sin(15/180 * PI) + UP * cos(15/180 * PI)) * sqrt(2) * sqrt(3), fill_color=QING, **poly_kwargs)
        poly_12 = Polygon(O_b - (DOWN * sin(15/180 * PI) + LEFT * cos(15/180 * PI)) * sqrt(2) * sqrt(3), O_b + (DOWN * sin(15/180 * PI) + LEFT * cos(15/180 * PI)) * sqrt(2) * sin(15/180 * PI) * sqrt(3),
                          O_b + (LEFT * sin(15/180 * PI) + UP * cos(15/180 * PI)) * sqrt(2) * sqrt(3), fill_color=ZHU, **poly_kwargs)
        poly_13 = Polygon(O_b + (DOWN * sin(15/180 * PI) + LEFT * cos(15/180 * PI)) * sqrt(2) * sqrt(3), O_b - (DOWN * sin(15/180 * PI) + LEFT * cos(15/180 * PI)) * sqrt(2) * sin(15/180 * PI) * sqrt(3),
                          O_b - (LEFT * sin(15/180 * PI) + UP * cos(15/180 * PI)) * sqrt(2) * sqrt(3), fill_color=ZHU, **poly_kwargs)
        poly_14 = Polygon(O_b - (DOWN * sin(15/180 * PI) + LEFT * cos(15/180 * PI)) * sqrt(2) * sqrt(3), O_b - (DOWN * sin(15/180 * PI) + LEFT * cos(15/180 * PI)) * sqrt(2) * sin(15/180 * PI) * sqrt(3),
                          O_b - (LEFT * sin(15/180 * PI) + UP * cos(15/180 * PI)) * sqrt(2) * sqrt(3), fill_color=QING, **poly_kwargs)
        polys_02 = VGroup(poly_13, poly_14, poly_12, poly_11)

        group_all = VGroup(triangle, cube_a, cube_b, cube_c, lines, polys_02, polys_01).scale_about_point(self.scale_all, ORIGIN)

        self.always_continually_update = True

        self.wait(0.1)
        self.add(triangle_abc)
        self.play(FadeIn(cube_a), FadeIn(cube_b), FadeIn(cube_c))
        self.wait()
        self.play(ShowCreation(line_01))
        self.wait(0.2)
        self.play(ShowCreation(line_02), ShowCreation(line_03), run_time=0.4)
        self.wait(0.2)
        self.play(ShowCreation(line_04), ShowCreation(line_05), run_time=0.4)
        self.wait(0.5)

        self.play(FadeIn(poly_01), run_time=0.3)
        self.play(FadeIn(poly_02), run_time=0.3)
        self.play(FadeIn(poly_03), run_time=0.3)
        self.play(FadeIn(poly_04), run_time=0.3)
        self.wait(0.5)

        self.play(FadeIn(poly_11), run_time=0.3)
        self.play(FadeIn(poly_12), run_time=0.3)
        self.play(FadeIn(poly_13), run_time=0.3)
        self.play(FadeIn(poly_14), run_time=0.3)
        self.wait()

        p11 = poly_11.copy()
        self.add(p11), self.remove(poly_11)
        self.rotate_about_point(p11, (O_b + (LEFT * sin(15/180 * PI) + UP * cos(15/180 * PI)) * sqrt(2) * sqrt(3)) * self.scale_all, PI/2)
        self.wait(0.5)
        p12 = poly_12.copy()
        self.add(p12), self.remove(poly_12)
        self.play(ApplyMethod(p11.shift, 2 * (1 + sqrt(3)) * (DOWN * sqrt(3)/2 + LEFT / 2) * self.scale_all),
                  ApplyMethod(p12.shift, 2 * (1 + sqrt(3)) * (DOWN * sqrt(3)/2 + LEFT / 2) * self.scale_all), run_time=1.25)
        self.wait(0.8)

        p14 = poly_14.copy()
        self.add(p14), self.remove(poly_14)
        self.rotate_about_point(p14, RIGHT * 2 * self.scale_all, PI/2)
        self.wait(0.5)
        p13 = poly_13.copy()
        self.add(p13), self.remove(poly_13)
        self.play(ApplyMethod(p14.shift, 4 * DOWN * self.scale_all),
                  ApplyMethod(p13.shift, 4 * DOWN * self.scale_all), run_time=1.25)
        self.wait(0.8)

        p02 = poly_02.copy()
        self.add(p02), self.remove(poly_02)
        self.rotate_about_point(p02, (O_a + (LEFT * sin(15/180 * PI) + UP * cos(15/180 * PI)) * sqrt(2)) * self.scale_all, -PI/2)
        self.wait(0.5)
        p01 = poly_01.copy()
        self.add(p01), self.remove(poly_01)
        self.play(ApplyMethod(p02.shift, 2 * (1 + sqrt(3)) * (RIGHT * sqrt(3)/2 + DOWN / 2) * self.scale_all),
                  ApplyMethod(p01.shift, 2 * (1 + sqrt(3)) * (RIGHT * sqrt(3)/2 + DOWN / 2) * self.scale_all), run_time=1.25)
        self.wait(0.8)

        p03 = poly_03.copy()
        self.add(p03), self.remove(poly_03)
        self.rotate_about_point(p03, LEFT * 2 * self.scale_all, -PI/2)
        self.wait(0.5)
        p04 = poly_04.copy()
        self.add(p04), self.remove(poly_04)
        self.play(ApplyMethod(p03.shift, 4 * DOWN * self.scale_all),
                  ApplyMethod(p04.shift, 4 * DOWN * self.scale_all), run_time=1.25)

        p_old = VGroup(polys_01, polys_02)
        p_new = VGroup(p04, p03, p01, p02, p13, p14, p12, p11)
        p_new_02 = VGroup(p04, p03, p01, p02, p13, p14, p12, p11).copy()
        self.wait(1.)

        self.play(ReplacementTransform(p_new, p_old), run_time=1)
        self.play(Write(TextMobject('$a^{2}$', color=RED, stroke_color=None).scale(1.6).move_to(cube_a)),
                  Write(TextMobject('$b^{2}$', color=YELLOW, stroke_color=None).scale(2).move_to(cube_b)))
        self.wait(0.5)
        self.play(ReplacementTransform(p_old, p_new_02), run_time=1)
        self.play(Write(TextMobject('$c^{2}$', color=GREEN, stroke_color=None).scale(2.8).move_to(cube_c)))

        self.wait(2.5)

    def rotate_about_point(self, Mobject, p, theta, run_time=1):

        dt = self.dt
        n = int(run_time/dt)
        d_theta = theta / n
        for i in range(n):
            # vec = p - Mobject.get_center()
            Mobject.shift(-p)
            Mobject.rotate_about_origin(d_theta - 0.0002)
            Mobject.shift(p)
            self.wait(dt)

class Pythagoras_Euclid(Scene):

    CONFIG = {
        'scale_all': 0.72,
        'dt': 1/29.5,
    }

    def construct(self):

        cube_kwargs = {
            "color": WHITE,
            "stroke_width": 1.6,
            "fill_opacity": 1,
        }
        cube1_kwargs = {
            "color": WHITE,
            "stroke_width": 1.6,
            "fill_opacity": 0.15,
        }

        O_a = (1 + sqrt(3)) * (LEFT * sqrt(3)/2 + UP * 0.5)
        O_b = (1 + sqrt(3)) * (RIGHT * 0.5 + UP * sqrt(3)/2)
        O_c = DOWN * 2

        triangle_abc = Polygon(np.array([-2, 0, 0]), np.array([2, 0, 0]), np.array([-1, sqrt(3), 0]), color=WHITE, stroke_width=2)
        cube = Cube(fill_opacity=0, stroke_width=1).scale(0.2).shift(RIGHT * 0.2 + DOWN * 0.2).rotate_about_origin(-PI/6).shift(np.array([-1, sqrt(3), 0]))
        triangle = VGroup(triangle_abc, cube)

        cube_a = Cube(fill_color=QING, **cube_kwargs).scale(1).move_to(O_a).rotate(PI/3)
        cube_b = Cube(fill_color=ZHU, **cube_kwargs).scale(sqrt(3)).move_to(O_b).rotate(-PI/6)
        cube_c = Cube(fill_color=PINK, **cube_kwargs).scale(2).move_to(O_c)

        cube_a1 = Cube(fill_color=QING, **cube1_kwargs).scale(1).move_to(O_a).rotate(PI/3)
        cube_b1 = Cube(fill_color=ZHU, **cube1_kwargs).scale(sqrt(3)).move_to(O_b).rotate(-PI/6)
        cube_c1 = Cube(fill_color=PINK, **cube1_kwargs).scale(2).move_to(O_c)
        cubes = VGroup(cube_a1, cube_b1, cube_c1)

        line_kwargs = {
            'color': WHITE,
            "stroke_width": 1.6,
        }

        dash_01 = DashedLine(O_a + (LEFT * sin(15/180 * PI) + UP * cos(15/180 * PI)) * sqrt(2), np.array([-1, sqrt(3) + 4, 0]), dash_length=0.2, **line_kwargs)
        dash_02 = DashedLine(O_b + (LEFT * sin(15/180 * PI) + UP * cos(15/180 * PI)) * sqrt(2) * sqrt(3), np.array([-1, sqrt(3) + 4, 0]), dash_length=0.2, **line_kwargs)
        dash_03 = DashedLine(np.array([-1, sqrt(3), 0]), np.array([-1, sqrt(3) + 4, 0]), dash_length=0.2, **line_kwargs)

        dashs = VGroup(dash_01, dash_02, dash_03)

        dash_11 = DashedLine(LEFT * 2, LEFT * 2 + UP * 4, dash_length=0.2, **line_kwargs)
        dash_12 = DashedLine(LEFT * 1 + DOWN * 4, LEFT * 1 + UP * sqrt(3), dash_length=0.2, **line_kwargs)
        dash_13 = DashedLine(RIGHT * 2, RIGHT * 2 + UP * 4, dash_length=0.2, **line_kwargs)

        dashs_2 = VGroup(dash_11, dash_12, dash_13)

        group_all = VGroup(triangle, cube_a, cube_b, cube_c, cubes, dashs, dashs_2).scale_about_point(self.scale_all, ORIGIN).shift(DOWN * 0.5)

        self.always_continually_update = True

        self.wait(0.1)
        self.add(triangle_abc)
        self.add(cubes)
        self.play(FadeIn(cube_a), FadeIn(cube_b), FadeIn(cube_c))
        self.wait()

        self.play(ShowCreation(dash_01))
        self.play(ShowCreation(dash_02))
        self.play(ShowCreation(dash_03))
        self.wait()

        # update cube_a
        time_a = 1.8
        na = int(time_a / self.dt)
        v = 2 * sqrt(3) / na * (sqrt(3) / 2 * UP + RIGHT / 2)
        for i in range(na):

            self.remove(cube_a)
            cube_a = Polygon(LEFT * 2, UP * sqrt(3) + LEFT, O_a + (LEFT * sin(15/180 * PI) + UP * cos(15/180 * PI)) * sqrt(2) + v * (i + 1),
                              O_a + (DOWN * sin(15/180 * PI) + LEFT * cos(15/180 * PI)) * sqrt(2) +  v * (i + 1),
                             fill_color=QING, **cube_kwargs).scale_about_point(self.scale_all, ORIGIN).shift(DOWN * 0.5)
            self.add(cube_a)
            self.wait(self.dt)

        self.wait()

        # update cube_b

        time_b = 1.8
        nb = int(time_b / self.dt)
        v = 2 / nb * (sqrt(3) / 2 * LEFT + UP / 2)
        for i in range(nb):

            self.remove(cube_b)
            cube_b = Polygon(RIGHT * 2, UP * sqrt(3) + LEFT, O_b + (LEFT * sin(15/180 * PI) + UP * cos(15/180 * PI)) * sqrt(2) * sqrt(3) + v * (i + 1),
                              O_b - (DOWN * sin(15/180 * PI) + LEFT * cos(15/180 * PI)) * sqrt(2) * sqrt(3) +  v * (i + 1),
                             fill_color=ZHU, **cube_kwargs).scale_about_point(self.scale_all, ORIGIN).shift(DOWN * 0.5)
            self.add(cube_b)
            self.wait(self.dt)

        self.wait()
        self.play(ShowCreation(dash_11))
        self.play(ShowCreation(dash_12))
        self.play(ShowCreation(dash_13))
        self.wait()

        self.play(ApplyMethod(cube_a.shift, DOWN * 4 * self.scale_all), ApplyMethod(cube_b.shift, DOWN * 4 * self.scale_all), run_time=1.8)
        self.wait()

        # update cube_a & cube_b
        time = 1.8
        n = int(time / self.dt)
        v = sqrt(3) * DOWN / n
        for i in range(n):
            self.remove(cube_a)
            self.remove(cube_b)
            cube_a = Polygon(LEFT * 2 + DOWN * 4, LEFT * 2, -v * (n - i - 1) + LEFT, -v * (n - i - 1) + DOWN * 4 + LEFT,
                             fill_color=QING, **cube_kwargs).scale_about_point(self.scale_all, ORIGIN).shift(DOWN * 0.5)
            cube_b = Polygon(RIGHT * 2 + DOWN * 4, RIGHT * 2, -v * (n - i - 1) + LEFT, -v * (n - i - 1) + DOWN * 4 + LEFT,
                             fill_color=ZHU, **cube_kwargs).scale_about_point(self.scale_all, ORIGIN).shift(DOWN * 0.5)
            self.add(cube_a)
            self.add(cube_b)
            self.wait(self.dt)

        self.wait(3)

class Pythagoras_Euclid_02(Scene):

    CONFIG = {
        'scale_all': 0.8,
        'dt': 1/29.5,
    }

    def construct(self):

        cube_kwargs = {
            "color": WHITE,
            "stroke_width": 1.6,
            "fill_opacity": 0.6,
        }
        cube1_kwargs = {
            "color": WHITE,
            "stroke_width": 1.6,
            "fill_opacity": 0.0,
        }

        O_a = (1 + sqrt(3)) * (LEFT * sqrt(3)/2 + UP * 0.5)
        O_b = (1 + sqrt(3)) * (RIGHT * 0.5 + UP * sqrt(3)/2)
        O_c = DOWN * 2

        triangle_abc = Polygon(np.array([-2, 0, 0]), np.array([2, 0, 0]), np.array([-1, sqrt(3), 0]), color=WHITE, stroke_width=2)
        cube = Cube(fill_opacity=0, stroke_width=1).scale(0.2).shift(RIGHT * 0.2 + DOWN * 0.2).rotate_about_origin(-PI/6).shift(np.array([-1, sqrt(3), 0]))
        triangle = VGroup(triangle_abc, cube)

        cube_a = Cube(fill_color=QING, **cube_kwargs).scale(1).move_to(O_a).rotate(PI/3)
        cube_b = Cube(fill_color=ZHU, **cube_kwargs).scale(sqrt(3)).move_to(O_b).rotate(-PI/6)
        cube_c = Cube(fill_color=PINK, **cube_kwargs).scale(2).move_to(O_c)

        cube_a1 = Cube(fill_color=QING, **cube1_kwargs).scale(1).move_to(O_a).rotate(PI/3)
        cube_b1 = Cube(fill_color=ZHU, **cube1_kwargs).scale(sqrt(3)).move_to(O_b).rotate(-PI/6)
        cube_c1 = Cube(fill_color=PINK, **cube1_kwargs).scale(2).move_to(O_c)
        cubes = VGroup(cube_a1, cube_b1, cube_c1)

        dash_kwargs = {
            "color": WHITE,
            "stroke_width": 1.6,
            "dash_length": 0.2,
        }

        dash_00 = DashedLine(O_a + (LEFT * cos(15/180 * PI) + DOWN * sin(15/180 * PI)) * sqrt(2),
                             O_b - (LEFT * cos(15/180 * PI) + DOWN * sin(15/180 * PI)) * sqrt(2) * sqrt(3), **dash_kwargs)
        dash_01 = DashedLine(O_a + (LEFT * cos(15/180 * PI) + DOWN * sin(15/180 * PI)) * sqrt(2), RIGHT * 2, **dash_kwargs)
        dash_02 = DashedLine(LEFT + sqrt(3) * UP, LEFT * 2 + DOWN * 4, **dash_kwargs)
        dash_03 = DashedLine(LEFT + sqrt(3) * UP, LEFT + 4 * DOWN, **dash_kwargs)
        dashes = VGroup(dash_00, dash_01, dash_02, dash_03)

        poly_kwargs = {
            "color": WHITE,
            # "fill_color":YELLOW,
            "stroke_width": 1.6,
            "fill_opacity": 0.8,
        }

        poly_01 = Polygon(O_a + (LEFT * cos(15/180 * PI) + DOWN * sin(15/180 * PI)) * sqrt(2), LEFT * 2,
                         LEFT + sqrt(3) * UP, fill_color=QING, **poly_kwargs)

        rect_01 = Polygon(LEFT * 2, LEFT * 2 + DOWN * 4, LEFT * 1 + DOWN * 4, LEFT, fill_color=QING, **poly_kwargs)
        rect_02 = Polygon(RIGHT * 2, RIGHT * 2 + DOWN * 4, LEFT * 1 + DOWN * 4, LEFT, fill_color=ZHU, **poly_kwargs)
        polys = VGroup(poly_01, rect_01, rect_02)

        group_all = VGroup(triangle, cube_a, cube_b, cube_c, cubes, dashes, polys).scale_about_point(self.scale_all, ORIGIN).shift(DOWN * 0.25)

        self.always_continually_update = True

        self.wait(0.1)
        self.add(triangle)
        self.add(cubes)
        self.play(FadeIn(cube_a1), FadeIn(cube_b1), FadeIn(cube_c1))
        self.wait(0.125)
        a2 = TextMobject('$a^{2}$', color=QING).scale(1.5).move_to(cube_a)
        b2 = TextMobject('$b^{2}$', color=ZHU).scale(1.8).move_to(cube_b)
        c2 = TextMobject('$c^{2}$', color=PINK).scale(2.4).move_to(cube_c).shift(UP * 0.15)
        self.play(Write(a2), Write(b2), Write(c2))
        self.wait(1.)
        self.play(ShowCreation(dash_00), FadeOut(a2), FadeOut(b2), FadeOut(c2), run_time=1.2)
        self.play(ShowCreation(dash_01), run_time=0.75)
        self.play(ShowCreation(dash_02), run_time=0.75)
        self.play(ShowCreation(dash_03), run_time=0.75)
        self.wait(0.8)
        self.play(FadeIn(poly_01), run_time=1.2)
        self.wait(0.8)

        ## update step 01 ##
        poly_02 = poly_01.copy()
        self.add(poly_02.set_fill(QING, 0.8))
        time = 1.25
        n = int(time/self.dt)
        v = sqrt(3) * 2 * (RIGHT * cos(PI/6) + DOWN * sin(PI/6)) / n
        for i in range(1, n+1):
            self.remove(poly_01)
            poly_01 = Polygon(O_a + (LEFT * cos(15/180 * PI) + DOWN * sin(15/180 * PI)) * sqrt(2), LEFT * 2,
                         LEFT + sqrt(3) * UP + v * i, fill_color=QING, **poly_kwargs).scale_about_point(self.scale_all, ORIGIN).shift(DOWN * 0.25)
            self.add(poly_01)
            self.wait(self.dt)
        self.wait()
        self.rotate_about_point(poly_01, LEFT * 2 * self.scale_all + DOWN * 0.25, -PI/2, 1.25)
        self.wait()

        ## update step 02 ##
        time = 1.25
        n = int(time/self.dt)
        v = DOWN * sqrt(3) / n
        for i in range(1, n+1):
            self.remove(poly_01)
            poly_01 = Polygon(LEFT * 2, LEFT * 2 + DOWN * 4, LEFT + sqrt(3) * UP + v * i, fill_color=QING, **poly_kwargs).scale_about_point(self.scale_all, ORIGIN).shift(DOWN * 0.25)
            self.add(poly_01)
            self.wait(self.dt)
        self.wait()

        mult_2 = TextMobject('$\\times 2$').scale(1.2).shift(DOWN * 1.5 + LEFT * 3.2)
        v1 = Vector(1.4 *RIGHT).next_to(mult_2, RIGHT * 0.4)
        v2 = Vector((RIGHT * cos(PI/3) + UP * sin(PI/3)) * 1.8).next_to(mult_2, UP * 0.4).shift(RIGHT * 0.5)

        self.play(Write(mult_2), ShowCreation(v1), ShowCreation(v2))
        self.wait(0.8)
        # self.play(ReplacementTransform(poly_01, rect_01), ReplacementTransform(poly_02, cube_a), run_time=1.2)

        self.play(FadeIn(rect_01), FadeOut(poly_01), FadeIn(cube_a), FadeOut(poly_02),
                  FadeOut(VGroup(mult_2, v1, v2)))
        self.wait(1.6)

        self.play(FadeIn(cube_b), run_time=0.9)
        self.wait(0.5)
        self.play(TransformFromCopy(cube_b, rect_02), run_time=1.2)

        self.wait(2.5)

    def rotate_about_point(self, Mobject, p, theta, run_time=1):

        dt = self.dt
        n = int(run_time/dt)
        d_theta = theta / n
        for i in range(n):
            # vec = p - Mobject.get_center()
            Mobject.shift(-p)
            Mobject.rotate_about_origin(d_theta - 0.0002)
            Mobject.shift(p)
            self.wait(dt)

class Pythagoras_Euclid_03(Scene):

    CONFIG = {
        'scale_all': 0.8,
        'dt': 1/29.5,
    }

    def construct(self):

        cube_kwargs = {
            "color": WHITE,
            "stroke_width": 1.6,
            "fill_opacity": 0.6,
        }
        cube1_kwargs = {
            "color": WHITE,
            "stroke_width": 1.6,
            "fill_opacity": 0.0,
        }

        O_a = (1 + sqrt(3)) * (LEFT * sqrt(3)/2 + UP * 0.5)
        O_b = (1 + sqrt(3)) * (RIGHT * 0.5 + UP * sqrt(3)/2)
        O_c = DOWN * 2

        triangle_abc = Polygon(np.array([-2, 0, 0]), np.array([2, 0, 0]), np.array([-1, sqrt(3), 0]), color=WHITE, stroke_width=2)
        cube = Cube(fill_opacity=0, stroke_width=1).scale(0.2).shift(RIGHT * 0.2 + DOWN * 0.2).rotate_about_origin(-PI/6).shift(np.array([-1, sqrt(3), 0]))
        triangle = VGroup(triangle_abc, cube)

        cube_a = Cube(fill_color=QING, **cube_kwargs).scale(1).move_to(O_a).rotate(PI/3)
        cube_b = Cube(fill_color=ZHU, **cube_kwargs).scale(sqrt(3)).move_to(O_b).rotate(-PI/6)
        cube_c = Cube(fill_color=PINK, **cube_kwargs).scale(2).move_to(O_c)

        cube_a1 = Cube(fill_color=QING, **cube1_kwargs).scale(1).move_to(O_a).rotate(PI/3)
        cube_b1 = Cube(fill_color=ZHU, **cube1_kwargs).scale(sqrt(3)).move_to(O_b).rotate(-PI/6)
        cube_c1 = Cube(fill_color=PINK, **cube1_kwargs).scale(2).move_to(O_c)
        cubes = VGroup(cube_a1, cube_b1, cube_c1)

        dash_kwargs = {
            "color": WHITE,
            "stroke_width": 1.6,
            "dash_length": 0.2,
        }

        dash_00 = DashedLine(O_a + (LEFT * cos(15/180 * PI) + DOWN * sin(15/180 * PI)) * sqrt(2),
                             O_b - (LEFT * cos(15/180 * PI) + DOWN * sin(15/180 * PI)) * sqrt(2) * sqrt(3), **dash_kwargs)
        dash_01 = DashedLine(O_a + (LEFT * cos(15/180 * PI) + DOWN * sin(15/180 * PI)) * sqrt(2), RIGHT * 2, **dash_kwargs)
        dash_02 = DashedLine(LEFT + sqrt(3) * UP, LEFT * 2 + DOWN * 4, **dash_kwargs)
        dash_03 = DashedLine(LEFT + sqrt(3) * UP, LEFT + 4 * DOWN, **dash_kwargs)
        dashes = VGroup(dash_00, dash_01, dash_02, dash_03)

        poly_kwargs = {
            "color": WHITE,
            # "fill_color":YELLOW,
            "stroke_width": 1.6,
            "fill_opacity": 0.8,
        }

        poly_01 = Polygon(O_a + (LEFT * cos(15/180 * PI) + DOWN * sin(15/180 * PI)) * sqrt(2), LEFT * 2,
                         LEFT + sqrt(3) * UP, fill_color=QING, **poly_kwargs)

        rect_01 = Polygon(LEFT * 2, LEFT * 2 + DOWN * 4, LEFT * 1 + DOWN * 4, LEFT, fill_color=QING, **poly_kwargs)
        rect_02 = Polygon(RIGHT * 2, RIGHT * 2 + DOWN * 4, LEFT * 1 + DOWN * 4, LEFT, fill_color=ZHU, **poly_kwargs)
        polys = VGroup(poly_01, rect_01, rect_02)

        group_all = VGroup(triangle, cube_a, cube_b, cube_c, cubes, dashes, polys).scale_about_point(self.scale_all, ORIGIN).shift(DOWN * 0.25)

        self.always_continually_update = True


        self.add(triangle)

        self.add(cube_a, cube_b)
        self.add(rect_01, rect_02)
        self.wait()
        cube_c_ab = VGroup(rect_01, rect_02)

        text = TextMobject(*['$a^{2}$', '     +     ', '$b^{2}$', '     =     ', '$c^{2}$']).scale(2.7).shift(LEFT * 0.2)
        text.set_color_by_tex_to_color_map({
            '$a^{2}$': QING,
            '$b^{2}$': ZHU,
            '$c^{2}$': PINK,
        })
        text[0].shift(LEFT * 1.)
        text[1].shift(LEFT * 0.6)
        text[3].shift(RIGHT * 0.75)
        text[4].shift(RIGHT * 1.2)
        text[1].scale(0.75), text[3].scale(0.75)

        self.play(FadeOut(triangle))
        self.play(ApplyMethod(cube_a.move_to, text[0].get_center() + RIGHT * 0.5),
                  ApplyMethod(cube_b.move_to, text[2].get_center() + RIGHT * 0.1),
                  ApplyMethod(cube_c_ab.move_to, text[4].get_center() + RIGHT * 0.2), run_time=1.25)
        self.wait(0.6)
        self.play(Write(text[1]))
        self.wait(0.2)
        self.play(Write(text[3]))
        self.wait()
        self.play(ReplacementTransform(cube_a, text[0]))
        self.wait(0.2)
        self.play(ReplacementTransform(cube_b, text[2]))
        self.wait(0.2)
        self.play(ReplacementTransform(cube_c_ab, text[4]))

        self.wait(2.5)

class Leonardo_da_Vinci(Scene):

    CONFIG = {
        'scale_all': 0.65,
        'dt': 1/29.5,
    }

    def construct(self):

        self.create_cubes(PI/6)
        self.play(FadeIn(self.all_obj[0][0]), FadeIn(self.all_obj[1]), run_time=1)

        self.wait(0.32)
        self.play(FadeIn(self.all_obj[0][1]), FadeIn(self.all_obj[0][2]), run_time=1)
        self.wait(0.6)
        self.play(ShowCreation(self.all_obj[2]), run_time=1.5)
        self.wait()

        self.always_continually_update = True
        self.all_obj.set_fill(BLACK, 0), self.all_obj.set_color(BLACK)

        theta_list = list(np.linspace(PI/6, PI * 1/12, int(0.6/self.dt))) + list(np.linspace(PI/12, PI * 5/12, int(2./self.dt))) + list(np.linspace(PI * 5/12, PI/3, int(0.6/self.dt)))

        for theta in theta_list:
            self.create_cubes(theta)
            self.add(self.all_obj)
            self.wait(self.dt)
            self.remove(self.all_obj)

        self.create_cubes(PI/3)
        self.add(self.left_part)
        self.add(self.right_part)
        self.wait(1.2)

        vector_left = LEFT * 3.2 + DOWN * 1.6
        vector_right = RIGHT * 4. + UP * 1.2
        self.play(ApplyMethod(self.left_part.shift, vector_left),
                  ApplyMethod(self.right_part.shift, vector_right), run_time=1.2)
        self.polys[0].shift(vector_left), self.polys[1].shift(vector_left)
        self.polys[2].shift(vector_right), self.polys[3].shift(vector_right)
        self.wait(0.8)

        self.play(FadeIn(self.polys[0]), run_time=0.8)
        self.wait(0.4)
        self.play(TransformFromCopy(self.polys[0], self.polys[2]), run_time=1.25)
        self.wait()

        self.play(FadeIn(self.polys[1]), run_time=0.8)
        self.wait(0.4)
        self.play(TransformFromCopy(self.polys[1], self.polys[3]), run_time=1.25)
        self.wait()

        self.play(Write(TextMobject('=').scale(2.5).shift(RIGHT * 1.05)), run_time=1)
        self.wait(1)
        self.play(FadeOut(self.polys), run_time=1.2)
        self.wait()

        self.play(FadeOut(self.left_part[0]), FadeOut(self.left_part[1]), FadeOut(self.left_part[-1]),
                  FadeOut(self.right_part[0]), FadeOut(self.right_part[1]), FadeOut(self.right_part[-1]), run_time=1)
        self.wait(0.8)
        text_l = TextMobject(*['$a^{2}$', '+', '$b^{2}$'], color=WHITE).\
            set_color_by_tex_to_color_map({'$a^{2}$': QING, '$b^{2}$': ZHU,}).\
            scale(2.5).move_to(self.left_part).shift(RIGHT * 0.6)
        text_r = TextMobject('$c^{2}$', color=PINK).scale(2.5).move_to(self.right_part[3]).shift(LEFT * 0.72 + UP * 0.1)
        self.play(ReplacementTransform(VGroup(self.left_part[2], self.left_part[3]), text_l))
        self.wait(0.2)
        self.play(ReplacementTransform(self.right_part[2], text_r))

        self.wait(2.4)

    def create_cubes(self, theta):

        O_a = (2 * sin(theta) + 2 * cos(theta)) * (LEFT * cos(theta) + UP * sin(theta))
        O_b = (2 * sin(theta) + 2 * cos(theta)) * (UP * cos(theta) + RIGHT * sin(theta))
        O_c = DOWN * 2

        triangle_abc = Polygon(np.array([-2, 0, 0]), np.array([2, 0, 0]), np.array([-2 * cos(2 * theta), 2 * sin(2 * theta), 0]), color=WHITE, stroke_width=2)
        cube = Cube(fill_opacity=0, stroke_width=1).scale(0.2).shift(RIGHT * 0.2 + DOWN * 0.2).rotate_about_origin(-theta).shift(np.array([-2 * cos(2 * theta), 2 * sin(2 * theta), 0]))
        triangle = VGroup(triangle_abc, cube)
        triangle_02 = Polygon(2 * RIGHT + 4 * (sin(theta) + cos(theta)) * (LEFT * cos(theta) + UP * sin(theta)),
                              2 * LEFT + 4 * (sin(theta) + cos(theta)) * (UP * cos(theta) + RIGHT * sin(theta)),
                              np.array([-2 * cos(2 * theta), 2 * sin(2 * theta), 0]), color=WHITE, stroke_width=2)
        # triangle_03 = Polygon(2 * RIGHT + 4 * DOWN, 2 * LEFT + 4 * DOWN, 4 * DOWN + 2 * (cos(2 * theta) * RIGHT + sin(2 * theta) * DOWN), color=WHITE, stroke_width=2)

        triangle_03 = triangle.copy().scale_about_point(-1, O_c)

        cube_kwargs = {
            "color": WHITE,
            "stroke_width": 1.6,
            "fill_opacity": 1,
        }
        cube_a = Cube(fill_color=QING, **cube_kwargs).scale(sin(theta) * 2).move_to(O_a).rotate(-theta)
        cube_b = Cube(fill_color=ZHU, **cube_kwargs).scale(cos(theta) * 2).move_to(O_b).rotate(-theta)
        cube_c = Cube(fill_color=PINK, **cube_kwargs).scale(2).move_to(O_c)

        dash_kwargs = {
            "color": WHITE,
            "stroke_width": 1.6,
            "dash_length": 0.2,
        }

        dash_01 = DashedLine(4 * DOWN + 2 * (cos(2 * theta) * RIGHT + sin(2 * theta) * DOWN), np.array([-2 * cos(2 * theta), 2 * sin(2 * theta), 0]), **dash_kwargs)
        dash_02 = DashedLine(LEFT * 2 + (LEFT * cos(theta) + UP * sin(theta)) * 4 * sin(theta), RIGHT * 2 + (RIGHT * sin(theta) + UP * cos(theta)) * 4 * cos(theta), **dash_kwargs)

        poly_kwargs = {
            "color": YELLOW,
            "fill_color":YELLOW,
            "stroke_width": 2,
            "fill_opacity": 0.8,
        }
        poly_kwargs02 = {
            "color": GREEN,
            "fill_color":GREEN,
            "stroke_width": 2,
            "fill_opacity": 0.8,
        }
        poly_01 = Polygon(LEFT * 2, RIGHT * 2, RIGHT * 2 + (RIGHT * sin(theta) + UP * cos(theta)) * 4 * cos(theta),
                          LEFT * 2 + (LEFT * cos(theta) + UP * sin(theta)) * 4 * sin(theta), **poly_kwargs)
        poly_02 = Polygon(2 * RIGHT + 4 * (sin(theta) + cos(theta)) * (LEFT * cos(theta) + UP * sin(theta)),
                          2 * LEFT + 4 * (sin(theta) + cos(theta)) * (UP * cos(theta) + RIGHT * sin(theta)),
                          RIGHT * 2 + (RIGHT * sin(theta) + UP * cos(theta)) * 4 * cos(theta),
                          LEFT * 2 + (LEFT * cos(theta) + UP * sin(theta)) * 4 * sin(theta), **poly_kwargs02)
        poly_03 = Polygon(LEFT * 2 + DOWN * 4, LEFT * 2, np.array([-2 * cos(2 * theta), 2 * sin(2 * theta), 0]),
                          4 * DOWN + 2 * (cos(2 * theta) * RIGHT + sin(2 * theta) * DOWN), **poly_kwargs)
        poly_04 = Polygon(RIGHT * 2 + DOWN * 4, RIGHT * 2, np.array([-2 * cos(2 * theta), 2 * sin(2 * theta), 0]),
                          4 * DOWN + 2 * (cos(2 * theta) * RIGHT + sin(2 * theta) * DOWN), **poly_kwargs02)

        self.polys = VGroup(poly_01, poly_02, poly_03, poly_04).scale_about_point(self.scale_all, ORIGIN).shift(UP * 0.2)

        triangles = VGroup(triangle, triangle_02, triangle_03)
        cubes = VGroup(cube_a, cube_b, cube_c)
        dashes = VGroup(dash_01, dash_02)

        self.all_obj = VGroup(triangles, cubes, dashes).scale_about_point(self.scale_all, ORIGIN).shift(UP * 0.2)
        self.left_part = VGroup(triangle.copy(), triangle_02.copy(), cube_a.copy(), cube_b.copy(), dash_02.copy())
        self.right_part = VGroup(triangle.copy(), triangle_03.copy(), cube_c.copy(), dash_01.copy())

class Pythagoras_liuhui(Scene):

    CONFIG = {
        'scale_all': 1,
    }

    def construct(self):

        QING, QING_A, QING_0 = '#1984D6', '#19B5ED', '#99D7FF'
        ZHU, ZHU_A, ZHU_0 = '#D44712', '#F46C1B', '#FFA952'

        cube_kwargs = {
            "color": WHITE,
            "stroke_width": 1,
            "fill_opacity": 0.6,
        }

        new_origin = DOWN * 1.2 + RIGHT * 1
        O_a = (UP + LEFT) * sqrt(3) + new_origin
        O_b = RIGHT + UP + new_origin
        O_c = RIGHT * 2 + LEFT * 2 * sqrt(2) * cos(15 * PI/180) + UP * 2 * sqrt(2) * sin(15 * PI/180) + new_origin

        cube_a = Cube(fill_color=QING_A, **cube_kwargs).scale(sqrt(3)).move_to(O_a).set_fill(QING_0, 0)
        cube_b = Cube(fill_color=ZHU_A, **cube_kwargs).scale(1).move_to(O_b).set_fill(ZHU_0, 0)
        cube_c = Cube(**cube_kwargs).scale(2).move_to(O_c).rotate(PI/6).set_fill(YELLOW, 0)
        # cubes = VGroup(cube_a, cube_b, cube_c)

        text_a = TextMobject('a', color=QING).scale(1.25).next_to(cube_a, UP * 0.6)
        text_b = TextMobject('b', color=ZHU).scale(1.25).next_to(cube_b, UP * 0.6).shift(RIGHT * 0.1)
        text_c = TextMobject('c', color=PINK).scale(1.25).next_to(cube_c, DOWN * 0.6).shift(RIGHT * 1.25 + UP * 0.9)
        texts = VGroup(text_a, text_b, text_c)

        poly_kwargs = {
            "color": WHITE,
            "stroke_width": 2,
            "fill_opacity": 0.95,
        }

        poly_01 = Polygon(np.array([-2 * sqrt(3), 2 * sqrt(3) - 2, 0]), UP * 2 * sqrt(3), (LEFT + UP) * 2 * sqrt(3), fill_color=QING_A, **poly_kwargs).shift(new_origin)
        poly_02 = Polygon(np.array([-2 * sqrt(3), 2 * sqrt(3) - 2, 0]), LEFT * 2 * sqrt(3), LEFT * 2 * sqrt(3) + RIGHT * 2 * (sqrt(3) - 1)/sqrt(3), fill_color=QING_A, **poly_kwargs).shift(new_origin)
        poly_03 = Polygon(np.array([-2 * sqrt(3), 2 * sqrt(3) - 2, 0]), LEFT * 2 * sqrt(3) + RIGHT * 2 * (sqrt(3) - 1)/sqrt(3), ORIGIN, UP * 2 * sqrt(3), fill_color=QING, **poly_kwargs).shift(new_origin)
        qing = VGroup(poly_03, poly_02, poly_01).copy()

        poly_04 = Polygon(ORIGIN, RIGHT * 2, UP * 2 + RIGHT * (2 * (sqrt(3) - 1)/sqrt(3)), UP * 2, fill_color=ZHU, **poly_kwargs).shift(new_origin)
        poly_05 = Polygon(RIGHT * 2, (RIGHT + UP) * 2, UP * 2 + RIGHT * (2 * (sqrt(3) - 1)/sqrt(3)), fill_color=ZHU_A, **poly_kwargs).shift(new_origin)
        zhu = VGroup(poly_04, poly_05).copy()

        qing_zhu = VGroup(poly_03, poly_04, poly_01, poly_05, poly_02)

        self.wait(0.4)
        self.play(FadeIn(cube_a), FadeIn(cube_b))
        self.play(Write(text_a), Write(text_b))
        self.wait(0.8)
        self.play(ShowCreation(cube_c), run_time=0.85)
        self.play(Write(text_c))
        self.wait(0.8)

        self.play(FadeIn(qing_zhu))
        self.wait(0.8)

        cube_a.set_fill(QING_0, 0.25)
        cube_b.set_fill(ZHU_0, 0.25)

        self.play(ApplyMethod(poly_01.shift, 2 * (DOWN * sqrt(3) + RIGHT)), run_time=1.45)
        self.play(ApplyMethod(poly_05.shift, 2 * (LEFT * sqrt(3) + DOWN)), run_time=1.45)
        self.play(ApplyMethod(poly_02.shift, -2 * (LEFT * sqrt(3) + DOWN)), run_time=1.45)
        self.wait(2)

        # self.play(FadeOut(qing_zhu), FadeOut(cubes), FadeOut(texts), run_time=0.8)
        # self.wait(0.6)

        qing.scale(0.9).move_to(LEFT * 4.8)
        zhu.scale(0.9).move_to(LEFT * 1)
        qing_zhu_new = qing_zhu.copy().scale(0.9).move_to(RIGHT * 4)

        self.remove(cube_c)
        self.play(ReplacementTransform(cube_a, qing), ReplacementTransform(cube_b, zhu), ReplacementTransform(qing_zhu, qing_zhu_new),
                  FadeOut(texts), run_time=1.2)
        self.wait(0.4)

        # self.play(FadeIn(qing), run_time=0.4)
        self.play(FadeIn(TextMobject('+').scale(1.5).next_to(qing, RIGHT * 1.5)), run_time=0.45)
        # self.play(FadeIn(zhu), run_time=0.4)
        self.play(FadeIn(TextMobject('=').scale(1.5).next_to(zhu, RIGHT * 2.5)), run_time=0.45)
        # self.play(FadeIn(qing_zhu), run_time=0.4)


        self.wait(1.25)
        self.play(ReplacementTransform(qing, TextMobject('$a^{2}$', color=QING).scale(3).move_to(qing).shift(RIGHT * 0.45 + UP * 0.1)))
        self.play(ReplacementTransform(zhu, TextMobject('$b^{2}$', color=ZHU).scale(3).move_to(zhu).shift(UP * 0.1)))
        self.play(ReplacementTransform(qing_zhu_new, TextMobject('$c^{2}$', color=PINK).scale(3).move_to(qing_zhu_new).shift(LEFT * 1.45 + UP * 0.1)))

        self.wait(2)

class Pythagoras_tree(Scene):

    CONFIG = {
        'scale_all': 1,
        'tree_layer': 10,
        'tree_color': [QING, ZHU],
        'init_angle': PI/180 * 53,
    }

    def construct(self):

        self.create_tree()



    def create_tree(self):

        cube_kwargs = {
            "color": WHITE,
            "stroke_width": 1,
            "fill_opacity": 1,
        }
        self.all_obj = VGroup()

        n = self.tree_layer
        cube_c = Cube(**cube_kwargs)

        for i in range(n):

            cube_c = Cube(**cube_kwargs)

class Pythagoras_by_scaling(Scene):

     CONFIG = {}

     def construct(self):

         triangle_abc = Polygon(np.array([-4, -1.5, 0]), np.array([4, -1.5, 0]), np.array([2, -1.5 + 2 * sqrt(3), 0]),
                                color=WHITE, stroke_width=3.6, fill_color=PINK, fill_opacity=0.25)
         cube = Cube(fill_opacity=0, stroke_width=1.8).scale(0.4).shift(RIGHT * 0.4 + DOWN * 0.4).\
             rotate_about_origin(-PI/3).shift(np.array([2, -1.5 + 2 * sqrt(3), 0]))

         triangle_01 = VGroup(triangle_abc, cube).scale(0.75)

         tri_2 = Polygon(np.array([4, -1.5, 0]), np.array([4, -1.5 + 2 * sqrt(3), 0]), np.array([2, -1.5 + 2 * sqrt(3), 0]),
                                color=WHITE, stroke_width=3.6, fill_color=QING, fill_opacity=0.25)
         cube_2 = Cube(fill_opacity=0, stroke_width=1.8).scale(0.2).shift(LEFT * 0.2 + DOWN * 0.2).shift(np.array([4, -1.5 + 2 * sqrt(3), 0]))
         triangle_02 = VGroup(tri_2, cube_2)

         tri_3 = Polygon(np.array([-4, -1.5, 0]), np.array([-4, -1.5 + 2 * sqrt(3), 0]), np.array([2, -1.5 + 2 * sqrt(3), 0]),
                                color=WHITE, stroke_width=3.6, fill_color=ZHU, fill_opacity=0.25)
         cube_3 = Cube(fill_opacity=0, stroke_width=1.8).scale(0.3).shift(RIGHT * 0.3 + DOWN * 0.3).shift(np.array([-4, -1.5 + 2 * sqrt(3), 0]))
         triangle_03 = VGroup(tri_3, cube_3)

         b = TextMobject('b', color=ZHU).scale(1.5).shift(LEFT * 0.8 + UP * 0.75)
         a = TextMobject('a', color=QING).scale(1.5).shift(RIGHT * 2.5 + UP * 0.6)
         c = TextMobject('c', color=PINK).scale(1.5).shift(DOWN * 1.4)

         b_c = TextMobject(*['b', '$\\times$', 'c']).set_color_by_tex_to_color_map({'b':ZHU, 'c':PINK})\
             .scale(1.5).shift(LEFT * 1.4 + UP * 1.)
         a_c = TextMobject(*['a', '$\\times$', 'c']).set_color_by_tex_to_color_map({'a':QING, 'c':PINK})\
             .scale(1.5).shift(RIGHT * 3.9 + UP * 0.8)
         c_c = TextMobject(*['c', '$\\times$', 'c']).set_color_by_tex_to_color_map({'c':PINK})\
             .scale(1.5).shift(DOWN * 2)
         bc = TextMobject('bc', color=ZHU).scale(1.45).shift(LEFT * 1.15 + UP * 0.7)
         ac = TextMobject('ac', color=QING).scale(1.45).shift(RIGHT * 3.35 + UP * 0.54)
         c2 = TextMobject('$c^{2}$', color=PINK).scale(1.45).shift(DOWN * 1.95)

         ## anim triangle_01 ##

         self.play(ShowCreation(triangle_abc), run_time=0.8)
         self.wait(0.25)
         self.play(FadeIn(cube))
         self.wait(0.5)

         self.play(Write(a))
         self.wait(0.1)
         self.play(Write(b))
         self.wait(0.1)
         self.play(Write(c))
         self.wait()

         self.play(ApplyMethod(triangle_01.scale, 4/3), ReplacementTransform(b, b_c),
                   ReplacementTransform(a, a_c), ReplacementTransform(c, c_c), run_time=1.25)
         self.wait(0.75)
         self.play(ReplacementTransform(b_c, bc), ReplacementTransform(a_c, ac), ReplacementTransform(c_c, c2), run_time=1.25)
         self.wait(1.2)

         ## anim triangle_02 ##
         self.play(FadeIn(triangle_02), run_time=1)
         self.wait()

         ab = TextMobject('ab', color=QING).scale(1.45).shift(RIGHT * 4.54 + UP * 0.56)
         a2 = TextMobject('$a^{2}$', color=QING).scale(1.45).shift(RIGHT * 3.25 + UP * 2.4)

         self.play(Write(ab), run_time=1.)
         self.wait(0.5)
         self.play(Write(a2))
         self.wait(1.2)

         ## anim triangle_03 ##

         self.play(FadeIn(triangle_03), run_time=1)
         self.wait()

         ba = TextMobject('ba', color=ZHU).scale(1.45).shift(LEFT * 4.5 + UP * 0.7)
         b2 = TextMobject('$b^{2}$', color=ZHU).scale(1.45).shift(LEFT * 1.05 + UP * 2.4)

         self.play(Write(ba), run_time=1.)
         self.wait(0.5)
         self.play(Write(b2))
         self.wait(2)

         ## conclusion
         line_01 = Line(np.array([-4.03, -1.5 + 2 * sqrt(3), 0]), np.array([2, -1.5 + 2 * sqrt(3), 0]), color=ZHU, stroke_width=20)
         line_02 = Line(np.array([2, -1.5 + 2 * sqrt(3), 0]), np.array([4.03, -1.5 + 2 * sqrt(3), 0]), color=QING, stroke_width=20)
         line_03 = Line(np.array([-4.03, -1.5, 0]), np.array([4.03, -1.5, 0]), color=PINK, stroke_width=20)
         self.play(ShowCreation(line_01), run_time=0.75)
         self.wait(0.2)
         self.play(ShowCreation(line_02), run_time=0.5)
         self.wait(0.4)
         self.play(ShowCreation(line_03), run_time=1)
         self.wait()
         self.play(ApplyMethod(VGroup(triangle_01, triangle_02, triangle_03, a2, b2, c2, ab, ac, bc, ba, line_01, line_02, line_03).shift, UP * 0.8), time=1)

         text = TextMobject(*['$a^{2}$', '+', '$b^{2}$', '=', '$c^{2}$']).scale(2.5).shift(DOWN * 2.5)
         text.set_color_by_tex_to_color_map({
             '$a^{2}$': QING,
             '$b^{2}$': ZHU,
             '$c^{2}$': PINK,
         })

         self.play(TransformFromCopy(a2, text[0]))
         self.wait(0.1)
         self.play(TransformFromCopy(b2, text[2]))
         self.wait(0.1)
         self.play(TransformFromCopy(c2, text[-1]))
         self.wait(0.1)
         self.play(Write(text[1]), Write(text[3]))

         self.wait(2.5)

class Pythagoras_by_CirclePower(Scene):

    def construct(self):
        loc = UP + LEFT * 1.75

        A = RIGHT * 2 + loc
        B = LEFT * 2 + loc
        C = np.array([-1, sqrt(3), 0]) + loc
        D = ORIGIN + loc
        E = LEFT * 4 + loc

        p_list = [A, B, C, D, E]

        p_group = VGroup()
        for p in p_list:
            p_group.add(Dot(p, color=YELLOW))

        triangle_abc = Polygon(A, B, C)
        cube = Cube(color=BLUE, fill_opacity=0, stroke_width=1.8).scale(0.1).shift(0.1 * (RIGHT + DOWN)).rotate_about_origin(-30 * DEGREES).shift(C)
        circle = Circle(radius=2).move_to(B)
        L_BE = Line(B, E, color=BLUE)

        text_A = TextMobject('A', color=YELLOW).move_to(A).shift(DOWN * 0.3)
        text_B = TextMobject('B', color=YELLOW).move_to(B).shift(DOWN * 0.3)
        text_C = TextMobject('C', color=YELLOW).move_to(C).shift((UP + RIGHT) * 0.2)
        text_D = TextMobject('D', color=YELLOW).move_to(D).shift(DOWN * 0.3 + RIGHT * 0.3)
        text_E = TextMobject('E', color=YELLOW).move_to(E).shift(DOWN * 0.3 + LEFT * 0.3)

        t_a = TextMobject('a', color=RED).shift((B + C)/2 + (LEFT + UP) * 0.15)
        t_b = TextMobject('b', color=BLUE).shift((A + C)/2 + RIGHT * 0.12 +UP * 0.25)
        t_c = TextMobject('c', color=PINK).move_to(D).shift(UP *0.25 + RIGHT * 0.25)
        t_a02 = TextMobject('a', color=RED).shift((B +E)/2 + DOWN * 0.25)
        t_a03 = TextMobject('a', color=RED).shift((D +B)/2 + DOWN * 0.25)

        text_01 = TextMobject(*['$AC^{2}$', '=', '$AE\\times AD$', '$\\Leftrightarrow$', '$b^{2}$', '= (', 'c', '+', 'a', '$)\\times($', 'c',  '-', 'a', ') =', '$c^{2}$', '-', '$a^{2}$'], color=WHITE)#.scale(0.95)
        text_01.set_color_by_tex_to_color_map({
            '$AC^{2}$': YELLOW,
            '$AE\\times AD$': YELLOW,
            # '$\\Leftrightarrow$': WHITE,
            '$b^{2}$': BLUE,
            '$c^{2}$': PINK,
            '$a^{2}$': RED,
            'c': PINK,
            'a': RED,
        })
        text_01[3].set_color(WHITE)
        text_01.shift(DOWN * 2).align_to(text_E, LEFT)

        text_02 = TextMobject(*['$\\Leftrightarrow$', '$c^{2}$', '=', '$a^{2}$', '+', '$b^{2}$'])
        text_02.set_color_by_tex_to_color_map({
            '$b^{2}$': BLUE,
            '$c^{2}$': PINK,
            '$a^{2}$': RED,
        })
        text_02.shift(DOWN * 2.8).align_to(text_01[3], LEFT)

        self.add(triangle_abc, cube)
        self.wait(0.5)
        self.play(Write(t_a), Write(t_b), Write(t_c))
        self.wait()

        self.play(ShowCreation(circle), run_time=1.25)
        self.wait(0.5)

        self.play(ShowCreation(L_BE), runtime=1)
        self.wait(0.25)
        self.play(Write(t_a02), Write(t_a03))
        self.wait(0.5)
        self.play(Write(text_A), Write(text_B), Write(text_C),
                  ShowCreation(p_group[0]), ShowCreation(p_group[1]), ShowCreation(p_group[2]))
        self.play(Write(text_D), ShowCreation(p_group[3]))
        self.play(Write(text_E), ShowCreation(p_group[4]))
        self.wait(1.25)

        self.play(Write(text_01), run_time=1.8)
        self.wait(1.2)
        self.play(Write(text_02), run_time=1)

        self.wait(3)

class Ptolemy_Theorem(Scene):

    CONFIG = {
        'loc': LEFT * 3.8 + UP * 0.5,
        'r': 2.4,
    }

    def construct(self):

        self.always_continually_update = True

        loc = self.loc
        center = ORIGIN + loc
        r = self.r

        circle = Circle(radius=r).move_to(center)

        theta_a = -160 * DEGREES
        theta_b = -20 * DEGREES
        theta_c = 80 * DEGREES
        theta_d = 120 * DEGREES

        A = r * (UP * sin(theta_a) + RIGHT * cos(theta_a)) + loc
        B = r * (UP * sin(theta_b) + RIGHT * cos(theta_b)) + loc
        C = r * (UP * sin(theta_c) + RIGHT * cos(theta_c)) + loc
        D = r * (UP * sin(theta_d) + RIGHT * cos(theta_d)) + loc

        dot_O = Dot(loc, color=YELLOW)

        dot_A = Dot(A, color=YELLOW)
        dot_B = Dot(B, color=YELLOW)
        dot_C = Dot(C, color=YELLOW)
        dot_D = Dot(D, color=YELLOW)

        t_O = TextMobject('O', color=YELLOW).move_to(dot_O).shift(DOWN * 0.3 + LEFT * 0.2)
        t_A = TextMobject('A', color=YELLOW).move_to(dot_A).shift(DOWN * 0.3 + LEFT * 0.2)
        t_B = TextMobject('B', color=YELLOW).move_to(dot_B).shift(DOWN * 0.3 + RIGHT * 0.2)
        t_C = TextMobject('C', color=YELLOW).move_to(dot_C).shift(UP * 0.3 + RIGHT * 0.2)
        t_D = TextMobject('D', color=YELLOW).move_to(dot_D).shift(UP * 0.3 + LEFT * 0.2)

        p_O = VGroup(t_O, dot_O)
        p_B = VGroup(t_B, dot_B)
        p_C = VGroup(t_C, dot_C)
        p_D = VGroup(t_D, dot_D)
        p_A = VGroup(t_A, dot_A)

        AB = Line(A, B, color=BLUE)
        AC = Line(A, C, color=BLUE)
        DA = Line(D, A, color=BLUE)
        BC = Line(B, C, color=BLUE)
        BD = Line(B, D, color=BLUE)
        CD = Line(C, D, color=BLUE)

        self.p_group = VGroup(p_O, p_A, p_B, p_C, p_D)
        self.line_group = VGroup(AB, AC, DA, BC, BD, CD)

        self.play(ShowCreation(circle), run_time=1.5)
        self.wait(0.2)
        self.play(ShowCreation(p_O))
        self.wait(0.4)
        self.play(ShowCreation(AB), run_time=0.15)
        self.play(ShowCreation(BC), run_time=0.15)
        self.play(ShowCreation(CD), run_time=0.15)
        self.play(ShowCreation(DA), run_time=0.15)
        self.play(ShowCreation(AC), run_time=0.15)
        self.play(ShowCreation(BD), run_time=0.15)

        self.wait(0.25)
        self.play(ShowCreation(p_A), ShowCreation(p_B), ShowCreation(p_C), ShowCreation(p_D), run_time=1.25)
        self.wait(0.6)


        title = TextMobject('托勒密定理：', color=BLUE).to_corner(LEFT * 12.8 + UP * 1.6)
        text01 = TextMobject('圆的内接凸四边形两对边乘积之和').scale(0.8).to_corner(LEFT * 12.8 + UP * 3)
        text02 = TextMobject('等于两条对角线的乘积').scale(0.8).to_corner(LEFT * 12.8 + UP * 4.2)
        formula_01 = TextMobject(*['即：', 'AD', '$\\times$', 'BC', '+', 'AB', '$\\times$', 'CD', '=', 'AC', '$\\times$', 'BD'])
        formula_01.set_color_by_tex_to_color_map({
            'AB': YELLOW, 'BC': YELLOW, 'CD': YELLOW, 'AC': YELLOW, 'BD': YELLOW, 'BC': YELLOW, 'AD': YELLOW,
        })
        formula_01.scale(0.8)
        formula_01[1:12].scale(0.9).shift(LEFT * 0.4)
        formula_01.to_corner(LEFT * 12.8 + UP * 5.5)

        Ptolemy = VGroup(title, text01, text02, formula_01)

        self.play(Write(title))
        self.wait(0.2)
        self.play(Write(text01), run_time=2.4)
        self.wait(0.12)
        self.play(Write(text02), run_time=2.)
        self.wait(0.8)
        self.play(Write(formula_01), run_time=1.8)
        self.wait(0.9)

        self.play(ShowCreation(SurroundingRectangle(Ptolemy, color=BLUE)))
        self.wait(1.5)

        text03 = TextMobject(*['当四边形', 'ABCD', '为矩形', '，可得：']).scale(0.8).to_corner(LEFT * 12.8 + UP * 7.5)
        text03[1].set_color(YELLOW)
        self.play(Write(text03[0:3]), run_time=1.8)

        final_a, final_b, final_c, final_d = -150 * DEGREES, -30 * DEGREES, 30 * DEGREES, 150 * DEGREES
        dt = 1/30
        n = 48
        d_a, d_b, d_c, d_d = (final_a - theta_a) / n, (final_b - theta_b) / n, (final_c - theta_c) / n, (final_d - theta_d) / n
        self.p_group.set_opacity(0.2)
        self.line_group.set_opacity(0.2)
        for i in range(n):
            self.remove(self.p_group, self.line_group)
            self.create_ABCD(theta_a + d_a * (i+1), theta_b + d_b * (i+1), theta_c + d_c * (i+1), theta_d + d_d * (i+1))
            self.add(self.line_group, self.p_group)
            self.wait(dt)

        formula_02 = TextMobject('BC', '$\\times$', 'BC', '+', 'AB', '$\\times$', 'AB', '=', 'AC', '$\\times$', 'AC').scale(0.8)
        formula_02.set_color_by_tex_to_color_map({
            'AB': ZHU, 'BC': BLUE, 'AC': PINK,
        }).to_corner(LEFT * 12.8 + UP * 9)
        self.play(Write(text03[3]), run_time=1)
        self.play(Write(formula_02), run_time=1.8)
        self.wait(1.5)

        formula_03 = TextMobject('$BC^{2}$', '+', '$AB^{2}$', '=', '$AC^{2}$').scale(0.9)
        formula_03.set_color_by_tex_to_color_map({
            '$AB^{2}$': ZHU, '$BC^{2}$': BLUE, '$AC^{2}$': PINK,
        }).to_corner(LEFT * 12.8 + UP * 10.6)

        self.play(TransformFromCopy(formula_02, formula_03), run_time=1.5)
        self.wait(0.6)

        self.play(ShowCreation(SurroundingRectangle(formula_03, color=GREEN)))
        self.wait(0.6)
        self.play(Write(TextMobject('$\\checkmark$', color=GREEN).scale(1.2).next_to(formula_03, RIGHT * 1.6)), run_time=1.25)

        self.wait(4)


    def create_ABCD(self, theta_a, theta_b, theta_c, theta_d):

        r = self.r
        loc = self.loc

        A = r * (UP * sin(theta_a) + RIGHT * cos(theta_a)) + loc
        B = r * (UP * sin(theta_b) + RIGHT * cos(theta_b)) + loc
        C = r * (UP * sin(theta_c) + RIGHT * cos(theta_c)) + loc
        D = r * (UP * sin(theta_d) + RIGHT * cos(theta_d)) + loc

        dot_O = Dot(loc, color=YELLOW)

        dot_A = Dot(A, color=YELLOW)
        dot_B = Dot(B, color=YELLOW)
        dot_C = Dot(C, color=YELLOW)
        dot_D = Dot(D, color=YELLOW)

        t_O = TextMobject('O', color=YELLOW).move_to(dot_O).shift(DOWN * 0.3 + LEFT * 0.2)
        t_A = TextMobject('A', color=YELLOW).move_to(dot_A).shift(DOWN * 0.3 + LEFT * 0.2)
        t_B = TextMobject('B', color=YELLOW).move_to(dot_B).shift(DOWN * 0.3 + RIGHT * 0.2)
        t_C = TextMobject('C', color=YELLOW).move_to(dot_C).shift(UP * 0.3 + RIGHT * 0.2)
        t_D = TextMobject('D', color=YELLOW).move_to(dot_D).shift(UP * 0.3 + LEFT * 0.2)

        p_O = VGroup(dot_O, t_O)
        p_B = VGroup(dot_B, t_B)
        p_C = VGroup(dot_C, t_C)
        p_D = VGroup(dot_D, t_D)
        p_A = VGroup(dot_A, t_A)
        self.p_group = VGroup(p_O, p_A, p_B, p_C, p_D)

        AB = Line(A, B, color=BLUE)
        AC = Line(A, C, color=BLUE)
        DA = Line(D, A, color=BLUE)
        BC = Line(B, C, color=BLUE)
        BD = Line(B, D, color=BLUE)
        CD = Line(C, D, color=BLUE)
        self.line_group = VGroup(AB, AC, DA, BC, BD, CD)

class Pythagoras_06(Scene):

    CONFIG = {
        'scale_factor': 0.72,
    }

    def construct(self):

        loc = LEFT * 4.5

        A = np.array([sqrt(3), -1, 0]) + loc
        B = np.array([-sqrt(3), 1, 0]) + loc
        C = np.array([-sqrt(3), -1, 0]) + loc

        p1 = np.array([2 - sqrt(3), 1 + 2 * sqrt(3), 0]) + loc
        p2 = np.array([2 + sqrt(3), 1 + 2 * sqrt(3), 0]) + loc
        p3 = np.array([2 + sqrt(3), -1 + 2 * sqrt(3), 0]) + loc
        p4 = np.array([2 + sqrt(3), -1, 0]) + loc
        p5 = np.array([2 + sqrt(3), -1 - 2 / sqrt(3), 0]) + loc
        p6 = np.array([2 + sqrt(3), -1 - 2 * sqrt(3), 0]) + loc
        p7 = np.array([sqrt(3), -1 - 2 * sqrt(3), 0]) + loc
        p8 = np.array([-sqrt(3), -1 - 2 * sqrt(3), 0]) + loc
        p9 = np.array([-2 - sqrt(3), -1 - 2 * sqrt(3), 0]) + loc
        p10 = np.array([-2 - sqrt(3), -1, 0]) + loc
        p11 = np.array([-2 - sqrt(3), 1, 0]) + loc
        p12 = np.array([-2 - sqrt(3), 1 + 2 / sqrt(3), 0]) + loc
        p13 = np.array([-2 - sqrt(3), 1 + 2 * sqrt(3), 0]) + loc
        p14 = np.array([-sqrt(3), 1 + 2 * sqrt(3), 0]) + loc

        poly_config = {
            "stroke_width": 1.5,
            "fill_opacity": 1,
        }
        ABC = Polygon(A, B, C, color=GREEN, stroke_color=GREEN, **poly_config).scale_about_point(self.scale_factor, ORIGIN)
        cube_a = Polygon(B, p11, p10, C, color=ZHU, stroke_color=ZHU, **poly_config).scale_about_point(self.scale_factor, ORIGIN)
        cube_b = Polygon(A, C, p8, p7, color=QING, stroke_color=QING, **poly_config).scale_about_point(self.scale_factor, ORIGIN)
        cube_c = Polygon(A, p3, p1, B, color=PINK, stroke_color=PINK, **poly_config).scale_about_point(self.scale_factor, ORIGIN)
        rect = Polygon(p2, p6, p9, p13, color=WHITE, stroke_width=0, fill_color=GREEN_A, fill_opacity=0).scale_about_point(self.scale_factor, ORIGIN)

        center = Dot(loc, color=YELLOW).scale(1.5).scale_about_point(self.scale_factor, ORIGIN)

        poly_config_02 = {
            "color": GREEN_A,
            "stroke_width": 1.5,
            "stroke_color": GREEN_A,
            "fill_opacity": 1,
        }


        poly01 = Polygon(p1, p3, p2, **poly_config_02).scale_about_point(self.scale_factor, ORIGIN)
        poly02 = Polygon(p3, A, p4, **poly_config_02).scale_about_point(self.scale_factor, ORIGIN)
        poly03 = Polygon(p4, A, p5, **poly_config_02).scale_about_point(self.scale_factor, ORIGIN)
        poly04 = Polygon(p5, A, p7, p6, **poly_config_02).scale_about_point(self.scale_factor, ORIGIN)
        poly05 = Polygon(C, p9, p8, **poly_config_02).scale_about_point(self.scale_factor, ORIGIN)
        poly06 = Polygon(C, p10, p9, **poly_config_02).scale_about_point(self.scale_factor, ORIGIN)
        poly07 = Polygon(B, p11, p12, **poly_config_02).scale_about_point(self.scale_factor, ORIGIN)
        poly08 = Polygon(B, p12, p13, p14, **poly_config_02).scale_about_point(self.scale_factor, ORIGIN)
        poly09 = Polygon(B, p14, p1, **poly_config_02).scale_about_point(self.scale_factor, ORIGIN)

        cut_line = Line(p12 + (p12 - p5) * 3, p5 + (p5 - p12) * 3, color=YELLOW, stroke_width=10).scale_about_point(self.scale_factor, ORIGIN)


        poly_left = Polygon(p12, p5, p6, p9, color=GREEN, fill_opacity=0, stroke_width=0).scale_about_point(self.scale_factor, ORIGIN)
        poly_right = Polygon(p2, p5, p12, p13, color=GREEN, fill_opacity=0, stroke_width=0).scale_about_point(self.scale_factor, ORIGIN)
        poly_group = VGroup(poly01, poly02, poly03, poly04, poly05, poly06, poly07, poly08, poly09)

        left = VGroup(ABC, cube_a, cube_b, poly04, poly05, poly06, poly07)
        right = VGroup(cube_c, poly01, poly02, poly03, poly09, poly08)

        left_all = VGroup(left, poly_left)
        right_all = VGroup(right, poly_right)

        self.add(rect)
        self.play(FadeIn(ABC))
        self.wait(0.2)
        self.play(FadeIn(cube_a), FadeIn(cube_b), FadeIn(cube_c), run_time=0.8)
        self.wait()
        # self.play(ShowCreation(rect))
        # self.wait(0.6)
        self.play(ApplyMethod(rect.set_opacity, 1), run_time=1.)
        self.add(poly_group)
        self.play(FadeOut(rect), run_time=0.2)
        self.wait(1.)

        self.play(FadeInFromLarge(center))


        text_01 = TextMobject('直角三角形斜边的中点').scale(0.9).to_corner(LEFT * 14.5 + UP * 2)
        text_02 = TextMobject('为大矩形的几何中心，').scale(0.9).to_corner(LEFT * 14.5 + UP * 3.5)
        text_03 = TextMobject('过该点的直线将大矩形').scale(0.9).to_corner(LEFT * 14.5 + UP * 5)
        text_04 = TextMobject('分成面积相等的两部分').scale(0.9).to_corner(LEFT * 14.5 + UP * 6.5)

        text = VGroup(text_01, text_02, text_03, text_04)
        rect_text = SurroundingRectangle(text, color=YELLOW)
        arrow = Arrow(center.get_center(), rect_text.get_center() + (rect_text.get_right()[0] - rect_text.get_left()[0])/2 * LEFT, color=YELLOW)

        self.play(ShowCreation(arrow))
        self.wait(0.25)
        self.play(ShowCreation(rect_text))
        self.wait(0.25)
        for i in range(4):
            self.play(Write(text[i]), run_time=1.6)
            self.wait(0.12)
        self.wait(1.)

        self.play(FadeOut(text), FadeOut(rect_text), FadeOut(arrow), run_time=1)
        self.wait(0.4)

        self.play(ShowCreation(cut_line), FadeOut(center), run_time=0.36)
        self.play(FadeOut(cut_line), ApplyMethod(left_all.shift, DOWN * 0.025), ApplyMethod(right_all.shift, UP * 0.025), run_time=0.5)
        self.play(ApplyMethod(left_all.shift, LEFT * 0.5), ApplyMethod(right_all.shift, RIGHT * 6.75), run_time=1.2)
        self.wait(0.5)
        # self.play(ApplyMethod(right.rotate, 90*DEGREES), run_time=1.2)

        theta = 180 * DEGREES
        t = 2.5
        n = 72
        c = right_all.get_center()
        for i in range(n):
            right_all.shift(-c)
            right_all.rotate_about_origin(theta/n)
            right_all.shift(c)
            self.wait(t/n)
        s = poly_right.get_center()[1] - poly_left.get_center()[1]
        t = 1.4
        n = 40
        for i in range(n):
            # right.rotate(theta/n)
            right_all.shift(DOWN * s/n + RIGHT * 0.25/n)
            self.wait(t/n)
        self.wait()

        ##
        text_05 = TextMobject('左右两部分面积相等，同时去掉全等的部分面积任然相等').scale(0.8).to_corner(UP * 1.5 + LEFT * 1.5)
        self.play(Write(text_05), run_time=1.8)
        self.wait(0.2)
        self.play(Write(TextMobject('=').scale(1.6).shift(DOWN * 1.5 + RIGHT * 0.05)))
        self.play(ApplyMethod(poly_group.set_stroke, WHITE, 2.5), run_time=1.)

        def remove_pair(A, B):
            center = (A.get_center() + B.get_center())/2
            self.play(ApplyMethod(A.set_stroke, YELLOW, 5), ApplyMethod(B.set_stroke, YELLOW, 5), run_time=0.75)
            self.wait(0.25)
            self.remove(A, B)
            A2 = A.copy()
            B2 = B.copy()
            self.play(ApplyMethod(A2.move_to, center), ApplyMethod(B2.move_to, center), run_time=0.6)
            self.wait(0.1)
            self.play(FadeOutAndShiftDown(A2), FadeOutAndShiftDown(B2))

        remove_pair(poly03, poly07)
        self.wait(0.5)
        remove_pair(poly02, poly06)
        self.wait(0.5)
        remove_pair(poly09, poly05)
        self.wait(0.5)
        remove_pair(poly04, poly08)
        self.wait(0.5)
        remove_pair(poly01, ABC)
        self.wait(0.5)

        formula = TextMobject(*['$a^{2}$', '+', '$b^{2}$', '=', '$c^{2}$']).scale(2.4).shift(UP * 2.25 + LEFT * 1)
        formula.set_color_by_tex_to_color_map({
            '$a^{2}$': ZHU, '$b^{2}$': QING, '$c^{2}$': PINK,
        })

        self.play(ApplyMethod(cube_a.shift, RIGHT * 1.5), ApplyMethod(cube_b.shift, RIGHT * 1.5), FadeOut(text_05))
        self.wait(0.25)
        self.play(TransformFromCopy(cube_a, formula[0]))
        self.wait(0.25)
        self.play(TransformFromCopy(cube_b, formula[2]))
        self.wait(0.25)
        self.play(Write(formula[1]))
        self.wait(0.5)
        self.play(TransformFromCopy(cube_c, formula[4]))
        self.wait(0.25)
        self.play(Write(formula[3]))
        self.wait(0.8)
        self.play(Write(TextMobject('$\\checkmark$', color=GREEN).scale(2.25).next_to(formula, RIGHT * 3)), run_time=1.2)
        self.wait(4)

class Pythagoras_incircle(Scene):

    def construct(self):

        loc = LEFT * 5.6 + UP * 0.65

        a = 2.4
        b = a * 4/3

        c = sqrt(a ** 2 + b ** 2)
        r = (a + b - c) / 2

        C = loc
        A = loc + b * RIGHT
        B = loc + a * UP

        ABC = Polygon(A, B, C, color=WHITE)
        cube = Cube(color=BLUE, fill_opacity=0, stroke_width=2).scale(0.12).shift(C + 0.12 * (UP + RIGHT))
        triangle = VGroup(ABC, cube)

        center = Dot(C + r * (UP + RIGHT), color=GREEN)
        circle = Circle(radius=r, color=YELLOW).shift(C + r * (UP + RIGHT))
        arrow = Arrow(center.get_center(), center.get_center() + r * (LEFT + UP) * sqrt(2)/2, color=GREEN).scale(2.4)

        text_a = TextMobject('a', color=ZHU).scale(1.1).move_to(C).shift(UP * a / 2 + LEFT * 0.3)
        text_b = TextMobject('b', color=QING).scale(1.1).move_to(C).shift(RIGHT * b / 2 + DOWN * 0.3)
        text_c = TextMobject('c', color=PINK).scale(1.1).move_to(C).shift(UP * a / 2 + RIGHT * b / 2 + (RIGHT + UP) * 0.3/sqrt(2))
        text_r = TextMobject('r', color=GREEN).scale(1.1).move_to(center).shift(UP * 0.54 + LEFT * 0.2)

        title = TextMobject('直角三角形内接圆半径公式：').scale(1.0).to_corner(LEFT * 10.5 + UP * 1.25)
        formula_01 = TextMobject(*['r', '=', '$\\frac{a + b - c}{2}$']).scale(1.4).to_corner(LEFT * 12. + UP * 3.)
        formula_01.set_color_by_tex_to_color_map({
            'r':GREEN,
            '$\\frac{a + b - c}{2}$':PINK,
        })
        formula_02 = TextMobject(*['r', '=', '$\\frac{ab}{a + b + c}$']).scale(1.4).to_corner(LEFT * 12. + UP * 5.35)
        formula_02.set_color_by_tex_to_color_map({
            'r':GREEN,
            '$\\frac{ab}{a + b + c}$':PINK,
        })

        self.add(triangle)
        self.play(Write(text_a), Write(text_b), Write(text_c), run_time=0.8)
        self.wait(0.4)

        self.play(ShowCreation(circle), run_time=1.2)
        self.wait(0.2)
        self.play(FadeIn(center), ShowCreation(arrow), run_time=1.)
        self.wait(0.2)
        self.play(Write(text_r), run_time=0.8)
        self.wait()
        self.play(Write(title), run_time=1.2)
        self.wait(0.6)
        self.play(TransformFromCopy(text_r, formula_01[0]))
        self.play(Write(formula_01[1]))
        self.play(Write(formula_01[2]), run_time=1.25)
        self.wait(0.8)
        self.play(TransformFromCopy(text_r, formula_02[0]))
        self.play(Write(formula_02[1]))
        self.play(Write(formula_02[2]), run_time=1.25)
        self.wait(1.8)

        ## proof 01
        triangle_01 = triangle.copy()
        circle_01 = circle.copy()
        # center_01 = center.copy()
        D = loc + (a-r) * b/c * RIGHT + (b-r) * a/c * UP
        tri_config = {
            "stroke_width": 2.5,
            'stroke_color': WHITE,
            "fill_opacity": 0.3,
        }
        shift_down = DOWN* 3.6
        tri_01 = Polygon(B, B + DOWN * (a-r), center.get_center(), color=ZHU, **tri_config)
        tri_02 = Polygon(B, D, center.get_center(), color=ZHU, **tri_config)
        tri_11 = Polygon(A, A + LEFT * (b-r), center.get_center(), color=QING, **tri_config)
        tri_12 = Polygon(A, D, center.get_center(), color=QING, **tri_config)
        cube = Polygon(C, C + r * RIGHT, center.get_center(), C + r * UP, color=PINK, **tri_config)
        poly_group = VGroup(tri_01, tri_11, tri_02, tri_12, cube).shift(shift_down)

        #text_r01 = TextMobject('r', color=GREEN)
        text_ar = TextMobject(*['a', '-', 'r']).set_color_by_tex_to_color_map({'a':ZHU, 'b':QING, 'r':GREEN})
        text_br = TextMobject(*['b', '-', 'r']).set_color_by_tex_to_color_map({'a':ZHU, 'b':QING, 'r':GREEN})

        self.play(ApplyMethod(triangle_01.shift, shift_down), ApplyMethod(circle_01.shift, shift_down))
        self.wait(0.5)
        self.play(FadeIn(poly_group), run_time=1.5)
        self.wait(0.4)
        r1 = text_r.copy().scale(1/1.1).next_to(cube, DOWN * 0.6)
        r2 = text_r.copy().scale(1/1.1).next_to(cube, LEFT * 0.6)
        r3 = text_r.copy().scale(1/1.1).next_to(cube, UP * 0.6)
        r4 = text_r.copy().scale(1/1.1).next_to(cube, RIGHT * 0.6)
        r5 = text_r.copy().scale(1/1.1).next_to(cube, RIGHT * 1).shift(UP * 0.6)
        self.play(Write(r1), Write(r2), Write(r3), Write(r4), Write(r5))
        self.wait(0.5)
        ar1 = text_ar.copy().rotate(PI/2).next_to(tri_01, LEFT * 0.6)
        br1 = text_br.copy().next_to(tri_11, DOWN * 0.6)
        self.play(Write(ar1), Write(br1))
        self.wait(0.5)
        ar2 = text_ar.copy().rotate(-np.arctan(3/4)).next_to(tri_02, (RIGHT + UP) * 0.1).shift(LEFT * 0.65 + DOWN * 0.65/3*4 + LEFT * 0.2 + UP * 0.15)
        br2 = text_br.copy().rotate(-np.arctan(3/4)).next_to(tri_12, (RIGHT + UP) * 0.1).shift(LEFT * 0.9 + DOWN * 1.2 + LEFT * 0.32 + UP * 0.32 * 3/4)
        self.play(Write(ar2), Write(br2))
        self.wait(0.5)

        text01 = TextMobject(*['显然：', 'a', '-', 'r', '+', 'b', '-', 'r', '=', 'c']).set_color_by_tex_to_color_map({
            'a': ZHU, 'b': QING, 'c': PINK, 'r': GREEN
        }).to_corner(LEFT * 10.5 + DOWN * 5.6)
        text02 = TextMobject(*['$\\Rightarrow\\quad$', 'r', '=', '$\\frac{a + b - c}{2}$']).set_color_by_tex_to_color_map({
            '$\\Rightarrow\\quad$': WHITE, 'r': GREEN, '$\\frac{a + b - c}{2}$': PINK,
        }).to_corner(LEFT * 10.5 + DOWN * 3)
        text02[0].set_color(GREEN)
        text02[1:4].scale(1.2)
        self.play(Write(text01[0]))
        self.play(TransformFromCopy(ar2, text01[1:4]))
        self.play(Write(text01[4]), run_time=0.54)
        self.play(TransformFromCopy(br2, text01[5:8]))
        self.play(Write(text01[8]), run_time=0.54)
        self.play(TransformFromCopy(text_c, text01[9]), run_time=1)
        self.wait()
        self.play(Write(text02), run_time=1.8)
        self.play(ShowCreation(SurroundingRectangle(formula_01, color=GREEN)))
        self.play(Write(TextMobject('$\\checkmark$', color=GREEN).scale(1.25).next_to(formula_01, RIGHT * 2.5)))
        self.wait(2)

        ## proof 02
        self.play(FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), FadeOut(r5),
                  FadeOut(ar1), FadeOut(ar2), FadeOut(br1), FadeOut(br2),
                  FadeOut(text01), FadeOut(text02))
        self.wait(0.75)
        self.play(ApplyMethod(poly_group.set_opacity, 0.8))
        self.wait(0.6)

        group_01 = VGroup(triangle_01, circle_01, poly_group)
        vect = loc + shift_down + a/2 * UP + b/2 * RIGHT + 0.075 * (RIGHT +UP)
        group_02 = group_01.copy().shift(-vect).rotate_about_origin(PI).shift(vect)

        self.play(FadeIn(group_02), run_time=1.2)
        self.wait(0.9)

        loc_new = DOWN * 1.24 + LEFT * 2.75

        config_new = {
            "stroke_width": 2,
            'stroke_color': WHITE,
            "fill_opacity": 0.8,
        }

        tri_ar_1 = Polygon(loc_new, loc_new + (a-r)*RIGHT, loc_new + UP * r, color=ZHU, **config_new)
        tri_ar_2 = Polygon(loc_new + r * UP, loc_new + r * UP + RIGHT * (a-r), loc_new + RIGHT * (a-r), color=ZHU, **config_new)
        cube_r_1 = Polygon(loc_new + r * UP + RIGHT * (a-r), loc_new + RIGHT * (a-r),
                    loc_new + RIGHT * a, loc_new + RIGHT * a + r * UP, color=PINK, **config_new)
        cube_r_2 = cube_r_1.copy().shift(b*RIGHT)
        tri_br_1 = Polygon(loc_new, loc_new + (b-r)*RIGHT, loc_new + UP * r, color=QING, **config_new)
        tri_br_2 = Polygon(loc_new + r * UP, loc_new + r * UP + RIGHT * (b-r), loc_new + RIGHT * (b-r), color=QING, **config_new)

        ar_rect_1 = VGroup(tri_ar_1, tri_ar_2)
        ar_rect_2 = ar_rect_1.copy().shift(RIGHT * (a + b))
        br_rect_1 = VGroup(tri_br_1, tri_br_2).shift(RIGHT * a)
        br_rect_2 = br_rect_1.copy().shift(RIGHT * (a - r + b))

        rect_right = VGroup(ar_rect_1, cube_r_1, br_rect_1, cube_r_2, ar_rect_2, br_rect_2)

        rect_left = VGroup(group_01, group_02)
        self.play(ApplyMethod(group_01.shift, LEFT * 1), ApplyMethod(group_02.shift, LEFT * 1), TransformFromCopy(rect_left, rect_right), run_time=1.8)

        brace_a = Brace(Line(loc_new, loc_new + RIGHT * a)).shift(UP * 0.15)
        t_a = TextMobject('a', color=ZHU).next_to(brace_a, DOWN * 0.5)
        brace_b = Brace(Line(loc_new + RIGHT * a, loc_new + RIGHT * (a + b))).shift(UP * 0.15)
        t_b = TextMobject('b', color=QING).next_to(brace_b, DOWN * 0.36)
        brace_c = Brace(Line(loc_new + RIGHT * (a + b), loc_new + RIGHT * (a + b + c))).shift(UP * 0.15)
        t_c = TextMobject('c', color=QING).next_to(brace_c, DOWN * 0.5)

        brace_text = VGroup(brace_a, brace_b, brace_c, t_a, t_b, t_c)

        self.play(ShowCreation(brace_a), Write(t_a), ShowCreation(brace_b), Write(t_b), ShowCreation(brace_c), Write(t_c))
        self.wait(1.2)

        text_2 = TextMobject(*['左右面积相等：', 'a', 'b', '=', 'r', '(', 'a', '+', 'b', '+', 'c', ')']).to_corner(LEFT * 9 + DOWN * 2.25)
        text_2.set_color_by_tex_to_color_map({
            'a': ZHU, 'b':QING, 'r': GREEN, 'c':PINK,
        })

        self.play(Write(text_2[0]))
        self.wait()
        self.play(TransformFromCopy(rect_left, text_2[1:3]))
        self.wait(0.5)
        self.play(Write(text_2[3]))
        self.wait(0.5)
        self.play(TransformFromCopy(rect_right, text_2[4:12]))
        self.wait(1.2)

        self.play(TransformFromCopy(text_2[1:14], formula_02), run_time=1.5)
        self.play(ShowCreation(SurroundingRectangle(formula_02, color=GREEN)))
        self.play(Write(TextMobject('$\\checkmark$', color=GREEN).scale(1.25).next_to(formula_02, RIGHT * 2.5)))
        self.wait(2)

        self.play(FadeOut(rect_left), FadeOut(rect_right), FadeOut(brace_text), FadeOut(text_2))
        self.wait(0.8)

        ## conclusion
        formula_new = VGroup(formula_01.copy(), formula_02.copy()).to_corner(LEFT * 3 + UP * 9)
        brace_new = Brace(formula_new, RIGHT)
        text_final = TextMobject(*['$\\Rightarrow$', '$a^{2}$', '+', '$b^{2}$', '=', '$c^{2}$']).scale(1.8).next_to(brace_new, RIGHT).shift(UP * 0.16)
        text_final.set_color_by_tex_to_color_map({
            '$\\Rightarrow$': WHITE, '$a^{2}$': ZHU, '$b^{2}$': QING, '$c^{2}$': PINK,
        })

        self.play(TransformFromCopy(VGroup(formula_01, formula_02), formula_new))
        self.wait(0.8)
        self.play(ShowCreation(brace_new))
        self.wait(1)
        self.play(Write(text_final), run_tiem=2.25)
        self.wait(0.6)
        self.play(Write(TextMobject('$\\checkmark$', color=GREEN).scale(2).next_to(text_final, RIGHT * 2.)), run_time=1.6)

        self.wait(4)

class Pythagoras_07(Scene):

    def construct(self):

        loc = LEFT * 4. + DOWN * 0.75

        a = 1.6
        b = 2.5
        c = sqrt(a ** 2 + b ** 2)

        C = loc
        A = loc + RIGHT * b
        B = loc + UP * a

        ABC = Polygon(A, B, C, color=WHITE, stroke_width=2)
        cube = Cube(color=WHITE, fill_opacity=0, stroke_width=1.5).scale(0.16).shift((C + UP * 0.16 + RIGHT * 0.16))
        cube_a = Polygon(B, C, C + LEFT * a, B + LEFT * a, color=WHITE, stroke_width=2)
        cube_b = Polygon(A, C, C + DOWN * b, A + DOWN * b, color=WHITE, stroke_width=2)
        cube_c = Polygon(A, B, B + c * (UP * b/c + RIGHT * a/c), A + c * (UP * b/c + RIGHT * a/c), color=WHITE, stroke_width=2)

        tri_ab1 = Polygon(A, C, C + DOWN * a, color=WHITE, stroke_width=2).shift(np.array([0,0,1]))
        tri_ab2 = Polygon(A, A + DOWN * b, A + DOWN * b + LEFT * a, color=WHITE, stroke_width=2)

        tri_1 = Polygon(C + DOWN * a, C + DOWN * a + RIGHT * (b-a), A, color=WHITE, stroke_width=2)
        tri_2 = Polygon(C + DOWN * b + RIGHT * (b-a), C + DOWN * a + RIGHT * (b-a), A, color=WHITE, stroke_width=2)
        cube_1 = Polygon(C + DOWN * a, C + DOWN * a + RIGHT * (b-a), C + DOWN * b + RIGHT * (b-a), C + DOWN * b, color=WHITE, stroke_width=2)

        tri_a1 = Polygon(B, C, C + LEFT * a, color=WHITE, stroke_width=2)
        tri_a2 = Polygon(B, B + LEFT * a, C + LEFT * a, color=WHITE, stroke_width=2)

        tri_ab1_2 = Polygon(B + RIGHT * a + UP * (b-a), B + RIGHT * (a + b) + UP * (b-a), B + RIGHT * a + UP * b, color=WHITE, stroke_width=2).set_fill(QING, 1)
        tri_ab2_2 = Polygon(B, A, A + UP * a, color=WHITE, stroke_width=2).set_fill(QING, 1)

        tri_1_2 = Polygon(B, B + (UP + RIGHT) * a, B + RIGHT * a + UP * b, color=WHITE, stroke_width=2).set_fill(QING, 1)
        tri_2_2 = tri_2.copy().shift(RIGHT * a + UP * b).set_fill(QING, 1)
        cube_1_2 = cube_1.copy().shift(RIGHT * a + UP * (a + b)).set_fill(QING, 1)

        tri_a1_2 = tri_a1.copy().shift((UP + RIGHT) * a).set_fill(ZHU, 1)
        tri_a2_2 = tri_a2.copy().shift(UP * (b-a) + RIGHT * (a + b)).set_fill(ZHU, 1)

        self.play(ShowCreation(ABC), FadeIn(cube), run_time=1.)
        self.wait(0.4)
        self.play(ShowCreation(cube_a), run_time=1.)
        self.wait(0.1)
        self.play(ShowCreation(cube_b), run_time=1.)
        self.wait(0.1)
        self.play(ShowCreation(cube_c), run_time=1.)
        self.wait(0.2)

        self.play(ApplyMethod(cube_a.set_fill, ZHU, 0.4), ApplyMethod(cube_b.set_fill, QING, 0.4), ApplyMethod(cube_c.set_fill, PINK, 0.4))
        self.wait(0.2)
        t_a = TextMobject('$a^{2}$', color=ZHU).scale(1.45).move_to(cube_a).set_opacity(0.9)
        t_b = TextMobject('$b^{2}$', color=QING).scale(1.75).move_to(cube_b).set_opacity(0.9)
        t_c = TextMobject('$c^{2}$', color=PINK).scale(2).move_to(cube_c).set_opacity(0.9)

        self.play(Write(t_a))
        self.play(Write(t_b))
        self.play(Write(t_c))

        self.wait(0.8)

        self.play(FadeIn(tri_ab1), FadeIn(tri_ab2), FadeIn(tri_1), FadeIn(tri_2), FadeIn(cube_1))
        self.wait(0.25)

        self.play(FadeIn(tri_a1), FadeIn(tri_a2))
        self.wait(0.25)

        self.play(ApplyMethod(tri_ab1.set_fill, QING, 1),
                  ApplyMethod(tri_ab2.set_fill, QING, 1),
                  ApplyMethod(tri_1.set_fill, QING, 1),
                  ApplyMethod(tri_2.set_fill, QING, 1),
                  ApplyMethod(cube_1.set_fill, QING, 1),
                  ApplyMethod(tri_a1.set_fill, ZHU, 1),
                  ApplyMethod(tri_a2.set_fill, ZHU, 1), run_time=1.25)

        self.wait(1.2)

        c1 = tri_ab1.copy()
        self.play(ReplacementTransform(c1, tri_ab1_2), FadeOut(tri_ab1), run_time=1.25)
        self.wait(0.8)
        c2 = tri_ab2.copy()
        self.play(ReplacementTransform(c2, tri_ab2_2), FadeOut(tri_ab2), run_time=1.25)
        self.wait(0.8)
        c3 = tri_1.copy()
        self.play(ReplacementTransform(c3, tri_1_2), FadeOut(tri_1), run_time=1.25)
        self.wait(0.8)
        c4 = tri_2.copy()
        self.play(ReplacementTransform(c4, tri_2_2), FadeOut(tri_2), run_time=1.25)
        self.wait(0.8)
        c5 = cube_1.copy()
        self.play(ReplacementTransform(c5, cube_1_2), FadeOut(cube_1), run_time=1.25)
        self.wait(0.8)
        c6 = tri_a1.copy()
        self.play(ReplacementTransform(c6, tri_a1_2), FadeOut(tri_a1), run_time=1.25)
        self.wait(0.8)
        c7 = tri_a2.copy()
        self.play(ReplacementTransform(c7, tri_a2_2), FadeOut(tri_a2), run_time=1.25)
        self.wait(1.5)

        text = TextMobject(*['$a^{2}$', '+', '$b^{2}$', '=', '$c^{2}$']).scale(1.8).shift(RIGHT * 2.75)
        text.set_color_by_tex_to_color_map({
            '$a^{2}$': ZHU, '$b^{2}$': QING, '$c^{2}$': PINK,
        })

        self.play(TransformFromCopy(VGroup(cube_a, cube_b), text[0:3]), run_time=1.25)
        self.wait(0.8)
        self.play(Write(text[3]))
        self.wait()
        self.play(TransformFromCopy(VGroup(c1, c2, c3, c4, c5, c6, c7), text[4]), run_time=1.5)

        self.wait(4)
