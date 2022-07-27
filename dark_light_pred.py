import cv2
import numpy as np
import os
ori_dir = './data/dark'

def img_estim(img, low_thrshld, hight_thrshld):
    mean_inten = np.mean(img)
    print('Intensity=', mean_inten)
    is_light = mean_inten > hight_thrshld
    if is_light:
        return 'light'
    is_dark = mean_inten < low_thrshld
    if is_dark:
        return 'dark'
    return 'normal'

filenames = os.listdir(ori_dir)
THRESH = 127
DIM = 64
for filename in filenames:
    image = cv2.imread(os.path.join(ori_dir, filename))
    # Resize image for fast computing
    image = cv2.resize(image, (DIM, DIM))
    # Convert color space to LAB format and extract L channel
    # L*: Lightness
    # a*: Red/Green Value
    # b*: Blue/Yellow Value
    L, A, B = cv2.split(cv2.cvtColor(image, cv2.COLOR_BGR2LAB))
    print(L.shape)
    print(img_estim(L, THRESH))
    