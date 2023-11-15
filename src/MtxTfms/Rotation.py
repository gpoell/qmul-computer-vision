import numpy as np
import math

class Rotation:

    def __init__(self, image, theta):
        self.image = image
        self.image_x = None
        self.image_y = None
        self.new_image = []
        self.origin = self.calc_origin()
        self.theta = (theta/360)*(2*np.pi)
        self.r_mtx = self.calc_rotation_mtx()
        self.new_origin = self.calc_new_origin()

    def calc_origin(self):
        # determine original image shape - decrement by 1 to align with array indexing
        self.image_x = np.shape(self.image)[0]-1
        self.image_y = np.shape(self.image)[1]-1

        origin_x = math.floor(self.image_x/2)
        origin_y = math.floor(self.image_y/2)
        return [origin_x, origin_y]
    
    def calc_new_origin(self):
        # determine original positions of image corners
        top_left = np.subtract([0, 0], self.origin)
        top_right = np.subtract([0, self.image_y], self.origin)
        # bottom_left = np.subtract([self.image_x, 0], self.origin)
        # bottom_right = np.subtract([self.image_x, self.image_y-1], self.origin)

        # Transform the corners -- return rounded integer values
        t_top_left = np.dot(self.r_mtx, top_left).astype(int)
        t_top_right = np.dot(self.r_mtx, top_right).astype(int)
        # t_bottom_left = np.dot(self.r_mtx, bottom_left).astype(int)
        # t_bottom_right = np.dot(self.r_mtx, bottom_right).astype(int)

        # Calculate new origin
        new_origin_y = int(np.abs(t_top_left[1]))
        new_origin_x = int(np.abs(t_top_right[0]))
        new_origin = [new_origin_x, new_origin_y]

        return new_origin

    
    def calc_canvas(self):
        # Give a small buffer of pixels to adjust for errors
        result = np.array(self.new_origin) + 1
        result *= 2
        return np.array(result)
                

    def calc_rotation_mtx(self):
        # Create the rotation matrix
        return np.array([[round(np.cos(self.theta), 3), round(-np.sin(self.theta), 3)],
                                  [round(np.sin(self.theta), 3), round(np.cos(self.theta), 3)]])
    
    # Calculate the pixel vectors with respect to the origin so we can perform the rotation
    def calc_pixel_vector(self, p, o):
        return [int((p[0] - o[0])), int((p[1] - o[1]))]
    
    # Tranform the pixel vector by theta using the rotation matrix
    def calc_transform_vector(self, pxl_vector):
        return np.dot(self.r_mtx, pxl_vector)
    
    # Rotate the Image and return it on a new image -- issues discussed in report
    def rotate_image(self):
        # Generate a new canvas the size of the image
        canvas = self.calc_canvas()
        canvas = np.zeros(([canvas[0], canvas[1], 3]))+255

        for i in range(self.image_x+1):
            for j in range(self.image_y+1):
                pxl_vals = self.image[i, j]
                pxl_coords = [i, j]
                pxl_vector = self.calc_pixel_vector(pxl_coords, self.origin)
                t_vector = self.calc_transform_vector(pxl_vector)
                result_vector = t_vector + self.new_origin
                res_x = int(result_vector[0])
                res_y = int(result_vector[1])
                canvas[res_x, res_y] = pxl_vals

        return canvas