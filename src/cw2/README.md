### CW2: Convolution
Convolution provides a way of multiplying two arrays to produce a third array. Depending on the designed
filter and the intended effect, the kernel can be a matrix of dimensions, for example, 3x3, 5x5 or 7x7.

a. Code a function that takes an input image, performs convolution with a given kernel, and returns the
resulting image.

b. Design a convolution kernel that computes, for each pixel, the average intensity value in a 3x3 region.
Use this kernel and the filtering function above, and save the resulting image.

c. Use the kernels provided below, apply the filtering function and save the resulting images. Comment
on the effect of each kernel.
kernel A
1   2   1
2   4   2
1   2   1
kernel B
0   1   0
1  -4   1
0   1   0
d. Use the filtering function for the following filtering operations: (i) A followed by A; (ii) A followed by B;
(iii) B followed by A. Comment the results.

