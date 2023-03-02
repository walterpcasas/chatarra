import os
import sys

from skimage.io import imread, imshow, show, imsave
from skimage.transform import rotate
from skimage import img_as_ubyte

flag = 0

try:
    inImages = sys.argv[1]
    maskImages = sys.argv[2]
    outImages = sys.argv[3]
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
        print(img)
        file = imread(os.path.join(inImages, img))
        mask = imread(os.path.join(maskImages, img))
        print(file.shape)
        print(mask.shape)

        sgmnt = file * mask
        imsave(os.path.join(outImages, img), img_as_ubyte(sgmnt))
        