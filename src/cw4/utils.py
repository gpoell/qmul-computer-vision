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

# Define a function that calculates the Local Binary Pattern (LBP) histogram for a given image
def ICV_img_lbp(image):

    img_length = len(image)
    lbp_index = []
    
    for i in range(img_length-3):
        for j in range(img_length-3):
            center = image[i+1, j+1]
            kernel = image[i:i+3, j:j+3]
            # create an LBP array consisting of 0s and 1s for values greater than the center
            lbp = (kernel > center).astype(int)
            # realign ordering for LBP arrays
            lbp = np.array((lbp[0,0], lbp[0,1], lbp[0,2], lbp[1,2], lbp[2,2], lbp[2,1], lbp[2,0], lbp[1,0]))
            # Calculate Base10 LBP value of the pixel  
            base2 = np.array((128, 64, 32, 16, 8, 4, 2, 1))
            lbp *= base2
            # Normalize
            result = np.sum(lbp)/256
            lbp_index.append(result)
    
    return lbp_index

# Function to plot the lbp histograms and return the LBP values to be used as descriptors
def ICV_img_lbp_hist(images):
    # Loop through image windows and plot the LBP Histograms
    lbp_hists = []
    for img in images:
        result = ICV_img_lbp(img)
        lbp_hists.append(result)

    return lbp_hists
