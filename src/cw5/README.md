### CW5: Object Counting
Moving objects captured by fixed cameras are the focus of several computer vision applications.

a. Write a function that performs pixel-by-pixel frame differencing using, as reference frame, the first
frame of an image sequence. Apply a classification threshold and save the results.

b. Repeat the exercise using the previous frame as reference frame (use frame It-1 as reference frame
for frame It, for each t). Comment the results in the report.

c. Write a function that generates a reference frame (background) for the sequence using for example
frame differencing and a weighted temporal averaging algorithm.

d. Write a function that counts the number of moving objects in each frame of a sequence. Generate a
bar plot that visualizes the number of objects for each frame of the whole sequence. Discuss in the
report the implemented solution, including advantages and disadvantages.