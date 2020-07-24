from manimlib.imports import *

class Programing_process(Scene):

    def construct(self):

        s = 0.25
        to_corner_loc = LEFT * 2 + UP * 0.1
        MAGENTA = '#6A6CCB'

        bg_rect = Rectangle(fill_color=DARK_GRAY, fill_opacity=0.275).scale(20)
        self.add(bg_rect)
        text_import = Text('import numpy as np\nimport matplotlib.pyplot as plt',
                           font='Consolas').scale(s).to_corner(to_corner_loc)
        text_import.set_color_by_t2c({'import':ORANGE, 'as': ORANGE})

        t0 = Text('import', font='Consolas').scale(s)
        h = text_import.get_height() - t0.get_height()
        w = t0.get_width()/len(t0)
        text_func = Text('iter_func = lambda z, c: (z ** 2 + c) # iteration function', font='Consolas').scale(s).to_corner(to_corner_loc).shift(DOWN * 3 * h)
        text_func.set_color_by_t2c({'lambda': ORANGE, '2': BLUE, '# iteration function': GRAY, ',': ORANGE})

        text_setvalue_01 = Text('def set_value(c, max_iter_num=128):', font='Consolas').scale(s).to_corner(to_corner_loc).shift(DOWN * 5 * h)
        text_setvalue_01.set_color_by_t2c({'def': ORANGE, 'set_value': GOLD_C, '128': BLUE, ',': ORANGE})
        text_setvalue_02 = Text('    z = complex(0, 0) # initial value of z\n'
                                '    num = 0\n'
                                '    while abs(z) < 2 and num < max_iter_num:\n'
                                '        z = iter_func(z, c)\n'
                                '        num += 1\n'
                                '    return num', font='Consolas')\
            .scale(s).to_corner(to_corner_loc).shift(DOWN * 6 * h + 4 * w * RIGHT)

        text_setvalue_02.set_color_by_t2c({'complex': MAGENTA, '0': BLUE, '# initial value of z': GRAY, 'abs':MAGENTA,
                                           'while': ORANGE, 'and': ORANGE, '1': BLUE, '2': BLUE, 'return': ORANGE})
        text_setvalue = VGroup(text_setvalue_01, text_setvalue_02)

        text_showfunc_01 = Text('def display_mandelbrot(x_num=1000, y_num=1000):', font='Consolas')\
            .scale(s).to_corner(to_corner_loc).shift(DOWN * 13 * h)
        text_showfunc_01.set_color_by_t2c({'def': ORANGE, 'display_mandelbrot': GOLD_C, '1': BLUE, '0':BLUE, ',': ORANGE})

        text_showfunc_02 = Text('    X, Y = np.meshgrid(np.linspace(-2, 2, x_num+1), np.linspace(-2, 2, y_num+1))\n'
                                '    C = X + Y * 1j\n'
                                '    result = np.zeros((y_num+1, x_num+1))', font='Consolas')\
            .scale(s).to_corner(to_corner_loc).shift(DOWN * 15 * h + 4 * w * RIGHT)
        text_showfunc_02.set_color_by_t2c({'1': BLUE, '2':BLUE, 'j': BLUE, ',': ORANGE})
        text_showfunc_03 = Text('    for i in range(y_num+1):\n'
                                '        for j in range(x_num+1):\n'
                                '            result[i, j] = set_value(C[i, j])', font='Consolas')\
            .scale(s).to_corner(to_corner_loc).shift(DOWN * 19 * h + 4 * w * RIGHT)

        text_showfunc_03.set_color_by_t2c({'for': ORANGE, 'in': ORANGE, 'range': MAGENTA, '1': BLUE, ',': ORANGE})

        text_showfunc_04 = Text('plt.imshow(result, interpolation="bilinear", cmap=plt.cm.hot,\n'
                                '           vmax=abs(result).max(), vmin=abs(result).min(),\n'
                                '           extent=[-2, 2, -2, 2])\n'
                                'plt.show()', font='Consolas')\
            .scale(s).to_corner(to_corner_loc).shift(DOWN * 23 * h + 4 * w * RIGHT)
        text_showfunc_04.set_color_by_t2c({'interpolation':RED, '"bilinear"': GREEN_D, 'cmap': RED,
                                           'vmax':RED, 'vmin':RED, 'extent':RED, 'abs': MAGENTA, ',': ORANGE})

        text_showfunc = VGroup(text_showfunc_01, text_showfunc_02, text_showfunc_03, text_showfunc_04)

        text_main = Text('if __name__ == "__main__":\n'
                         '    \n'
                         # '    iter_num = 200 # maximum iteration num\n'
                         '    display_mandelbrot(2000, 2000)', font='Consolas')\
            .scale(s).to_corner(to_corner_loc).shift(DOWN * 28 * h)
        text_main.set_color_by_t2c({'if': ORANGE, '"__main__"': GREEN_D, '2': BLUE, '0': BLUE,
                                    '# maximum iteration num': GRAY, ',': ORANGE})
        separate_line = Line(UP * 10, DOWN * 10, color=GRAY, stroke_width=1).to_corner(to_corner_loc * RIGHT).shift(w * LEFT)
        line_num = VGroup()
        for i in range(50):
            tex_i = Text(str(i), color=GRAY, font='Consolas').scale(s).shift(DOWN * h * i).scale(0.8)
            if i > 9:
                tex_i.shift(LEFT * w/2)
            line_num.add(tex_i)
        line_num.next_to(separate_line, LEFT * 1.5).to_corner(to_corner_loc * UP).shift(DOWN * h * 0.1).to_corner(LEFT * 0.2)

        rect_gray = Rectangle(stroke_width=0, fill_color=GRAY, fill_opacity=0.15, height=10, width=3).align_to(separate_line, RIGHT)

        self.add(separate_line, rect_gray)
        self.play(Write(line_num))
        self.wait()

        dt = 0.01
        self.play(Write(text_import), run_time=len(text_import)*dt)
        self.wait()
        self.play(Write(text_func), run_time=len(text_func)*dt)
        self.wait()
        self.play(Write(text_setvalue), run_time=(len(text_setvalue_01)+len(text_setvalue_02))*dt)
        self.wait()
        self.play(Write(text_showfunc), run_time=(len(text_showfunc_01)+len(text_showfunc_02)+len(text_showfunc_03)+len(text_showfunc_04))*dt)
        self.wait()
        self.play(Write(text_main), run_time=len(text_main)*dt)
        self.wait(4)
