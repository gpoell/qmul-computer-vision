# ECS709P Computer Vision
Author: Garrett Poell (230460269)  
Email: g.poell@se23.qmul.ac.uk


### Python Dependencies
* Python - 3.11.2
* OpenCV - 4.8.1.78 (4.8 latest)
* Matplotlib - 3.8.0
* Numpy (latest)

### INSTRUCTIONS
Inside of the src/ directory are folders for each coursework task that contain a jupyternotebook called main.ipynb and a utils.py that contain all of the related functions for that task. The main.ipynb are the only files that need to be executed and you can run them from the top. The files will source the images and video from the data/ directory structure and the output (images and graphs) will be mapped to the corresponding output/ directories outlined below. All of the scripts should source images and videos from the given Datasets, but if you want to change them then you will need to update the lines of code near the top where the paths are declared.

1. Install dependencies (latest versions should all be fine)
2. Copy in Datasets (DatasetA, DatasetB, DatasetC, etc..) to the data/ directory and ensure it maps the same as below
3. Run the main.ipynb for the given task (cw1, cw2, etc..)
4. Validate any output in the output/ directory


### Folder Structure
> data  
    > DatasetA  
        car-1.jpg  
        car-2.jpg  
        car-3.jpg  
        face-1.jpg  
        face-2.jpg  
        face-3.jpg  
    cw1_b.png  
    DatasetB.avi  
    DatasetC.avi  
    DatasetC.mpg  
    test.jpg  
> output  
    > cw1  
    > cw2  
    > cw3  
        > figures  
        > video_out  
    > cw4  
    > cw5  
        > frame_diff  
        > video_out  
> src  
    > cw1  
        main.ipynb  
        utils.py  
    > cw2  
        main.ipynb  
        utils.py  
    > cw3  
        main.ipynb  
        utils.py  
    > cw4  
        main.ipynb  
        utils.py  
    > cw5  
        main.ipynb  
        utils.py  
