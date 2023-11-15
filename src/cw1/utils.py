import numpy as np
import math

# Creates a rotation matrix based on provided angle
def ICV_t_rotate(theta): 
    return np.array([
            [round(np.cos(theta), 3), round(-np.sin(theta), 3)],
            [round(np.sin(theta), 3), round(np.cos(theta), 3)]
        ])

# Creates a shear matrix using provided angle
def ICV_t_shear(theta):
    return np.array([
        [1, 1/np.tan(theta)],
        [0, 1]
    ])

# Function to calculate the origin of an image
def ICV_img_origin(image):
    image_x = np.shape(image)[0]
    image_y = np.shape(image)[1]

    origin_x = math.floor(image_x/2)
    origin_y = math.floor(image_y/2)
    return [origin_x, origin_y]

# Function to generate a new canvas to fit the transformed image
def ICV_generate_canvas(image, origin, transform):
    image_x = np.shape(image)[0]
    image_y = np.shape(image)[1]

    top_left = np.subtract([0, 0], origin)
    top_right = np.subtract([0, image_y], origin)
    bottom_left = np.subtract([image_x, 0], origin)
    bottom_right = np.subtract([image_x, image_y], origin)

    t_top_left = np.abs(np.dot(transform, top_left).astype(int))
    t_top_right = np.abs(np.dot(transform, top_right).astype(int))
    t_bottom_left = np.abs(np.dot(transform, bottom_left).astype(int))
    t_bottom_right = np.abs(np.dot(transform, bottom_right).astype(int))

    canvas_x = np.max([t_top_left[0], t_top_right[0], t_bottom_left[0], t_bottom_right[0]])*2
    canvas_y = np.max([t_top_left[1], t_top_right[1], t_bottom_left[1], t_bottom_right[1]])*2
    return np.zeros((canvas_x+1, canvas_y+1, 3))+255


# Function to perform the transformation of a given image and the transform matrix
def ICV_transform_image(image, transform):
    image_x = np.shape(image)[0]
    image_y = np.shape(image)[1]

    # Calculate the origin of the image
    origin = ICV_img_origin(image)

    # Generate New Canvas
    canvas = ICV_generate_canvas(image, origin, transform)

    # Generate new origin to align pixels
    new_origin = ICV_img_origin(canvas)

    for i in range(image_x):
        for j in range(image_y):
            pxl_vals = image[i, j]
            pxl_coords = [i, j]
            # Calculate the pixel vectors with respect to the origin so we can perform the rotation
            pxl_vector = [int((pxl_coords[0] - origin[0])), int((pxl_coords[1] - origin[1]))]
            # Tranform the pixel vector by theta using the rotation matrix
            t_vector = np.dot(transform, pxl_vector)
            result_vector = t_vector + new_origin
            res_x = int(result_vector[0])
            res_y = int(result_vector[1])
            canvas[res_x, res_y] = pxl_vals
    
    return canvas

def ICV_cw1(image, theta1, theta2, flag=None):

    # Theta1 is used for Rotations
    theta1 = np.radians(theta1)

    # Theta2 is used for Shear
    theta2 = np.radians(theta2)

    # Rotation Matrix
    t_rotate = ICV_t_rotate(theta1)

    # Shear matrix
    t_shear =  ICV_t_shear(theta2)

    # Calculate the transformation matrix for rotating by θ1 and skewing by θ2
    if flag == "reverse":
        transform = np.dot(t_rotate, t_shear)
    else:
        transform = np.dot(t_shear, t_rotate)

    # Perform the transformation of the image
    result = ICV_transform_image(image, transform)

    return result