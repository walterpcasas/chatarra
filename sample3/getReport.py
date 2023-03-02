# Este arquivo só foi testado na Base P

import os
import re
import sys
import shutil

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from skimage.io import imread, imshow, show, imsave
from skimage.transform import rotate
from skimage import img_as_ubyte

flag = 0

try:
    inMnt = sys.argv[1]
    inMntRot = sys.argv[2]
    originMnt = sys.argv[3]
    outReport = sys.argv[4]
    flag = 1
except:
    print('Missing arguments')


if flag == 1:
    pass