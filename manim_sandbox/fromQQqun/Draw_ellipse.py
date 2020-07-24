from manimlib.imports import *

class Draw_Ellipse(Scene):

    def construct(self):

        s = 0.8 # scale_factor
        F1 = LEFT * 4 * s
        F2 = RIGHT * 4* s
        P = UP * 3 * s

        dot_F1 = Dot(F1, color=RED).scale(1.5)
        dot_F2 = Dot(F2, color=RED).scale(1.5)
        dot_P = Dot(P, color=PINK).scale(1.5)

        F1P = Line(F1, P, color=BLUE)
        F2P = Line(F2, P, color=BLUE)

        text_F1 = TexMobject('F_{1}', color=RED).next_to(F1, DOWN * 0.8)
        text_F2 = TexMobject('F_{2}', color=RED).next_to(F2, DOWN * 0.8)

        ellipse = VGroup()

        self.add(text_F1, text_F2, F1P, F2P, ellipse, dot_F1, dot_F2, dot_P)
        self.wait()


        dot_P.add_updater(lambda d: d.move_to(P))
        F1P.add_updater(lambda l: l.put_start_and_end_on(F1, P))
        F2P.add_updater(lambda l: l.put_start_and_end_on(F2, P))

        d_theta = TAU / 360 * 3
        dt=1/30
        p_old = dot_P.get_center()

        for i in range(120 + 60):
            P = (5 * RIGHT * np.cos(d_theta * i + PI/2) + 3 * UP * np.sin(d_theta * i + PI/2)) * s
            p_new = dot_P.get_center()
            ellipse.add(Line(p_old, p_new, stroke_width=3, color=PINK))
            self.wait(dt)
            p_old = p_new

        self.wait(2)
