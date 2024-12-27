### CW4: Texture Classification
The Local Binary Pattern (LBP) operator describes the surroundings of a pixel by generating a bit-code
from the binary derivatives of a pixel.

a. Write a function that divides a greyscale image into equally sized non-overlapping windows and
returns the feature descriptor for each window as distribution of LBP codes. For each pixel in the
window, compare the pixel to each of its 8 neighbours. Convert the resulting bit-codes (base 2) to
decimals (base 10 numbers) and compute their histogram over the window. Normalize the histogram
(which is now a feature descriptor representing the window). Show in the report the resulting images.

b. Come up with a descriptor that represents the whole image as consisting of multiple windows. For
example, you could combine several local descriptions into a global description by concatenation.
Discuss in the report alternative approaches. Using the global descriptor you created, implement a
classification process that separates the images in the dataset into two categories: face images and
non-face images (for example, you could use histogram similarities). Comment the results in the
report. Is the global descriptor able to represent whole images of different types (e.g. faces vs. cars)?
Identify problems (if any), discuss them in the report and suggest possible solutions.

c. Decrease the window size and perform classification again. Comment the results in the report.

d. Increase the window size and perform classification again. Comment the results in the report.

e. Discuss how LBP can be used or modified for the analysis of dynamic textures in a video.