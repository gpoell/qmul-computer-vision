import numpy as np
import matplotlib.pyplot as plt

# This function creates histograms for RGB values of an image and saves them to the output/figures directory
# It takes two parameters
#   1. index: this integer value is used for the naming convention of the saved image
#   2. image: an image to process the RGB values

def ICV_color_histogram(index, image):

    # Convert the index to a string to avoid conflicts with saving
    index = str(index)

    # Separate RGB color channels
    red, green, blue = image[:,:,0], image[:,:,1], image[:,:,2]

    # Use Numpy Flatten to convert the arrays to 1-D to be processed by Histogram
    # For example, this converts a frame of 960 x 1280 to an array of 1,228,800 x 1
    red_pixels = red.flatten()
    green_pixels = green.flatten()
    blue_pixels = blue.flatten()

    # Overlay histograms of the pixels of each color in the bottom subplot
    plt.figure(figsize=(12, 12))
    plt.hist(red_pixels, bins=256, density=False, color='red', histtype='step')
    plt.hist(green_pixels, bins=256, density=False, color='green', histtype='step')
    plt.hist(blue_pixels, bins=256, density=False, color='blue', histtype='step')

    # Update the title and labels of the figures
    plt.title('RGB Values for Image ' + index)
    plt.ylabel('RGB Counts')
    plt.xlabel('RGB Values')

    # Save the figure
    plt.savefig(fname=f'../../output/cw3/figures/figure{index}.png')

    # Return RGB pixel values for processing distance
    return [red_pixels, green_pixels, blue_pixels]
