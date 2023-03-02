import os
import sys
import shutil

from skimage.io import imread, imshow, show, imsave
from skimage.transform import rotate
from skimage import img_as_ubyte

flag = 0

try:
    inImages = sys.argv[1]
    outImages = sys.argv[2]
    # numAngles = sys.argv[3]
    flag = 1
except:
    print('Missing arguments')


if flag == 1:

    if not os.path.exists(outImages):
        os.makedirs(outImages)

    imgs = os.listdir(inImages)
    imgs.sort()
    print('Rotation of', len(imgs),'images')

    for number, img in enumerate(imgs):
        print('Image',number)
        file = imread(os.path.join(inImages, img))
        for angle in range(0, 360, 80):
            rotImg = rotate(file, angle)
            sufix = '-'+ str(angle)+'.'
            imsave(os.path.join(outImages, img.replace('.', sufix)), img_as_ubyte(rotImg))