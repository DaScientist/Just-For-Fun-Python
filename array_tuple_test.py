import numpy as np
from time import sleep
import random
global toggle_num
toggle_num = -1
max_number_of_cameras = 2


def toggle_camera():
    global toggle_num
    toggle_num = (toggle_num + 1) % max_number_of_cameras


i = 2
cams = [np.zeros((2, 2), np.uint8), np.ones((2, 2), np.uint8)]

while True:
    toggle_camera()
    print(toggle_num)
    cams[toggle_num] = np.ones((2, 2), np.uint8) * i
    print(np.concatenate(cams, axis=1))
    sleep(0.5)
    i = i+1
