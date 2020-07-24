from manimlib.imports import *
############################################
# some test before writing Triangles class #
class Test_01(Scene):

    CONFIG = {'camera_config': {
        'background_color': WHITE,
    }}

    def setup(self):
        l = 1
        A, B, C = l/np.sqrt(3) * complex_to_R3(np.exp(1j * 0)) + RIGHT * 0.125, \
                  l/np.sqrt(3) * complex_to_R3(np.exp(2j * PI/3)), \
                  l/np.sqrt(3) * complex_to_R3(np.exp(-2j * PI/3))

        self.vect_x, self.vect_y = A - C, B - C
        self.tri_01 = Polygon(A, B, C, stroke_width=1, fill_opacity=1)
        self.tri_02 = self.tri_01.copy().rotate(PI, about_point=(A+B)/2)

    def construct(self):
        C = 1/np.sqrt(3) * complex_to_R3(np.exp(-2j * PI/3))
        list_1 = [[0, 0], [-1, 1]]
        list_2 = [[-1, 0], [-1, -1]]
        list_3 = [[0, -1], [0, -2]]
        group_1 = self.create_triangles(list_1, '#1955D6').scale(3, about_point=C)
        group_2 = self.create_triangles(list_2, '#4486E8').scale(3, about_point=C)
        group_3 = self.create_triangles(list_3, '#567ADF').scale(3, about_point=C)
        cube = VGroup(group_1, group_2, group_3).shift(UP)
        list_m = [[-2, -1], [-2, 0], [-2, 1], [-2, 2], [-2, 3], [-1, 2], [-1, 1],
                  [0, 0], [0, 1], [1, 0], [1, -1], [1, -2], [1, -3], [1, -4]]
        tex_m = self.create_triangles(list_m, WHITE).shift(UP)
        self.add(cube, tex_m)
        self.wait()

    def create_triangle(self, i, j):
        if j % 2 == 0:
            return self.tri_01.copy().shift(i * self.vect_x + j/2 * self.vect_y)
        else:
            return self.tri_02.copy().shift(i * self.vect_x + (j-1)/2 * self.vect_y)

    def create_triangles(self, list_ij, color=BLUE):
        tri_group = VGroup()
        for i, j in list_ij:
            tri_group.add(self.create_triangle(i, j))
        return tri_group.set_color(color)

##################
# Triangle class #
class Triangles(VGroup):

    CONFIG = {
        'stroke_width': 1,
        'tri_scale': 1, # there's some bugs
        # 'tri_list': [[0, 0]],
    }

    def __init__(self, X, Y, O, **kwargs):

        VGroup.__init__(self, **kwargs)

        self.vect_x, self.vect_y = (X - O) * self.tri_scale, (Y - O) * self.tri_scale
        self.X, self.Y, self.O = O + self.vect_x, O + self.vect_y, O
        self.tri_01 = Polygon(self.X, self.Y, self.O,  stroke_width=self.stroke_width, fill_opacity=1)
        self.tri_02 = self.tri_01.copy().rotate(PI, about_point=(X+Y)/2)

    def create_triangle(self, i, j):
        if j % 2 == 0:
            return self.tri_01.copy().shift(i * self.vect_x + j/2 * self.vect_y)
        else:
            return self.tri_02.copy().shift(i * self.vect_x + (j-1)/2 * self.vect_y)

    def create_triangles(self, list_ij, color=BLUE, scale=1, plot_depth=0):
        tri_group = VGroup()
        for i, j in list_ij:
            tri_group.add(self.create_triangle(i, j))
        tri_group.scale(scale, about_point=self.O).set_color(color)
        self.add(tri_group)
        return tri_group

    def create_list_by_move(self, move_instr, start=[0, 0]):
        list = [start]
        for str in move_instr:

            i, j = list[-1]
            if j % 2 == 0:
                if str == 'Y' or str == 'U':
                    list.append([i, j+1])
                elif str == 'y' or str == 'D':
                    list.append([i, j-1])
                elif str == 'X' or str == 'R':
                    list.append([i, j+1])
                elif str == 'x' or str == 'L':
                    list.append([i-1, j+1])
                else:
                    print('error, invalid move instruction')
            else:
                if str == 'Y' or str == 'U':
                    list.append([i, j+1])
                elif str == 'y' or str == 'D':
                    list.append([i, j-1])
                elif str == 'X' or str == 'R':
                    list.append([i+1, j-1])
                elif str == 'x' or str == 'L':
                    list.append([i, j-1])
                else:
                    print('error, invalid move instruction')

        return list

    def create_triangles_by_move(self, move_instr, start=[0, 0], color=BLUE, scale=1, plot_depth=0):
        list = self.create_list_by_move(move_instr, start=start)
        return self.create_triangles(list, color=color, scale=scale, plot_depth=plot_depth)

    def list_by_move_instruction(self, instruction):
        # '2_3_XYYYXY%-1_2_XYYYXY'
        if instruction == '' or instruction == ' ':
            return []
        list_1 = instruction.split('%')
        list = []
        for l in list_1:
            split_l = l.split('_')
            i, j, move_instr = int(split_l[0]), int(split_l[1]), split_l[2]
            if move_instr != '':
                list += self.create_list_by_move(move_instr, start=[i,j])
            else:
                list.append([i, j])
        return list

    def triangles_by_move_instruction(self, instruction, color=BLUE, scale=1, plot_depth=0):
        list = self.list_by_move_instruction(instruction)
        return self.create_triangles(list, color=color, scale=scale, plot_depth=plot_depth)

##################################
# some test about Triangle class #
class Test_Plot_by_tri(Scene):

    def construct(self):
        l = 0.4
        X, Y, O = l/np.sqrt(3) * complex_to_R3(np.exp(1j * 0)) + RIGHT * 0.15 * l, \
                  l/np.sqrt(3) * complex_to_R3(np.exp(2j * PI/3)), \
                  l/np.sqrt(3) * complex_to_R3(np.exp(-2j * PI/3))


        list_1 = [[0, 0], [-1, 1]]
        list_2 = [[-1, 0], [-1, -1]]
        list_3 = [[0, -1], [0, -2]]
        list_m = [[-2, -1], [-2, 0], [-2, 1], [-2, 2], [-2, 3], [-1, 2], [-1, 1],
                  [0, 0], [0, 1], [1, 0], [1, -1], [1, -2], [1, -3], [1, -4]]
        list_m2 = [[-2, -3], [-2, -2], [-2, -1], [-2, 0], [-2, 1], [-2, 2], [-2, 3], [-1, 2], [-1, 1],
                   [0, 0], [0, 1], [1, 0], [1, -1], [1, -2], [1, -3], [1, -4], [1, -5], [1, -6]]
        tri_m = Triangles(X, Y, O)

        tri_a = Triangles(X, Y, O)
        list_a = tri_a.create_list_by_move('Y' * 6 + 'XYXyX' + 'y' * 6, start=[-2, -3]) +\
                 tri_a.create_list_by_move('yXY', start=[-1, -2])

        tri_n = Triangles(X, Y, O)
        # list_n = tri_a.create_list_by_move('Y' * 4 + 'XyXyX' + 'Y' * 2 + 'y' * 4, start=[-2, -1])
        list_n = tri_n.create_list_by_move('Y' * 6 + 'XyXyX' + 'Y' * 2 + 'y' * 6, start=[-2, -3])

        tri_i = Triangles(X, Y, O)
        # list_n = tri_a.create_list_by_move('Y' * 4 + 'XyXyX' + 'Y' * 2 + 'y' * 4, start=[-2, -1])
        list_i = [[-1, 3], [0, 2]] + tri_i.create_list_by_move('Y' * 3 , start=[-1, -3]) + tri_i.create_list_by_move('Y' * 3, start=[0, -4])


        tri_m.create_triangles(list_1, color='#1955D6', scale=3, plot_depth=-1)
        tri_m.create_triangles(list_2, color='#4486E8', scale=3, plot_depth=-1)
        tri_m.create_triangles(list_3, color='#4579DA', scale=3, plot_depth=-1)
        tri_m.create_triangles(list_m, color=WHITE, scale=1, plot_depth=0)
        tri_m.scale(1.56).shift(LEFT * 4.)

        tri_a.create_triangles(list_a, color=WHITE, scale=1, plot_depth=0).next_to(tri_m, RIGHT, buff=0.6)
        tri_n.create_triangles(list_n, color=WHITE, scale=1, plot_depth=0).next_to(tri_a, RIGHT, buff=0.6)
        tri_i.create_triangles(list_i, color=WHITE, scale=1, plot_depth=0).next_to(tri_n, RIGHT, buff=0.6)
        tri_m2 = Triangles(X, Y, O).create_triangles(list_m2, color=WHITE, scale=1, plot_depth=0).next_to(tri_i, RIGHT, buff=0.6)
        manim = VGroup(tri_m, tri_a, tri_n, tri_i, tri_m2).set_width(12).move_to(ORIGIN)
        self.add(manim)

        self.wait()

class Test_Plot_by_tri_02(Scene):

    def construct(self):

        r = 0.6
        theta = ValueTracker(0)
        X, Y, O = r * complex_to_R3(np.exp(1j * (PI/6 - theta.get_value()))),\
                  r * complex_to_R3(np.exp(1j * (PI/2 - 0 * theta.get_value()))), \
                  ORIGIN

        tri = Triangles(X, Y, O)

        # tri.create_triangles_by_move('Y' * 11 + 'yX' * 4, start=[-3, -5], color=BLUE_B)
        # tri.create_triangles_by_move('Xy' * 5 + 'X' + 'xy' * 4, start=[-3, 7], color=BLUE_D)
        # tri.create_triangles_by_move('y' * 8 + 'X' * 11, start=[-2, 2], color=BLUE_E)
        def update_tri(t):
            X, Y, O = r * complex_to_R3(np.exp(1j * (PI/6 - theta.get_value()))),\
                  r * complex_to_R3(np.exp(1j * (PI/2 - 0 * theta.get_value()))), \
                  ORIGIN
            t_new = Triangles(X, Y, O)
            t_new.create_triangles_by_move('Y' * 15 + 'yX' * 6, start=[-3, -5], color=BLUE_B)
            t_new.create_triangles_by_move('Xy' * 7 + 'X' + 'xy' * 6, start=[-3, 11], color=BLUE_D)
            t_new.create_triangles_by_move('y' * 12 + 'X' * 15, start=[-2, 6], color=BLUE_E)
            t.become(t_new)
        tri.add_updater(update_tri)


        self.add(tri)
        self.wait()
        # self.play(theta.set_value, PI/6, run_time=4)
        # self.wait()

#############################
# from @鹤翔万里 （xgnb!!!） #
class CGNB(Scene):

    def construct(self):

        l = 0.4
        X, Y, O = l/np.sqrt(3) * complex_to_R3(np.exp(1j * 0)) + RIGHT * 0.15 * l, \
                  l/np.sqrt(3) * complex_to_R3(np.exp(2j * PI/3)), \
                  l/np.sqrt(3) * complex_to_R3(np.exp(-2j * PI/3))

        tri_c = Triangles(X, Y, O)
        tri_c.create_triangles_by_move("xyxYxYYYYYYXYXyX", start=[1, -4]).center()
        tri_g = Triangles(X, Y, O)
        tri_g.create_triangles_by_move("XyyxyxYxYYYYYYXYXyX", start=[0, -1]).center()
        tri_n = Triangles(X, Y, O)
        tri_n.create_triangles_by_move("YYYYYYXyXyXYYyyyyyy", start=[-2, -3], color=WHITE).center()
        tri_b = Triangles(X, Y, O)
        tri_b.create_triangles_by_move("XyXyyxyxYxYYYYYYXYXyXyyx", start=[-1, 1], color=WHITE).center()

        cgnb = VGroup(tri_c, tri_g, tri_n, tri_b).arrange(RIGHT, buff=0.6)
        self.add(cgnb)

class Cigar666(Scene):

    def construct(self):
        
        l = 0.4
        X, Y, O = l/np.sqrt(3) * complex_to_R3(np.exp(1j * 0)) + RIGHT * 0.15 * l, \
                  l/np.sqrt(3) * complex_to_R3(np.exp(2j * PI/3)), \
                  l/np.sqrt(3) * complex_to_R3(np.exp(-2j * PI/3))

        tri_c = Triangles(X, Y, O)
        tri_c.create_triangles_by_move("xyxYxYYYYYYXYXyX", start=[1, -4]).center()

        tri_i = Triangles(X, Y, O)
        tri_i.create_triangles_by_move("Y" * 8 + "X" + "y" * 8, start=[-1, -3]).center()

        tri_g = Triangles(X, Y, O)
        tri_g.create_triangles_by_move("XyyxyxYxYYYYYYXYXyX", start=[0, -1]).center()

        tri_a = Triangles(X, Y, O)
        list_a = tri_a.create_list_by_move('Y' * 6 + 'XYXyX' + 'y' * 6, start=[-2, -3]) +\
                 tri_a.create_list_by_move('yXY', start=[-1, -2])
        tri_a.create_triangles(list_a).center()

        tri_r = Triangles(X, Y, O)
        tri_r.create_triangles_by_move("U"*6+"RURDRDDLDLRDRDD", start=[-2, -1]).center()

        tri_6 = Triangles(X, Y, O)
        tri_6.create_triangles_by_move("LULDL"+"D"*6+"RDRURUULULD", start=[1, 2], color=WHITE).center()

        cg666 = VGroup(tri_c, tri_i, tri_g, tri_a, tri_r, tri_6, tri_6.copy(), tri_6.copy()).arrange(RIGHT, buff=0.6).set_width(12)
        self.add(cg666)

#################################
# use Triangles to plot letters #
class Letter(Triangles):

    CONFIG = {
        'letter_dict': {
            'A': '-2_-3_' + 'Y' * 6 + 'XYXyX' + 'y' * 6 + '%' + '-1_-2_' +'yXY',
            # 'a': '0_1_Yxyx' + 'y' * 4 + 'XyXY' + '%' + '1_1_' + 'y' * 6 + 'X',
            'a': '0_1_Yxyx' + 'y' * 4 + 'XyXY' + '%' + '1_0_' + 'y' * 5,
            'i': '-1_3_%0_2_%' + '-1_-3_YYY' + '%' + '0_-4_YYY',
            'N': '-2_-3_' + 'Y' * 6 + 'XyXyX' + 'Y' * 2 + 'y' * 6,
            'n': '-2_-1_' + 'Y' * 4 + 'XyXyX' + 'Y' * 2 + 'y' * 4,
            'M': '-2_-3_' + 'Y' * 6 + 'XyXYX' + 'y' * 6,
            'm': '-2_-1_' + 'Y' * 4 + 'XyXYX' + 'y' * 4,
            'Z': '0_0_YYxyxy%-1_-1_yyXYXY',
            'S': '-1_0_xYYXYXY%0_-1_Xyyxyxy',
            's': '-1_0_xYYXYX%0_-1_Xyyxyx',
            'b': '-2_5_' + 'y' * 6 + 'XyXYXYYYYxYxy',
            'd': '1_2_' + 'y' * 6 + 'xyxYxYYYYXYXy',
            'o': '1_0_xYxyxyyyyXyXYXYYY',
            'x': '1_0_xyxYx%-2_-1_XYXyX',
            ' ': '',
        },
        # TODO add other letters
        'bg_color': ['#1955D6', '#498AED', '#4573D8'],
        'add_bg': False,
    }

    def __init__(self, X, Y, O, char, **kwargs):
        Triangles.__init__(self, X, Y, O, **kwargs)
        if self.add_bg:
            self.create_triangles([[0, 0], [-1, 1]], color=self.bg_color[0], scale=3)
            self.create_triangles([[-1, 0], [-1, -1]], color=self.bg_color[1], scale=3)
            self.create_triangles([[0, -1], [0, -2]], color=self.bg_color[2], scale=3)

        self.triangles_by_move_instruction(self.letter_dict[char], color=WHITE, scale=1)

class TexByTri(VGroup):

    def __init__(self, X, Y, O, tex='manim', add_bg='10000', **kwargs):
        VGroup.__init__(self, **kwargs)
        for char, s in zip(tex, add_bg):
            self.add(Letter(X, Y, O, char, add_bg=bool(int(s))))
        self.arrange(RIGHT)

class Test_letters(Scene):

    def construct(self):

        r = 0.6
        X, Y, O = r * complex_to_R3(np.exp(1j * PI/6)), r * complex_to_R3(np.exp(1j * PI/2 )), ORIGIN

        # m0 = Letter(X, Y, O, 'm', add_bg=True)
        # a = Letter(X, Y, O, 'a', add_bg=True)
        # n = Letter(X, Y, O, 'n', add_bg=True)
        # i = Letter(X, Y, O, 'i', add_bg=True)
        # m = Letter(X, Y, O, 'm', add_bg=True)
        # anim = VGroup(a, n, i, m).arrange(RIGHT, buff=0, aligned_edge=DOWN).next_to(m0, RIGHT, buff=0)
        # manim = VGroup(m0, *anim).set_width(10).move_to(ORIGIN)

        manim = TexByTri(X, Y, O, 'manim', add_bg='11111').set_width(11).shift(UP * 1.5)
        manim_2 = TexByTri(X, Y, O, 'mAnim', add_bg='00000').arrange(RIGHT, aligned_edge=DOWN).shift(DOWN * 1.5)

        self.add(manim, manim_2)
        self.wait()

class Manim_Sandbox(Scene):

    def construct(self):

        r = 0.25
        X, Y, O = r * complex_to_R3(np.exp(1j * PI/6)), r * complex_to_R3(np.exp(1j * PI/2 )), ORIGIN

        # boxes_01 = TexByTri(X, Y, O, '    ', add_bg='1111').arrange(RIGHT, buff=0)
        # manim = TexByTri(X, Y, O, 'manim', add_bg='11111').arrange(RIGHT, buff=0)
        # sand = TexByTri(X, Y, O, ' sand ', add_bg='111111').arrange(RIGHT, buff=0)
        # box = TexByTri(X, Y, O, ' box ', add_bg='11111').arrange(RIGHT, buff=0)
        # boxes_02 = TexByTri(X, Y, O, '    ', add_bg='1111').arrange(RIGHT, buff=0)
        # manim_sandbox = VGroup(boxes_01, manim, sand, box, boxes_02).arrange(DOWN, buff=0)
        # manim.shift(-Y * 1.5), box.shift(Y * 1.5), boxes_01.shift(-Y * 3), boxes_02.shift(Y * 3),

        # boxes_01 = TexByTri(X, Y, O, '    ', add_bg='1111').arrange(RIGHT, buff=0.5)
        # manim = TexByTri(X, Y, O, 'manim', add_bg='11111').arrange(RIGHT, buff=0.5)
        # sand = TexByTri(X, Y, O, ' sand ', add_bg='111111').arrange(RIGHT, buff=0.5)
        # box = TexByTri(X, Y, O, ' box ', add_bg='11111').arrange(RIGHT, buff=0.5)
        # boxes_02 = TexByTri(X, Y, O, '    ', add_bg='1111').arrange(RIGHT, buff=0.5)
        # manim_sandbox = VGroup(boxes_01, manim, sand, box, boxes_02).arrange(DOWN, buff=0)


        manim = TexByTri(X, Y, O, 'manim', add_bg='00000')
        manim[0].scale(1.25), manim[1].scale(0.82)
        manim.arrange(RIGHT, buff=0.5, aligned_edge=DOWN)
        sandbox = TexByTri(X, Y, O, 'Sandbox', add_bg='0000000')
        sandbox[1].scale(0.82), sandbox[3:6].scale(0.86)
        sandbox.arrange(RIGHT, buff=0.5, aligned_edge=DOWN)
        # box = TexByTri(X, Y, O, ' box ', add_bg='11111').arrange(RIGHT, buff=0.5)
        manim_sandbox = VGroup(manim, sandbox).arrange(DOWN, buff=0.5)

        self.add(manim_sandbox)
        self.wait()

# to plot some weird shape

class Cube_by_tri(Triangles):
    CONFIG = {
        'colors': ['#498AED', '#1955D6', '#4573D8'],
        'stroke_width': 1.6,
    }
    def __init__(self, X=UP * 0.5 + RIGHT * np.sqrt(3)/2, Y=UP, O=ORIGIN, scale_factor=1, **kwargs):
        self.X, self.Y, self.O= O + (X - O) * scale_factor, O + (Y - O) * scale_factor, O
        Triangles.__init__(self, self.X, self.Y, self.O, **kwargs)
        self.top = self.create_triangles([[0, 0], [-1,1]], color=self.colors[0])
        self.front = self.create_triangles([[-1, 0], [-1,-1]], color=self.colors[2])
        self.right = self.create_triangles([[0, -1], [0,-2]], color=self.colors[1])


        self.vect_up, self.vect_down = self.Y, -self.Y
        self.vect_front, self.vect_back = -self.X, self.X
        self.vect_right, self.vect_left = self.X - self.Y, self.Y - self.X
        self.move_dict = {'u': self.vect_up, 'd': self.vect_down, 'f': self.vect_front,
                          'b': self.vect_back, 'r': self.vect_right, 'l': self.vect_left}

    def move(self, instruction, leave_copy=False):

        # u: up, d: down, f: front, b: back, r: right, l: left

        copy = VGroup(self.copy())

        for s in instruction:
            v = self.move_dict[s]
            self.shift(v)
            if leave_copy:
                copy.add(self.copy())

        if not leave_copy:
            return self
        else:
            return copy

    def move_and_keep_copy(self, instruction):
        return self.move(instruction, leave_copy=True)

    def remove_faces(self, list):
        for i in range(3):
            if list[i] < 0:
                pass
            elif list[i] != 2:
                self[i].remove(self[i][list[i]])
            else:
                self[i].remove(self[i][0])
                self[i].remove(self[i][0])

class Test_Cube(Scene):

    def construct(self):

        cube = Cube_by_tri(scale_factor=0.8)
        cube[-1].set_stroke(width=0.8)
        cube.move('uull')
        cubes = cube.move_and_keep_copy('r' * 6 + 'f' * 6 + 'u' * 5)

        # all_faces = VGroup()
        # for c in cubes:
        #     all_faces.add(c[0], c[1], c[2])
        #     # all_faces.add(*c)
        # all_faces[0].set_plot_depth(2), all_faces[1].set_plot_depth(2), all_faces[3].set_plot_depth(2), all_faces[4].set_plot_depth(2)
        # self.add(*all_faces)

        self.add(cubes[0])
        self.wait(0.6)
        self.play(WiggleOutThenIn(cubes[0]))
        self.wait()
        for i in range(16):
            self.play(TransformFromCopy(cubes[i], cubes[i+1]), rate_func=linear, run_time=0.2 + np.sqrt(i) * 0.1)
        new_face = VGroup(cubes[0][0:2], cubes[1][0:2]).set_plot_depth(2).set_stroke(width=0.9)
        self.add(new_face)
        cubes[-1].move('d')
        self.play(cubes[-1].move, 'u', rate_func=linear, run_time=0.6)
        self.wait(0.8)
        self.play(cubes[-1].move, 'ff', rate_func=there_and_back, run_time=1.8)
        self.wait(2)

class Impossible_Shape(Scene):

    def construct(self):

        cube = Cube_by_tri(scale_factor=0.46)
        cube[1].set_stroke(width=1.25)
        cube[-1].set_stroke(width=1)
        cube.move('uull')
        cubes = cube.move_and_keep_copy('r' * 6 + 'f' * 6 + 'u' * 5).set_plot_depth(1)
        cube.move('llb')

        new_face = VGroup(cubes[0][0:2].copy(), cubes[1][0:2].copy(), cubes[2][0:2].copy(), cubes[3][0:2].copy()).set_plot_depth(2).set_stroke(width=1.25)
        cubes_02 = cube.move_and_keep_copy('f' * 7 + 'r' * 15 + 'u' * 15 + 'f' * 7).set_plot_depth(-1)
        new_face_02 = cubes_02[0][0].copy().set_plot_depth(2).set_stroke(width=1.1)
        new_face_03 = VGroup(cubes[12][1].copy(), cubes[12][2].copy()).set_plot_depth(2).set_stroke(width=1.45)
        new_face_04 = VGroup(cubes[6][0].copy(), cubes[6][-1].copy()).set_plot_depth(2).set_stroke(width=1.54)

        small_tri = VGroup(cubes, new_face, new_face_03, new_face_04)
        big_tri = VGroup(cubes_02, new_face_02)
        ##############
        # test shape #
        # self.add(cubes)
        # self.add(new_face)
        # self.wait()
        #
        # self.add(cubes_02)
        # self.add(new_face_02)
        # self.add(cubes[0])
        ##############
        self.add(cubes[0])
        self.wait(0.8)
        self.play(WiggleOutThenIn(cubes[0]), scale_value=1.2)
        self.wait(0.9)
        for i in range(16):
            self.play(TransformFromCopy(cubes[i], cubes[i+1]), rate_func=linear, run_time=0.18 + np.sqrt(i) * 0.05)

        self.add(new_face)
        cubes[-1].move('d')
        self.play(cubes[-1].move, 'u', rate_func=linear, run_time=0.5)
        self.wait(0.8)
        # self.play(cubes[-1].move, 'ffff',
        #           cubes[-2].move, 'fff',
        #           cubes[-3].move, 'ff',
        #           cubes[-4].move, 'f',
        #           rate_func=there_and_back_with_pause, run_time=2.7)
        self.play(cubes[-1].shift, cube.vect_front * 0.6 * 5,
                  cubes[-2].shift, cube.vect_front * 0.6 * 4,
                  cubes[-3].shift, cube.vect_front * 0.6 * 3,
                  cubes[-4].shift, cube.vect_front * 0.6 * 2,
                  cubes[-5].shift, cube.vect_front * 0.6,
                  rate_func=there_and_back_with_pause, run_time=2.7)
        self.wait(1.2)
        self.play(cubes[-1].shift, -cube.vect_front * 0.6 * 5,
                  cubes[-2].shift, -cube.vect_front * 0.6 * 4,
                  cubes[-3].shift, -cube.vect_front * 0.6 * 3,
                  cubes[-4].shift, -cube.vect_front * 0.6 * 2,
                  cubes[-5].shift, -cube.vect_front * 0.6,
                  rate_func=there_and_back_with_pause, run_time=2.7)
        self.wait(1.2)
        self.play(cubes[-1].shift, cube.vect_left * 0.6 * 5,
                  cubes[-2].shift, cube.vect_left * 0.6 * 4,
                  cubes[-3].shift, cube.vect_left * 0.6 * 3,
                  cubes[-4].shift, cube.vect_left * 0.6 * 2,
                  cubes[-5].shift, cube.vect_left * 0.6,
                  rate_func=there_and_back_with_pause, run_time=2.7)

        self.wait(2.)

        self.play(TransformFromCopy(cubes[0], cubes_02[0]), rate_func=linear, run_time=0.6)

        for i in range(len(cubes_02)-2):

            if i == 13:
                self.play(TransformFromCopy(cubes_02[i], cubes_02[i+1], rate_func=linear), FadeIn(new_face_03, rate_func=lambda t:1), run_time=0.2 + np.sqrt(i) * 0.025)
            elif i == 28:
                self.play(TransformFromCopy(cubes_02[i], cubes_02[i+1], rate_func=linear), FadeIn(new_face_04, rate_func=lambda t:1), run_time=0.2 + np.sqrt(i) * 0.025)
            else:
                self.play(TransformFromCopy(cubes_02[i], cubes_02[i+1]), rate_func=linear, run_time=0.2 + np.sqrt(i) * 0.025)

        self.add(new_face_02)
        cubes_02[-1].move('b')
        self.play(cubes_02[-1].move, 'f', rate_func=linear, run_time=0.6)
        # self.wait(0.8)
        #
        # self.play(big_tri.shift, LEFT * 2, small_tri.shift, RIGHT * 3, run_time=1.2)
        self.wait(4.5)

class Impossible_Shape_02(Scene):

    def construct(self):

        cube = Cube_by_tri(scale_factor=0.6)
        cube[1].set_stroke(width=1.4)
        cube[-1].set_stroke(width=1.2)

        n = 5
        cubes = cube.move_and_keep_copy('r' * n + 'u' * n + 'f' * n + 'u' * n + 'r' * (n-1))
        new_face = VGroup(cubes[1][0].copy(), cubes[1][1].copy())#.set_plot_depth(1)
        # new_face_02 = VGroup(cubes[2 * n + 1][0].copy(), cubes[2 * n + 1][2].copy())#.set_plot_depth(1)
        cubes[-1].remove_faces([-1, 1, 2])
        # cubes[-1].remove_faces([-1, 1, 2])

        cube.move('r' + 'f' * (n+1))
        cubes_1 = cube.move_and_keep_copy('f' * (n-1) + 'u' * n + 'r' * (n-1))
        cubes_1[-1].remove_faces([0, 1, 2])

        cube.move('r' + 'f' * n + 'r')
        cubes_2 = cube.move_and_keep_copy('r' * (n-1) + 'u' * (n-1))
        cubes_2[-1].remove_faces([2, 0, 0])

        cube.move('d' * (n-1) + 'b' * (n-1))
        cubes_3 = cube.move_and_keep_copy('f' * (n-2))
        cubes_3[-1].remove_faces([1, 2, -1])

        cube.move('f' + 'u' * 2 * n + 'f')
        cubes_4 = cube.move_and_keep_copy('f' * (n-2))
        cubes_4[-1].remove_faces([-1, 2, 1])


        self.add(cubes, new_face, cubes_1, cubes_2, cubes_3, cubes_4)

        self.wait(4.)

