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
            result = np.sum(lbp)
            lbp_index.append(result)
    
    return lbp_index

# Function to return LBP descriptors and histogram data
def ICV_img_lbp_hist(images):
    # Loop through image windows and plot the LBP Histograms
    lbp_data = []
    lbp_hists = []
    for img in images:
        result = ICV_img_lbp(img)
        # Numpy histogram function will return the data set using 256 bins representative of each RGB value
        (hist, _) = np.histogram(result, bins=256)
        lbp_hists.append(hist)
        lbp_data.append(result)

    return (lbp_data, lbp_hists)


def ICV_img_global_desc(descriptors):
    global_desc = []
    for desc in descriptors:
        global_desc.append(desc)
    return global_desc


def ICV_plot_figs(figures, img_name):
    x = np.arange(256)
    plt.figure(figsize=(12, 12))
    fig, axs = plt.subplots(3, 3)
    axs[0, 0].bar(x, figures[0])
    axs[0, 1].bar(x, figures[1])
    axs[0, 2].bar(x, figures[2])
    axs[1, 0].bar(x, figures[3])
    axs[1, 1].bar(x, figures[4])
    axs[1, 2].bar(x, figures[5])
    axs[2, 0].bar(x, figures[6])
    axs[2, 1].bar(x, figures[7])
    axs[2, 2].bar(x, figures[8])

    # Save the histograms
    plt.savefig(fname=f'../../output/cw4/{img_name}_lbp_hists.png')

def ICV_plot_windows(windows, img_name):
    # Plot equally divided shapes
    fig, axs = plt.subplots(3, 3)
    axs[0, 0].imshow(windows[0], cmap="gray")
    axs[0, 1].imshow(windows[1], cmap="gray")
    axs[0, 2].imshow(windows[2], cmap="gray")
    axs[1, 0].imshow(windows[3], cmap="gray")
    axs[1, 1].imshow(windows[4], cmap="gray")
    axs[1, 2].imshow(windows[5], cmap="gray")
    axs[2, 0].imshow(windows[6], cmap="gray")
    axs[2, 1].imshow(windows[7], cmap="gray")
    axs[2, 2].imshow(windows[8], cmap="gray")
    plt.savefig(fname=f'../../output/cw4/{img_name}_windows.png')