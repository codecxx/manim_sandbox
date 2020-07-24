import numpy as np 
import sys 
sys.path.append(r"D:\Program Files\manim-master")
from manimlib.imports import *

class Try2(ThreeDScene):
	def construct(self):
		direction = [1.7,1.7,1.7]
		start = [0,0,0]

		axes = ThreeDAxes()
		self.add(axes)
		self.set_camera_orientation(phi=60*DEGREES,theta=115*DEGREES,distance=10)

		max_r = 0.2
		max_tl = 0.4
		delta_theta = 0.4

		#参数看源码注释
		vector1 = ThreeDVector(
			direction=direction,
			ratio_of_tip_length_to_vector_length=1/5,
			max_bottom_radius=max_r,
			max_tip_length=max_tl,
			bottom_circle_delta_theta=delta_theta,
			tip_bottom_circle_delta_theta=delta_theta,
			bottom_circle_side_color=WHITE,
			tip_bottom_circle_side_color=WHITE,
			bottom_circle_side_width=2,
			tip_bottom_circle_side_width=2,
			color=BLUE_E,
			fill_opacity=1)

		br = 0.1
		tbr = 0.2
		tl = 0.4
		delta_theta = 0.4


		vector2 = ThreeDVector2(
			direction=direction,
			bottom_radius=br,
			tip_bottom_radius=tbr,
			tip_length=tl,
			bottom_circle_delta_theta=delta_theta,
			tip_bottom_circle_delta_theta=delta_theta,
			bottom_circle_side_color=BLUE_E,
			tip_bottom_circle_side_color=BLUE_E,
			bottom_circle_side_width=2,
			tip_bottom_circle_side_width=2,
			color=WHITE,
			fill_opacity=1,
			)

		vector1.shift(start)

		#dot = Dot(radius=0.5)
		#dot.shift([1.25,1.25,1.25])

		self.begin_ambient_camera_rotation(rate=0.5)
		self.play(FadeIn(vector2),run_time=2)
		#self.add(vector2)
		self.wait(2)



