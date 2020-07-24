from manimlib.imports import *
import math

'''
更新日志：
2020/2/12/18:19:43, V1.2:
    1.新增数学工具right_to_polar(第78行), polar_to_right(第84行)
    2.新增VGroup对象MyRightAngle(第372行),(事实上，是个Polygon)
2020/2/12/12:41:20, V1.1:
    1.优化了数学工具arg_angle, get_len
    2.新增数学工具get_angle
    3.从MathTools.py把函数,类都搬到了这里并进行优化
    4.新增友好的注释~
'''
'''
使用说明：
    本模块需导入manimlib.imports里的所有模块和包,若无导入,请使用语句:  from manimlib.imports import *
    本模块需导入math标准数学库,若无导入,请使用语句:     import math
    本模块分为“数学工具”,“自定义对象”,“VGroup对象”和“实验区”:
        数学工具:    为了适应本模块的使用,自定义了许多数学函数(尽管numpy,math有这类的函数但是我不知道哈哈哈)
                    如果其他库有 能帮助于此模块计算、运行的函数,可联系作者。
        自定义对象:   可以帮助研究计算(比如MyTriangle直接构造三角形以获取其三心坐标、周长、面积、三个角度等信息)
        VGroup对象:  由于我读不懂Grant的代码,不敢乱继承父类和调用父类的方法,所以自己整了个VGroup对象啦。
                     颜色、不透明度等属性可自行添加代码噢~
        试验区:       可以临时建立场景,查看效果。
    如有Bug,请联系作者。

    作者: 我是害羞的向量
    作者QQ: 1950473706
    manim交流群: 862671480
    數學（迫真）交流群: 726542042
'''

#数学工具
def arg_angle(start, end):
    #求射线辐角     start:顶点的np坐标  end:射线方向点的np坐标
    start_x, start_y, end_x, end_y = start[0], start[1], end[0], end[1]
    mode = 1    #以start为坐标系原点，判断象限
    if start_x < end_x and start_y < end_y:     mode = 1
    elif start_x > end_x and start_y < end_y:   mode = 2
    elif start_x > end_x and start_y > end_y:   mode = 3
    elif start_x < end_x and start_y > end_y:   mode = 4
    elif start_y == end_y and start_x < end_x:    mode = 5  #x正半轴
    elif start_x == end_x and start_y < end_y:    mode = 6  #y正半轴
    elif start_y == end_y and start_x > end_x:    mode = 7  #x负半轴
    elif start_x == end_x and start_y > end_y:    mode = 8  #y负半轴

    if (not mode == 6) and (not mode == 8):   #防止斜率不存在
        delta_x = end_x - start_x
        delta_y = end_y - start_y
        theta = math.atan(delta_y / delta_x)
    elif mode == 6: theta = PI / 2  #落在y正半轴
    elif mode == 8: theta = 3 * PI / 2  #落在y负半轴
    
    #math.atan()只会返回(pi/2, -pi/2),所以这里需要调整角的度数
    if mode == 2:   theta += PI
    elif mode == 3: theta += PI
    elif mode == 4: theta += 2 * PI
    elif mode == 5: theta = 0
    elif mode == 7: theta = PI

    return theta

def get_len(P1, P2):
    #返回两点之间的距离     P1,P2:两个点的np坐标
    P = P1 - P2 #为了方便，把问题转换成求向量P_1P_2模长
    return np.sqrt(np.sum(P ** 2))

def get_angle(A, O, B, major_arc = False):
    #返回∠AOB的大小，默认A,O,B为逆时针顺序(即OA为终边，OB为始边)
    #A,O,B:“终”点, 顶点, “始”点 的np坐标
    #major_arc:是否为优弧(即默认为劣弧)
    triangle = MyTriangle(O, B, A)
    angle = triangle.angle_A
    if major_arc:   angle = 2 * PI - angle  #如果是优弧
    return angle

def right_to_polar(O, P):
    #以点O为原点,把点P的直角坐标(np坐标)转换成以点O为极点,点P的极坐标
    r = get_len(O, P)
    theta = arg_angle(O, P)
    return [r, theta]

def polar_to_right(r, theta):
    #把极坐标转换成直角坐标(np坐标)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return np.array([x, y, 0])

def get_line_middle_point(P1, P2):
    '''
    param P1: 第一个点np坐标
    param P2: 第二个点np坐标
    return: 返回两点之间的中点
    '''
    x1, y1, x2, y2 = P1[0], P1[1], P2[0], P2[1]

    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    return np.array([x, y, 0])


def get_triangle_circumference(triangle):
    '''
    param triangle: MyTriangle对象
    return: 返回该三角形的周长
    '''
    return triangle.a + triangle.b + triangle.c


def get_triangle_area(triangle):
    '''
    param triangle: MyTriangle对象
    return: 返回该三角形的面积
    '''
    p = get_triangle_circumference(triangle) / 2
    return np.sqrt(p * (p - triangle.a) * (p - triangle.b) * (p - triangle.c))


def two_determinant(two_list):
    '''
    param two_list: 2*2数表（二维数组）
    return: 行列式
    '''
    a, b = two_list[0][0], two_list[0][1]
    c, d = two_list[1][0], two_list[1][1]
    return a * d - b * c


def three_determinant(three_list):
    '''
    param two_list: 3*3数表（二维数组）
    return: 行列式
    '''
    a, b, c = three_list[0][0], three_list[0][1], three_list[0][2]
    d, e, f = three_list[1][0], three_list[1][1], three_list[1][2]
    g, h, i = three_list[2][0], three_list[2][1], three_list[2][2]
    return a * two_determinant([[e, f], [h, i]]) - b * two_determinant([[d, f], [g, i]]) + c * two_determinant([[d, e], [g, h]])


def get_two_points_line(P1, P2):
    '''
    两点式化斜截式
    param P1: 第一个点的坐标P1(x1,y1)
    param P2: 第二个点的坐标P2(x2,y2)
    return: [k, b]
    '''
    x1, y1, x2, y2 = P1[0], P1[1], P2[0], P2[1]
    k = (y2 - y1) / (x2 - x1)
    b = y1 - x1 * (y2 - y1) / (x2 - x1)
    return [k, b]


def two_lines_intersection(k1, b1, k2, b2):
    '''
    两条斜截式直线交点
    param k1: 第一条直线斜率
    param b1: 第一条直线截距
    param k2: 第二条直线斜率
    param b2: 第二条直线截距
    return: [x, y]交点np坐标
    '''
    x = -(b1 - b2)/(k1 - k2)
    y = (k2 * b1 - k1 * b2) / (k2 - k1)
    return np.array([x, y, 0])

#自定义对象
class MyTriangle():

    ################战前信息########################

    def __init__(self, A, B, C):
        '''
        (基本属性)
        param A: A点np坐标
        param B: B点np坐标
        param C: C点np坐标
        '''

        self.A = A  # A的np坐标
        self.B = B  # B的np坐标
        self.C = C  # C的np坐标
        self.x1, self.y1 = A[0], A[1]
        self.x2, self.y2 = B[0], B[1]
        self.x3, self.y3 = C[0], C[1]
        self.a = get_len(B, C)  # 线段BC,即a的长度
        self.b = get_len(A, C)  # 线段AC,即b的长度
        self.c = get_len(A, B)  # 线段AB,即c的长度
        self.angle_A = math.acos((self.b * self.b + self.c * self.c - self.a * self.a) / (2 * self.b * self.c))  # 余弦定理
        self.angle_B = math.acos((self.a * self.a + self.c * self.c - self.b * self.b) / (2 * self.a * self.c))
        self.angle_C = math.acos((self.a * self.a + self.b * self.b - self.c * self.c) / (2 * self.a * self.b))

    ############四线交三边战区######################

    '''
    特别注意！！！如果高线,中线,角平分线的辐角为90°，就会产生不可扭转的错误！(斜率不存在)
    如有需要，请将MyTriangle对象三个顶点进行适当调整。
    (Bug修复ing......)
    '''
    #三条高线与对边交点坐标
    def get_drop_feet(self):
        points = []
        A, B, C, O = self.A, self.B, self.C, self.get_orthocenter()
        points.append(two_lines_intersection(
            *get_two_points_line(A, O), *get_two_points_line(B, C)))
        points.append(two_lines_intersection(
            *get_two_points_line(B, O), *get_two_points_line(C, A)))
        points.append(two_lines_intersection(
            *get_two_points_line(C, O), *get_two_points_line(A, B)))
        return points

    #三条中线与对边交点坐标
    def get_middle_points(self):
        points = []
        A, B, C, O = self.A, self.B, self.C, self.get_centroid()
        points.append(two_lines_intersection(
            *get_two_points_line(A, O), *get_two_points_line(B, C)))
        points.append(two_lines_intersection(
            *get_two_points_line(B, O), *get_two_points_line(C, A)))
        points.append(two_lines_intersection(
            *get_two_points_line(C, O), *get_two_points_line(A, B)))
        return points

    #三条角平分线线与对边交点坐标
    def get_angle_bisector_intersection(self):
        points = []
        A, B, C, O = self.A, self.B, self.C, self.get_incenter()
        points.append(two_lines_intersection(
            *get_two_points_line(A, O), *get_two_points_line(B, C)))
        points.append(two_lines_intersection(
            *get_two_points_line(B, O), *get_two_points_line(C, A)))
        points.append(two_lines_intersection(
            *get_two_points_line(C, O), *get_two_points_line(A, B)))
        return points

    #三条垂直平分线与对边交点坐标(三边中点)
    def get_vertical_bisector_intersection(self):
        points = []
        A, B, C = self.A, self.B, self.C
        points.append(get_line_middle_point(B, C))
        points.append(get_line_middle_point(C, A))
        points.append(get_line_middle_point(A, B))
        return points

    #############五心战区######################

    #垂心
    def get_orthocenter(self):
        #链接：https://zh.wikipedia.org/wiki/%E9%AB%98%E7%BA%BF
        x1, x2, x3, y1, y2, y3 = self.x1, self.x2, self.x3, self.y1, self.y2, self.y3

        X1_list = [
            [x2 * x3 + y2 * y3, 1, y1],
            [x3 * x1 + y3 * y1, 1, y2],
            [x1 * x2 + y1 * y2, 1, y3]
        ]
        X2_list = [
            [x1, y1, 1],
            [x2, y2, 1],
            [x3, y3, 1]
        ]
        Y1_list = [
            [x2 * x3 + y2 * y3, x1, 1],
            [x3 * x1 + y3 * y1, x2, 1],
            [x1 * x2 + y1 * y2, x3, 1]
        ]
        Y2_list = [
            [x1, y1, 1],
            [x2, y2, 1],
            [x3, y3, 1]
        ]
        X1 = three_determinant(X1_list)
        X2 = three_determinant(X2_list)
        Y1 = three_determinant(Y1_list)
        Y2 = three_determinant(Y2_list)
        x = X1 / X2
        y = Y1 / Y2
        return np.array([x, y, 0])

    #重心
    def get_centroid(self):
        #链接：https://zh.wikipedia.org/wiki/%E5%87%A0%E4%BD%95%E4%B8%AD%E5%BF%83
        x1, x2, x3, y1, y2, y3 = self.x1, self.x2, self.x3, self.y1, self.y2, self.y3

        x = (x1 + x2 + x3) / 3
        y = (y1 + y2 + y3) / 3
        return np.array([x, y, 0])

    #外心
    def get_circumcenter(self):
        #链接：https://zh.wikipedia.org/wiki/%E5%A4%96%E6%8E%A5%E5%9C%93
        x1, x2, x3, y1, y2, y3 = self.x1, self.x2, self.x3, self.y1, self.y2, self.y3

        X1_list = [
            [x1 * x1 + y1 * y1, y1, 1],
            [x2 * x2 + y2 * y2, y2, 1],
            [x3 * x3 + y3 * y3, y3, 1]
        ]
        X2_list = [
            [x1, y1, 1],
            [x2, y2, 1],
            [x3, y3, 1]
        ]
        Y1_list = [
            [x1, x1 * x1 + y1 * y1, 1],
            [x2, x2 * x2 + y2 * y2, 1],
            [x3, x3 * x3 + y3 * y3, 1]
        ]
        Y2_list = [
            [x1, y1, 1],
            [x2, y2, 1],
            [x3, y3, 1]
        ]
        X1 = three_determinant(X1_list)
        X2 = 2 * three_determinant(X2_list)
        Y1 = three_determinant(Y1_list)
        Y2 = 2 * three_determinant(Y2_list)
        x = X1 / X2
        y = Y1 / Y2
        return np.array([x, y, 0])

    #内心
    def get_incenter(self):
        #链接：https://zh.wikipedia.org/wiki/%E5%86%85%E5%88%87%E5%9C%86
        x1, x2, x3, y1, y2, y3 = self.x1, self.x2, self.x3, self.y1, self.y2, self.y3
        a, b, c = self.a, self.b, self.c

        x = (a * x1 + b * x2 + c * x3) / (a + b + c)
        y = (a * y1 + b * y2 + c * y3) / (a + b + c)
        return np.array([x, y, 0])

    #旁心(三个)
    def get_excenter(self):
        #链接：https://zh.wikipedia.org/wiki/%E6%97%81%E5%88%87%E5%9C%93
        x1, x2, x3, y1, y2, y3 = self.x1, self.x2, self.x3, self.y1, self.y2, self.y3
        a, b, c = self.a, self.b, self.c

        Ja_x = (-a * x1 + b * x2 + c * x3) / (-a + b + c)
        Ja_y = (-a * y1 + b * y2 + c * y3) / (-a + b + c)
        Jb_x = (a * x1 - b * x2 + c * x3) / (a - b + c)
        Jb_y = (a * y1 - b * y2 + c * y3) / (a - b + c)
        Jc_x = (a * x1 + b * x2 - c * x3) / (a + b - c)
        Jc_y = (a * y1 + b * y2 - c * y3) / (a + b - c)

        return [np.array([Ja_x, Ja_y, 0]), np.array([Jb_x, Jb_y, 0]), np.array([Jc_x, Jc_y, 0])]

#VGroup对象
def MyAngle(A, O, B, radius, color, line_width=0.05):
    #角
    start_angle = arg_angle(O, B)
    angle = get_angle(A, O, B)

    return VGroup(
        AnnularSector(
            start_angle,
            angle,
            arc_center=O,
            inner_radius=radius - line_width,
            outer_radius=radius,
            color=color
        ),
        Sector(
            start_angle,
            angle,
            arc_center=O,
            outer_radius=radius - line_width,
            color=color,
            fill_opacity=1 / 3
        )
    )

def MyRightAngle(A, O, B, width, color, line_width=DEFAULT_STROKE_WIDTH):
    #直角符号   width:直角符号的边长
    #实际上，这个直角符号是个菱形,只不过是为了融洽性
    #即使∠AOB不是直角，该函数也会返回个菱形
    start_angle = arg_angle(O, B)
    angle = get_angle(A, O, B)
    OQ1 = polar_to_right(width, start_angle + angle)
    OQ2 = polar_to_right(width, start_angle)
    OP = OQ1 + OQ2
    P, Q1, Q2 = O + OP, O + OQ1, O + OQ2
    return Polygon(
        O, Q2, P, Q1,
        color = color,
        fill_color = color,
        fill_opacity = 1 / 3,
        stroke_width = line_width
    )

def MyArrow(start, end, color):
    #尖顶的向量
    #效果详见manim交流群群文件MyArrow宣传片.mp4
    ARC = PI / 180
    AB = 1 / 3
    BQ = CQ = AB * np.sin(17 * ARC)
    PQ = BQ / np.tan(50 * ARC)
    AQ = AB * np.cos(17 * ARC)
    AP = AQ - PQ
    #设A点坐标为(0, 0)
    A, B, P, C = np.array([0., 0., 0.]), np.array([-AQ, BQ, 0.]), np.array([-AP, 0., 0.]), np.array([-AQ, -CQ, 0.])

    #平移箭头
    arrow_len = get_len(start, end)
    A[0] += arrow_len
    B[0] += arrow_len
    P[0] += arrow_len
    C[0] += arrow_len

    #旋转箭头
    theta = arg_angle(start, end)
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
        Polygon(A, B, P, C, color=color, fill_opacity=1).set_stroke(width=DEFAULT_STROKE_WIDTH/4),
    )

#实验区
class Lab(Scene):
    def dot_map(self):
        dots = VGroup()
        nums = VGroup()
        for x in range(-7, 8):
            for y in range(-4, 5):
                dots.add(Dot().scale(0.5).move_to(
                    RIGHT * x + UP * y).set_opacity(1 / 4))
                if y == 0:
                    nums.add(TextMobject(str(x)).scale(0.5).move_to(
                        RIGHT * x + UP * y + DOWN * 1 / 4).set_opacity(1 / 4))
                if x == 0 and y != 0:
                    nums.add(TextMobject(str(y)).scale(0.5).move_to(
                        RIGHT * x + UP * y + LEFT * 1 / 4).set_opacity(1 / 4))
        self.add(dots, nums)
    def construct(self):
        self.dot_map()
        A, O, B = np.array([-3, 3, 0]), ORIGIN, np.array([3, 1, 0])
        line_AO = Line(A, O, color=YELLOW)
        line_OB = Line(O, B, color=YELLOW)
        dot_O = Dot(O, color=WHITE)
        right_angle = MyRightAngle(A, O, B, width=1 / 4, color=YELLOW)

        self.add(line_AO, line_OB, dot_O, right_angle)
        self.wait(2)
