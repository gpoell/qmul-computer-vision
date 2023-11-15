import numpy as np

def create_test_image():
    # Create test image and degree to rotate
    square = np.zeros((1,1,3))
    theta = 45
    # Create RGB color channels representative of 3 dimension
    r = [255, 0, 0]
    g = [0, 255, 0]
    b = [0, 0, 255]

    # Add the RGB array to canvas
    red = square + r
    green = square + g
    blue = square + b

    # Concatenate the matrices together and stack horizontally
    hresult = np.concatenate((blue, green, red), axis=1)
    image = np.concatenate((hresult, hresult, hresult), axis=0)

    return image