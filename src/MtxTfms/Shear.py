import numpy as np
import math

class Shear:

    def __init__(self, image, percent):
        self.image = image
        self.image_x = None
        self.image_y = None
        self.origin = self.calc_origin()
        self.percent = percent
        self.r_mtx = self.calc_rotation_mtx()
        self.new_origin = self.calc_new_origin()

    