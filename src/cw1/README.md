### CW1: Transformations
Rotation, translation and skew are useful operations for matching, tracking, and data augmentation.

a. Write a function that takes as input an image I, rotates it by an angle θ1 and horizontally skews it by
an angle, θ2. Write the matrix formulation for image rotation R(.) and skewing S(.). Define all the
variables. Note that the origin of the coordinate system of the programming environment you use
might be different from the one shown in the lectures.

b. Create an image that contains your name written in Arial, point 72, capital letters. Rotate clockwise
the image you created by 30, 60, 120 and -50 degrees. Skew the same image by 10, 40 and 60
degrees. Complete the process so that all the pixels have a value. Discuss in the report the
advantages and disadvantages of different approaches.

c. Analyse the results when you change the order of the two operators: R(S(I)) and S(R(I)).
i. Rotate the image by θ1 = 20 clockwise and then skew the result by θ2 = 50.
ii. Skew the image by θ2 = 50 and then rotate the result by θ1 = 20 clockwise.
Are the results of (i) and (ii) the same? Why?
