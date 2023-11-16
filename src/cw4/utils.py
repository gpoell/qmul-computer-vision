import numpy as np
import matplotlib.pyplot as plt

# Function to divide an image into equal sized windows (9 for this example)
def ICV_img_windows(image):
    im_x = int(np.shape(image)[0] / 3)
    im_y = int(np.shape(image)[1] / 3)

    # Assuming this is a square image
    result =  [
        image[:im_x, :im_y],
        image[:im_x, im_y:im_y*2],
        image[:im_x, im_y*2:],
        image[im_x:im_x*2, :im_y],
        image[im_x:im_x*2, im_y:im_y*2],
        image[im_x:im_x*2, im_y*2:],
        image[im_x*2:, :im_y],
        image[im_x*2:, im_y:im_y*2],
        image[im_x*2:, im_y*2:],
    ]

    # Plot equally divided shapes
    fig, axs = plt.subplots(3, 3)
    axs[0, 0].imshow(result[0], cmap="gray")
    axs[0, 1].imshow(result[1], cmap="gray")
    axs[0, 2].imshow(result[2], cmap="gray")
    axs[1, 0].imshow(result[3], cmap="gray")
    axs[1, 1].imshow(result[4], cmap="gray")
    axs[1, 2].imshow(result[5], cmap="gray")
    axs[2, 0].imshow(result[6], cmap="gray")
    axs[2, 1].imshow(result[7], cmap="gray")
    axs[2, 2].imshow(result[8], cmap="gray")
    plt.savefig(fname=f'../../output/cw4/img_windows.png')

    return result