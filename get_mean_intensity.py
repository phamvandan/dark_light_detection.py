import cv2
import numpy as np
import os
# ori_dir = './data/dark'
# ori_dir = './data/normal'
ori_dir = './data/light'

intens = []

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
    intens.append(np.mean(L))

intens = np.array(intens)

print('Intensity=', np.mean(intens))