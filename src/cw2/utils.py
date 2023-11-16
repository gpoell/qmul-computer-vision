import numpy as np

# Task A: Code a function that takes an input image, performs convolution with a given kernel, and returns the 
# resulting image

def ICV_mtrx_convolution(image, conv_kernel):

    # Create the new image canvas
    image_x = len(image[:,0])
    image_y = len(image[0,:])
    canvas = np.zeros((image_x, image_y))

    # Determine the sum of the convolution kernel to be used for the convolution calculation
    conv_kernel_sum = np.sum(np.abs(conv_kernel))
    # If the kernel sum is zero then set it to 1 to avoid calculation error
    if conv_kernel_sum == 0:
        conv_kernel_sum = 1

    # The length of the convolution kernel determines the pixel kernel to process
    cv_x = int(np.shape(conv_kernel)[0])

    # Loop through image pixels to perform the convolution
    for i in range(image_x):

        # Skip the borders
        if i == image_x-cv_x:
            break
        
        for j in range(image_y):

            # Skip the borders
            if j == image_y-cv_x:
                break
            # Define the image kernel size based on the size of the convolution kernel
            image_kernel = image[i:i+cv_x, j:j+cv_x]
            
            # Determine the Convolution Result (the sum of the product of each pixel)
            conv_result = np.sum(conv_kernel * image_kernel)
            # print(image[i, j])
            result = conv_result / conv_kernel_sum
            # result = math.floor((np.sum(result)) * (1/np.sum(np.absolute(conv_kernel)))) # Issue here with one kernel - its sum is ZERO
            canvas[i, j] = result

    return canvas
