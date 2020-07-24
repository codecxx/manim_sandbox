from manimlib.imports import *

class Tracked_Point(VGroup):
    CONFIG = {
        'size': 0.1,
        'point_color': BLUE,
        'num_decimal_places': 2,
        'coordinates_scale': 0.8,
        'coordinates_color': GREEN,
        'coordinates_direction': DOWN * 0.25,
        'bracket_color': WHITE,
    }
    def __init__(self, init_loc=ORIGIN, **kwargs):

        VGroup.__init__(self, **kwargs)
        self.point = Dot(init_loc, color=self.point_color).set_height(self.size)
        self.value_x = DecimalNumber(0, color=self.coordinates_color, num_decimal_places=self.num_decimal_places).scale(self.coordinates_scale)
        self.value_y = DecimalNumber(0, color=self.coordinates_color, num_decimal_places=self.num_decimal_places).scale(self.coordinates_scale)
        text = TexMobject('(', ',', ')').scale(self.coordinates_scale)
        self.coordinates_text = VGroup(text[0], self.value_x, text[1], self.value_y, text[2])
        self.coordinates_text.add_updater(self.update_coordinates_text)
        self.add(self.point)

    def update_coordinates_text(self, coords):
        for i in range(1, len(coords)):
            coords[i].next_to(coords[i-1], RIGHT * 0.5)
        coords[2].align_to(coords[1], DOWN)
        pos = self.point.get_center()
        x, y = self.mapping_func(pos[0], pos[1])
        coords[1].set_value(x)
        coords[3].set_value(y)
        coords.next_to(self.point, self.coordinates_direction)

    def mapping_func(self, x, y):
        return x, y

class Test_point_tracker(Scene):

    def construct(self):
        numberplane = NumberPlane()
        self.play(ShowCreation(numberplane))
        self.wait()
        point = Tracked_Point(RIGHT * 3, size=0.25)

        self.play(ShowCreation(point), ShowCreation(point.coordinates_text))
        self.wait()
        self.play(Rotating(point, radians=TAU, about_point=ORIGIN), run_time=10)
        self.wait(2)
