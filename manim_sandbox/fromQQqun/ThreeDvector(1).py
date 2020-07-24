"""把这个文件导入进imports里就可以用了"""
from manimlib.mobject.geometry import Polygon

class ThreeDVector(VMobject):
    """
    这个类的原理：
    向量主体和向量顶端是圆锥，
    圆锥的底面是用多边形近似的圆，
    圆锥的侧面也是用多边形拼接的，
    所以d_theta控制多边形近似圆的精度的
    """
    CONFIG = {
    "radio_of_tip_length_to_vector_length":1/5,#顶端圆锥长度与向量长度的比
    "max_bottom_radius":0.05,#向量主体底端圆锥的最大半径
    "max_tip_length":0.4,#顶端圆锥最大长度(圆锥的高)
    "bottom_circle_d_theta":0.7,
    "tip_bottom_circle_d_theta":0.7,
    "fill_opacity":0.8,
    }

    def __init__(self,direction=RIGHT,**kwargs):
        VMobject.__init__(self,**kwargs)
        self.direction = np.array(direction,dtype=np.float)
        if self.get_length(self.direction) != 0:
            self.get_and_reset_some_parameters()
            self.get_rotation_matrix()
            self.get_bottom_circle_points()
            self.get_cone()
            self.get_tip_circle_points()
            self.get_tip_cone()
            self.add(
                self.bottom_circle,
                self.cone_side,
                self.tip_bottom_circle,
                self.tip_cone_side
                )
    def get_and_reset_some_parameters(self):
        l = self.get_length(self.direction)
        tl = l*self.radio_of_tip_length_to_vector_length
        if tl > self.max_tip_length :
            self.tip_length = self.max_tip_length
        else:
            self.tip_length = tl
        self.tip_bottom_radius = self.tip_length/2
        br = self.tip_bottom_radius/4
        if br > self.max_bottom_radius:
            self.bottom_radius = self.max_bottom_radius
        else:
            self.bottom_radius = br
        self.direction *= (l-tl)/l

    def get_rotation_matrix(self):
        rho = self.get_length(self.direction[:2])
        r = self.get_length(self.direction)
        cos_phi = self.direction[2] / r
        sin_phi = rho / r

        if rho != 0:
            cos_theta = self.direction[0] / rho
            sin_theta = self.direction[1] / rho
        else:
            cos_theta = 1
            sin_theta = 0

        self.M_z = np.array([
            [cos_theta,-sin_theta,0],
            [sin_theta,cos_theta,0],
            [0,0,1]
            ])

        self.M_y = np.array([
            [cos_phi,0,sin_phi],
            [0,1,0],
            [-sin_phi,0,cos_phi]
            ])

    def get_bottom_circle_points(self):
        points = []
        for theta in np.arange(\
            0,2*np.pi+self.bottom_circle_d_theta,self.bottom_circle_d_theta):
            point = [self.bottom_radius*np.cos(theta),
                     self.bottom_radius*np.sin(theta),
                     0]
            points.append(point)
        points = np.array(points).T

        self.bc_points = list(np.dot(self.M_z,np.dot(self.M_y,points)).T)

    def get_cone(self):
        self.bottom_circle = Polygon(
            *self.bc_points,
            color=self.color,
            fill_opacity=self.fill_opacity,
            stroke_width=1,
            stroke_color=self.color)

        self.cone_side = VGroup()

        n = 4
        rm_n = (len(self.bc_points)-1)%(n-2)
        step = (len(self.bc_points)-1)//(n-2)
        range1 = range(0,step*(n-2),n-2)
        for i in range1:
            points = [self.bc_points[j] for j in range(i,i+n-1)]
            points.append(self.direction)
            self.cone_side.add(Polygon(
                *points,
                color=self.color,
                fill_opacity=self.fill_opacity,
                stroke_width=1,
                stroke_color=self.color))
        points = [self.bc_points[i] for i in \
            range(step*(n-2),step*(n-2)+rm_n+1)]
        if rm_n != 0:
            points = [self.bc_points[i] for i in \
                range(step*(n-2),step*(n-2)+rm_n+1)]
            points.append(self.direction)
            self.cone_side.add(Polygon(
                *points,
                color=self.color,
                fill_opacity=self.fill_opacity,
                stroke_width=1,
                stroke_color=self.color
                ))

    def get_tip_circle_points(self):
        points = []
        for theta in np.arange(\
            0,2*np.pi+self.tip_bottom_circle_d_theta,self.tip_bottom_circle_d_theta):
            point = [self.tip_bottom_radius*np.cos(theta),
                     self.tip_bottom_radius*np.sin(theta),
                     0]
            points.append(point)
        points = np.array(points).T
        self.tbc_points = list(
            np.dot(self.M_z,np.dot(self.M_y,points)).T + self.direction
            )

    def get_tip_cone(self):
        self.tip_vertex = self.direction + \
            self.direction/self.get_length(self.direction)*self.tip_length

        self.tip_bottom_circle = Polygon(
            *self.tbc_points,
            color=self.color,
            fill_opacity=self.fill_opacity,
            stroke_width=1,
            stroke_color=self.color)

        self.tip_cone_side = VGroup()

        n = 4
        rm_n = (len(self.tbc_points)-1)%(n-2)
        step = (len(self.tbc_points)-1)//(n-2)
        range1 = range(0,step*(n-2),n-2)
        for i in range1:
            points = [self.tbc_points[j] for j in range(i,i+n-1)]
            points.append(self.tip_vertex)
            self.tip_cone_side.add(Polygon(
                *points,
                color=self.color,
                fill_opacity=self.fill_opacity,
                stroke_width=1,
                stroke_color=self.color))
        points = [self.tbc_points[i] for i in \
            range(step*(n-2),step*(n-2)+rm_n+1)]
        if rm_n != 0:
            points = [self.tbc_points[i] for i in \
                range(step*(n-2),step*(n-2)+rm_n+1)]
            points.append(self.tip_vertex)
            self.tip_cone_side.add(Polygon(
                *points,
                color=self.color,
                fill_opacity=self.fill_opacity,
                stroke_width=1,
                stroke_color=self.color
                ))

    def get_length(self,a):
        return np.sqrt(np.sum(np.square(a)))


class ThreeDVector2(VMobject):
    """
    这个类的原理：
    向量主体和向量顶端是圆锥，
    圆锥的底面是用多边形近似的圆，
    圆锥的侧面也是用多边形拼接的，
    所以d_theta控制多边形近似圆的精度的
    """
    CONFIG = {
    "direction":None,#终点
    "bottom_radius":0.05,#向量主体的底面半径
    "bottom_circle_d_theta":0.7,
    "tip_bottom_radius":0.1,#顶端圆锥的底面半径,建议是bottom_radius的四倍
    "tip_bottom_circle_d_theta":0.7,
    "tip_length":0.2,#顶端圆锥的长(圆锥的高)，建议是tip_bottom_radius的两倍
    "fill_opacity":0.8,
    }
    def __init__(self,**kwargs):
        VMobject.__init__(self,**kwargs)
        self.direction = np.array(self.direction)
        if self.get_length(self.direction) != 0:
            self.get_rotation_matrix()
            self.get_bottom_circle_points()
            self.get_cone()
            self.get_tip_circle_points()
            self.get_tip_cone()
            self.add(
                self.bottom_circle,
                self.cone_side,
                self.tip_bottom_circle,
                self.tip_cone_side
                )
    def get_rotation_matrix(self):
        rho = self.get_length(self.direction[:2])
        r = self.get_length(self.direction)
        cos_phi = self.direction[2] / r
        sin_phi = rho / r

        if rho != 0:
            cos_theta = self.direction[0] / rho
            sin_theta = self.direction[1] / rho
        else:
            cos_theta = 1
            sin_theta = 0

        self.M_z = np.array([
            [cos_theta,-sin_theta,0],
            [sin_theta,cos_theta,0],
            [0,0,1]
            ])

        self.M_y = np.array([
            [cos_phi,0,sin_phi],
            [0,1,0],
            [-sin_phi,0,cos_phi]
            ])

    def get_bottom_circle_points(self):
        points = []
        for theta in np.arange(\
            0,2*np.pi+self.bottom_circle_d_theta,self.bottom_circle_d_theta):
            point = [self.bottom_radius*np.cos(theta),
                     self.bottom_radius*np.sin(theta),
                     0]
            points.append(point)
        points = np.array(points).T

        self.bc_points = list(np.dot(self.M_z,np.dot(self.M_y,points)).T)

    def get_cone(self):
        self.bottom_circle = Polygon(
            *self.bc_points,
            color=self.color,
            fill_opacity=self.fill_opacity,
            stroke_width=1,
            stroke_color=self.color)

        self.cone_side = VGroup()

        n = 4
        rm_n = (len(self.bc_points)-1)%(n-2)
        step = (len(self.bc_points)-1)//(n-2)
        range1 = range(0,step*(n-2),n-2)
        for i in range1:
            points = [self.bc_points[j] for j in range(i,i+n-1)]
            points.append(self.direction)
            self.cone_side.add(Polygon(
                *points,
                color=self.color,
                fill_opacity=self.fill_opacity,
                stroke_width=1,
                stroke_color=self.color))
        points = [self.bc_points[i] for i in \
            range(step*(n-2),step*(n-2)+rm_n+1)]
        if rm_n != 0:
            points = [self.bc_points[i] for i in \
                range(step*(n-2),step*(n-2)+rm_n+1)]
            points.append(self.direction)
            self.cone_side.add(Polygon(
                *points,
                color=self.color,
                fill_opacity=self.fill_opacity,
                stroke_width=1,
                stroke_color=self.color
                ))

    def get_tip_circle_points(self):
        points = []
        for theta in np.arange(\
            0,2*np.pi+self.tip_bottom_circle_d_theta,self.tip_bottom_circle_d_theta):
            point = [self.tip_bottom_radius*np.cos(theta),
                     self.tip_bottom_radius*np.sin(theta),
                     0]
            points.append(point)
        points = np.array(points).T
        self.tbc_points = list(
            np.dot(self.M_z,np.dot(self.M_y,points)).T + self.direction
            )

    def get_tip_cone(self):
        self.tip_vertex = self.direction + \
            self.direction/self.get_length(self.direction)*self.tip_length

        self.tip_bottom_circle = Polygon(
            *self.tbc_points,
            color=self.color,
            fill_opacity=self.fill_opacity,
            stroke_width=1,
            stroke_color=self.color)

        self.tip_cone_side = VGroup()

        n = 4
        rm_n = (len(self.tbc_points)-1)%(n-2)
        step = (len(self.tbc_points)-1)//(n-2)
        range1 = range(0,step*(n-2),n-2)
        for i in range1:
            points = [self.tbc_points[j] for j in range(i,i+n-1)]
            points.append(self.tip_vertex)
            self.tip_cone_side.add(Polygon(
                *points,
                color=self.color,
                fill_opacity=self.fill_opacity,
                stroke_width=1,
                stroke_color=self.color))
        points = [self.tbc_points[i] for i in \
            range(step*(n-2),step*(n-2)+rm_n+1)]
        if rm_n != 0:
            points = [self.tbc_points[i] for i in \
                range(step*(n-2),step*(n-2)+rm_n+1)]
            points.append(self.tip_vertex)
            self.tip_cone_side.add(Polygon(
                *points,
                color=self.color,
                fill_opacity=self.fill_opacity,
                stroke_width=1,
                stroke_color=self.color
                ))

    def get_length(self,a):
        return np.sqrt(np.sum(np.square(a)))

