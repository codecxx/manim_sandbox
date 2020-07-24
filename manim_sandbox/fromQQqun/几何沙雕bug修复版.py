import numpy as np
import math

'''
欢迎使用几何沙雕！
在这里，你可以用幼儿园学的几何基础来构造几何模型！
你可以通过不同的方式定义直线，比如两点式，点斜式以用来获取它的仰角、斜率、参数方程坐标等沙雕信息
通过这些直线，你可以通过平移、旋转、关于点和直线对称等沙雕变换
通过这些沙雕变换，你又可以过某点作一条直线的平行线、垂线、角平分线、垂直平分线等沙雕作法
此外，通过这些沙雕操作，这里添加了“三角形五心”的专题。在这里，你可以获得三角形各个边长、角度、五心、欧拉线等沙雕信息
这里，为你的manim沙雕之路护航！

萌新：麻麻再也不用担心我带不动Geogebra、Desmos了！
大佬：这是什么垃圾？

作者：我是害羞的向量
备注：如有修改建议、添加建议、bug，请联系作者并素质三连该可爱的鸽子
'''

#圆周率
PI = math.pi
#旋转矩阵
ROTATE_MATRIX = lambda angle: np.array([
    [np.cos(angle), -np.sin(angle), 0],
    [np.sin(angle), np.cos(angle),  0],
    [0,             0,              0]
])

class MTwoPointLine():
    #线段类(通过两个点定义)
    #或者说,是一条有向线段

    def __init__(self, P0, P1):
        #初始化对象属性, P0起点,P1终点
        self.P0, self.P1 = P0, P1   #两点坐标
        self.vector = P1 - P0   #向量
        self.delta_x = self.vector[0]   #从起点到终点x的变化量
        self.delta_y = self.vector[1]   #从起点到终点y的变化量
        self.length = length_of_two_point(P0, P1)   ##length_of_two_point(A, B)返回两点距离。向量模长(线段长度)
        if self.delta_x == 0:   #判断是否斜率不存在(k=Δy/Δx)
            self.k = None
        else:
            self.k = self.delta_y / self.delta_x
        self.angle = arg_angle(P0, P1)  #arg_angle(start, end)函数在最后面有定义,功能:返回向量(有向线段)辐角(仰角)

        #参数函数定义线段
        self.t = np.linspace(0, 1, 1000)    #取t∈[0,1]
        self.P = [] #点集
        for t_n in self.t:
            self.P.append(P0 + self.vector * t_n)   #线段参数方程:P1+(P2-P1)t
    
    def shift(self, vec):
        #返回平移后的线段, vec:平移向量
        P0 = self.P0 + vec
        P1 = self.P1 + vec
        line = MTwoPointLine(P0, P1)

        return line
    
    def rotate(self, point, angle):
        #返回逆时针旋转后的线段, point:旋转中心, angle:旋转角度
        P0, P1 = self.P0 - point, self.P1 - point   #先把要旋转中心点平移到原点
        P0 = np.inner(ROTATE_MATRIX(angle), P0.T).T + point #旋转+平移回去
        P1 = np.inner(ROTATE_MATRIX(angle), P1.T).T + point
        line = MTwoPointLine(P0, P1)

        return line
    
    def symmetry_of_point(self, point):
        #返回关于某点对称后的线段
        return self.rotate(point, PI)
    
    def symmetry_of_line(self, line):
        #返回关于某直线(线段)对称后的线段
        v_line_1, v_line_2 = MVerticalLine(self.P0, line), MVerticalLine(self.P1, line) #MVerticalLine类:作某线过某点的垂线
        M1, M2 = cross_lines_point(v_line_1, line), cross_lines_point(v_line_2, line)   #cross_lines_point(l1, l2):返回两线交点,这里M1,M2都是垂足
        vec_P0M1, vec_P1M2 = M1 - self.P0, M2 - self.P1 #向量
        vec_P0P0, vec_P1P1 = 2 * vec_P0M1, 2 * vec_P1M2 #倍长向量(轴对称是两点线段的垂直‘平分’线)
        P0, P1 = self.P0 + vec_P0P0, self.P1 + vec_P1P1 #把向量加上'腿',就是坐标啦
        return MTwoPointLine(P0, P1)



class MTwoPointStraightLine(MTwoPointLine):
    #直线类(通过两个点定义,两点确定一条直线)
    #或者说是特别长的有向线段

    def __init__(self, A, B, start_length = 10, end_length = 10):
        #计算起点终点并传给父类处理
        AB_length = length_of_two_point(A, B)   #AB长度
        P = (A + B) / 2 #为了形式上的美观(吃饱撑得闲),从中点延展分别向起点终点延展start_length,end_length
        #算了懒得解释,自己在草稿本上画画
        vec_PB = B - P
        t0 = - 2 * start_length / AB_length
        t1 = 2 * end_length / AB_length
        P0 = P + vec_PB * t0
        P1 = P + vec_PB * t1
        super(MTwoPointStraightLine, self).__init__(P0, P1)

class MPointAngleStraightLine(MTwoPointStraightLine):
    #直线类(通过一个点和仰角定义,其实就是点斜式直线啦)

    def __init__(self, A, angle):
        vec_AB = np.array([math.cos(angle), math.sin(angle), 0])
        B = A + vec_AB
        super(MPointAngleStraightLine, self).__init__(A, B)



class MParallelLine(MPointAngleStraightLine):
    #平行直线类(过某点作已知直线的平行线)

    def __init__(self, Q, line):
        super(MParallelLine, self).__init__(Q, line.angle)

class MVerticalLine(MPointAngleStraightLine):
    #垂直直线类(过某点作已知直线的垂线)

    def __init__(self, Q, line):
        super(MVerticalLine, self).__init__(Q, line.angle + PI / 2)

class MBisectOfAngle(MPointAngleStraightLine):
    #角平分直线类(通过三个点确定一个角,然后把角平分)

    def __init__(self, A, O, B):
        l1 = MTwoPointLine(O, A)
        l2 = MTwoPointLine(O, B)
        angle = cross_lines_angle(A, O, B)
        print(l1.angle * 180 / PI)
        print(l2.angle * 180 / PI)
        print(angle * 180 / PI)
        if l1.angle >= l2.angle:
            super(MBisectOfAngle, self).__init__(O, l2.angle + angle / 2)
            print(1)
        else:
            super(MBisectOfAngle, self).__init__(O, l1.angle + angle / 2)
            print(2)

class MBisectOfVertical(MVerticalLine):
    #垂直平分直线类(作'线段'的垂直平分线)

    def __init__(self, line):
        M = (line.P0 + line.P1) / 2
        super(MBisectOfVertical, self).__init__(M, line)



class MTriangle():
    #三角形类(通过三个点来确定三角形)

    def __init__(self, A, B, C):
        self.A, self.B, self.C = A, B, C    #三点坐标

        self.a, self.b, self.c = length_of_two_point(B, C), length_of_two_point(C, A), length_of_two_point(A, B)    #三边长度
        a, b, c = self.a, self.b, self.c

        self.angle_A = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)) #三个角的度数, 余弦定理
        self.angle_B = math.acos((c ** 2 + a ** 2 - b ** 2) / (2 * c * a))
        self.angle_C = math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))

        self.Cir = a + b + c    #周长

        p = self.Cir / 2    #半周长
        self.Area = math.sqrt(p * (p - a) * (p - b) * (p - c))  #面积, 海伦公式

        self.high_points = self.get_high_lines(A, B, C)[:3]     #三条高分别与相应的对边的交点
        self.cross_high_point = self.get_high_lines(A, B, C)[-1]    #垂心

        self.midpoints = self.get_midlines(A, B, C)[:3] #三条中线分别与相应的对边的交点
        self.cross_midpoint = self.get_midlines(A, B, C)[-1]    #重心

        self.bisect_of_angle_points = self.get_bisect_of_angle_lines(A, B, C)[:3]   #三条角平分线分别与相应的对边的交点
        self.cross_bisect_angle_point = self.get_bisect_of_angle_lines(A, B, C)[-1] #内心

        self.bisect_vertical_points = self.get_bisect_verticals(A, B, C)[:3]    #三条垂直平分线分别与相应的对边的交点
        self.cross_bisect_vertical_point = self.get_bisect_verticals(A, B, C)[-1]   #外心

        self.Euler_line = MTwoPointLine(self.cross_high_point, self.cross_midpoint) #欧拉线

    def get_high_lines(self, A, B, C):
        AB, BC, CA = MTwoPointLine(A, B), MTwoPointLine(B, C), MTwoPointLine(C, A)
        AD, BE, CF = MVerticalLine(A, BC), MVerticalLine(B, CA), MVerticalLine(C, AB)
        D, E, F = cross_lines_point(AD, BC), cross_lines_point(BE, CA), cross_lines_point(CF, AB)
        point = cross_lines_point(BE, CF)
        return [D, E, F, point]

    def get_midlines(self, A, B, C):
        D = (B + C) / 2
        E = (C + A) / 2
        F = (A + B) / 2
        AB, BC, CA = MTwoPointLine(A, B), MTwoPointLine(B, C), MTwoPointLine(C, A)
        BE, CF = MVerticalLine(B, CA), MVerticalLine(C, AB)
        point = cross_lines_point(BE, CF)
        return [D, E, F, point]
    
    def get_bisect_of_angle_lines(self, A, B, C):
        AB, BC, CA = MTwoPointLine(A, B), MTwoPointLine(B, C), MTwoPointLine(C, A)
        AD, BE, CF = MBisectOfAngle(B, A, C), MBisectOfAngle(A, B, C), MBisectOfAngle(A, C, B)
        D, E, F = cross_lines_point(AD, BC), cross_lines_point(BE, CA), cross_lines_point(CF, AB)
        point = cross_lines_point(BE, CF)
        return [D, E, F, point]

    def get_bisect_verticals(self, A, B, C):
        AB, BC, CA = MTwoPointLine(A, B), MTwoPointLine(B, C), MTwoPointLine(C, A)
        AD, BE, CF = MBisectOfVertical(AB, CA), MBisectOfVertical(AB, BC), MBisectOfVertical(BC, CA)
        D, E, F = cross_lines_point(AD, BC), cross_lines_point(BE, CA), cross_lines_point(CF, AB)
        point = cross_lines_point(BE, CF)
        return [D, E, F, point]
    
    #这里我懒得写旁心了=w=,请自行添加[滑稽]



def arg_angle(start, end):
    #求射线辐角     start:顶点的np坐标  end:射线方向点的np坐标
    start_x, start_y, end_x, end_y = start[0], start[1], end[0], end[1]
    mode = 1    #以start为坐标系原点,判断象限
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

def cross_lines_point(l1, l2):
    #求两条线段的交点(即使线段没有相交也会自己找出来)
    k1, k2 = l1.k, l2.k #两条直线的斜率k
    b1 = - k1 * l1.P0[0] + l1.P0[1] #偏移量b
    b2 = - k2 * l2.P0[0] + l2.P0[1]
    if k1 == k2:    #两条直线斜率相等时
        if b1 == b2:    #1.重合
            return l1.P #返回其中一条线的点集
        else:   #2.平行
            return None #无交点
    elif k1 == None:    #如果其中一条直线垂直于x轴(即k不存在)
        x = l1.P0[0]    #交点横坐标就取这条直线的任意一点(以P0为例)的x坐标
        y = k2 * x + b2 #x有了,根据另一条直线的解析式就可以推出交点y坐标了
        return np.array([x, y, 0])
    elif k2 == None:
        x = l2.P0[0]
        y = k1 * x + b1
    else:   #一切正常的情况下
        x = - (b1 - b2) / (k1 - k2)
        y = k1 * x + b1

    return np.array([x, y, 0])

def cross_lines_angle(A, O, B):
    #返回由三个点定义的角的度数
    a, o, b = length_of_two_point(O, B), length_of_two_point(B, A), length_of_two_point(A, O)
    angle_O = math.acos((b ** 2 + a ** 2 - o ** 2) / (2 * b * a))
    
    return angle_O

def length_of_two_point(A, B):
    #返回两点的距离
    vec_AB = B - A
    return math.sqrt(np.sum(vec_AB ** 2))
