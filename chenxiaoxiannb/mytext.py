# from chenxiaoxian
from manimlib.imports import *


class ShowIncreasingSubsetsExample(Scene):
    def construct(self):
        text = TextMobject("ShowIncreasingSubsets")
        text.set_width(11)
        print(text)
        self.wait()
        self.play(ShowIncreasingSubsets(text[0], run_time=4))
        self.wait()


class textA(Scene):
    def construct(self):
        t1 = TextMobject('大', '家', '好')

        t2 = TexMobject("x", 'y', 'z')
        for i, item in enumerate(t2):
            item.align_to(t1[i], LEFT)
        t2.shift(DOWN)

        self.play(Write(t1))
        self.wait(2)
        self.play(Write(t2))


class UsingBraces(Scene):
    # Using braces to group text together
    def construct(self):
        eq1A = TextMobject("4x + 3y")
        eq1B = TextMobject("=")
        eq1C = TextMobject("0")
        eq2A = TextMobject("5x - 2y")
        eq2B = TextMobject("=")
        eq2C = TextMobject("3")
        eq1B.next_to(eq1A, RIGHT)
        eq1C.next_to(eq1B, RIGHT)
        eq2A.shift(DOWN)
        eq2B.shift(DOWN)
        eq2C.shift(DOWN)
        eq2A.align_to(eq1A, LEFT)
        eq2B.align_to(eq1B, LEFT)
        eq2C.align_to(eq1C, LEFT)

        eq_group = VGroup(eq1A, eq2A)
        braces = Brace(eq_group, LEFT)
        eq_text = braces.get_text("A pair of equations")

        self.add(eq1A, eq1B, eq1C)
        self.add(eq2A, eq2B, eq2C)
        self.play(GrowFromCenter(braces), Write(eq_text))


class UsingBraces1(Scene):
    # Using braces to group text together;Using TexMobject
    def construct(self):
        eq1A = TexMobject("4x + 3y")
        eq1B = TextMobject("=")
        eq1C = TextMobject("0")
        eq2A = TexMobject("5x - 2y")
        eq2B = TextMobject("=")
        eq2C = TextMobject("3")
        eq1B.next_to(eq1A, RIGHT)
        eq1C.next_to(eq1B, RIGHT)
        eq2A.shift(DOWN)
        eq2B.shift(DOWN)
        eq2C.shift(DOWN)
        eq2A.align_to(eq1A, LEFT)
        eq2B.align_to(eq1B, LEFT)
        eq2C.align_to(eq1C, LEFT)

        eq_group = VGroup(eq1A, eq2A)
        braces = Brace(eq_group, LEFT)
        eq_text = braces.get_text("A pair of equations")

        self.add(eq1A, eq1B, eq1C)
        self.add(eq2A, eq2B, eq2C)
        self.play(GrowFromCenter(braces), Write(eq_text))


class UsingBraces2(Scene):
    # Using braces to group text together
    def construct(self):
        eq1A = TexMobject("4x + 3y")
        eq1B = TextMobject("=")
        eq1C = TextMobject("0")
        eq2A = TextMobject("$$5x - 2y$$")
        eq2B = TextMobject("=")
        eq2C = TextMobject("3")
        eq1B.next_to(eq1A, RIGHT)
        eq1C.next_to(eq1B, RIGHT)
        eq2A.shift(DOWN)
        eq2B.shift(DOWN)
        eq2C.shift(DOWN)
        eq2A.align_to(eq1A, LEFT)
        eq2B.align_to(eq1B, LEFT)
        eq2C.align_to(eq1C, LEFT)

        eq_group = VGroup(eq1A, eq2A)
        braces = Brace(eq_group, LEFT)
        eq_text = braces.get_text("A pair of equations")

        self.add(eq1A, eq1B, eq1C)
        self.add(eq2A, eq2B, eq2C)
        self.play(GrowFromCenter(braces), Write(eq_text))


class MyAlign(Scene):
    def construct(self):
        title = TextMobject("This is some \\LaTeX")
        basel = TexMobject(
            r"& \phantom{=}(a+b)(a^2-ab+b^2) \\& = a^3-a^2b+ab^2 + a^2b-ab^2+b^3 \\& = a^3+b^3"
        )
        VGroup(title, basel).arrange(DOWN)
        self.play(
            Write(title),
            FadeInFrom(basel, UP),
        )
        self.wait()


class MyCase(Scene):
    def construct(self):
        title = TextMobject("This is some \\LaTeX")
        basel = TexMobject(
            r"y = \begin{cases} -x, &x\leqslant 0 \\x, &x>0\end{cases}"
            "\\frac{1}{n^2} = \\frac{\\pi^2}{6}"
            "\\\\"
            "\\boxed{E = mc^2} "
        )
        VGroup(title, basel).arrange(DOWN)
        self.play(
            Write(title),
            FadeInFrom(basel, UP),
        )
        self.wait()
#            , r"\\A. 3\\B. 6\\C. 8\\D.10"

class MyExam(Scene):
    def construct(self):
        basel = TextMobject(
            '''\\begin{flushleft}1. 已知集合 $A=\\{1,2,3,4,5\\}, B=\\{(x, y) \\mid x \\in A, y \\in A, x-y \\in A\\},$ 则 $B$
             中所含元素的个数为\\end{flushleft}''',
            r"\begin{tasks}(2)\task $3$\task $6$\task $8$\task $10$\end{tasks}"
        ).set_width(10).to_edge(UL)
        self.play(
            Write(basel),
        )
        self.wait()

class MyExam1(Scene):
    def construct(self):
        basel = TextMobject(r"\begin{tasks}[label=(\Alph*)](2)\task $f(x)$\task $g(x)$\task $h(x)$\task $\varphi(x)$\end{tasks}")
        self.play(
            Write(basel),
        )
        self.wait()

class MyExam3(Scene):
    def construct(self):
        basel = TextMobject("{\LARGE 借款还款计划客户空间和空间好看回来很厉害两节课换行理论和就会加快理论结合厉害厉害厉害健康和黑龙江回家了回来很快就会客家话健康和进口红酒看好了和厉害厉害和厉害了和}")
        basel = basel.set_width(8)
        self.play(
            Write(basel),
        )
        self.wait()


class MyBHCExam(Scene):
    def construct(self):
        basel = TextMobject(r"\begin{questions}[sp]\begin{minipage}{\linewidth}\question[5] 若 $z=1+\mathrm i,$ 则 ${|z^{2}-2z|=}$ \key{D} . \fourchoices{ $0$ }{ $1$ }{ $\sqrt{2}$ }{ $2\end{minipage}\end{questions}")
        self.play(
            Write(basel),
        )
        self.wait()

class Graph2D(GraphScene):
    CONFIG = {"x_min": -10, "x_max": 10, "x_axis_width": 18, "x_tick_frequency": 1,
              "x_leftmost_tick": None,
              # Change if different from x_min
              "x_labeled_nums": None, "x_axis_label": "$x$", "y_min": -1, "y_max": 10, "y_axis_height": 6,
              "y_tick_frequency": 1, "y_bottom_tick": None,
              # Change if different from y_min
              "y_labeled_nums": None, "y_axis_label": "$y$", "axes_color": GREY, "graph_origin": ORIGIN,
              "exclude_zero_label": True, "default_graph_colors": [BLUE, GREEN, YELLOW],
              "default_derivative_color": GREEN, "default_input_color": YELLOW, "default_riemann_start_color": BLUE,
              "default_riemann_end_color": GREEN, "area_opacity": 0.8, "num_rects": 50, }

    def x_2(self, x):
        return x ** 2

    def construct(self):
        self.setup_axes(animate=True)
        graph = self.get_graph(self.x_2, color=GREEN, x_min=-4, x_max=4)
        self.play(ShowCreation(graph), run_time=2)
        self.wait()


class ChangeColorAndSizeAnimation(Scene):
	def construct(self):
         text = TextMobject("Texxxt")
         self.play(Write(text))

         text.generate_target()
         text.target = TextMobject("Texxt")
         text.target.set_color(RED)
         text.target.scale(2)
         text.target.shift(LEFT)

         self.play(MoveToTarget(text),run_time = 2)
         self.wait()


class Updater(Scene):
    def construct(self):
        dot = Dot()
        text = TextMobject("Label")

        #self.add(dot,text)

        def update_text(obj):
            obj.next_to(dot,RIGHT,buff=SMALL_BUFF+2)

        # Only works in play
        self.play(
                dot.shift,UP*2,
                UpdateFromFunc(text,update_text),
                rate_func=smooth,  # Change this with: linear,smooth
                run_time=2
            )

        self.wait()


class AddUpdater1(Scene):
    def construct(self):
        dot = Dot()
        text = TextMobject("Label") \
            .next_to(dot, RIGHT, buff=SMALL_BUFF)

        self.add(dot, text)

        # Update function 更新函数
        def update_text(obj):
            obj.next_to(dot, RIGHT, buff=SMALL_BUFF)

        # Add update function to the objects
        # 把更新函数加给对象
        text.add_updater(update_text)

        # 如果想简洁，lambda表达式如下：
        # text.add_updater(lambda m: m.next_to(dot,RIGHT,buff=SMALL_BUFF))
        # 此时下面的remove_updater(update_text)不能继续使用，需要改为clear_updaters

        # Add the object again 重新加入text
        # 注意这个步骤不能少，否则看不到！！！
        # 即使之前加入过，现在还是要重新加入
        self.add(text)

        self.play(dot.shift, UP * 2)

        # Remove update function
        text.remove_updater(update_text)

        self.wait()