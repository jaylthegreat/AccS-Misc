import os


# this simply runs the command that takes a single picture.
# this program could easily be modified to take pics in timed intervals


# 0c45:6300 was the address of the camera when i ran the lsusb command in terminal
# getRekt.jpg is simply the name of the image we save. it can be changed to whatever
os.system("fswebcam --input 0c45:6300 getRekt.jpg")