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
    inImages = sys.argv[1]
    mntImages = sys.argv[2]
    predMnt = sys.argv[3]
    outImages = sys.argv[4]
    flag = 1
except:
    print('Missing arguments')


if flag == 1:

    if not os.path.exists(outImages):
        os.makedirs(outImages)

    imgs = os.listdir(inImages)
    imgs.sort()
    print('Minutiae of', len(imgs),'images')

    for number, img in enumerate(imgs):
        print('Image',number)
        name = re.split('-|\.', img)
        angle = name[2]
        prefix = name[0]+'-'+name[1]
        fileMnt = os.path.join(mntImages, prefix + '-seeds.txt')
        filePred = os.path.join(predMnt, prefix + '-'+angle+ '-seeds.txt')
        file = imread(os.path.join(inImages, img))


        # Minutiae Predict
        df_pred = pd.read_csv(filePred, delim_whitespace=True, header=None, skiprows=1)
        mntPred = np.zeros_like(file)
        for index, row in df_pred.iterrows():
            mntPred[int(row[1])][int(row[0])] = 1

        mask = mntPred > 0
        pointsPred = np.column_stack(np.where(mask))



        # Minutiae Input
        df = pd.read_csv(fileMnt, delim_whitespace=True, header=None, skiprows=1)

        
        mnt = np.zeros_like(file)

        for index, row in df.iterrows():
            mnt[row[1]][row[0]] = 1

        mntRot = rotate(mnt, int(angle))
        mask = mntRot > 0
        points = np.column_stack(np.where(mask))

        fig, ax = plt.subplots()
        ax.imshow(file, cmap='gray')
        ax.scatter(points[:,1], points[:,0], s=10, c='green', marker='*')
        ax.scatter(pointsPred[:,1], pointsPred[:,0], s=10, c='red', marker='*')
        ax.axis('off')
        plt.savefig(os.path.join(outImages, img))