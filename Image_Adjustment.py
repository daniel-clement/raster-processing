# this script was written by Daniel Clement - 2022
"""
This script enables the adjustment of several image characteristics of the images in a folder. First, contrast
stretching is applied using cv2. Next, apply brightness and sharpening adjustments using Pillow.
"""

# do imports
import os
import numpy as np
import cv2
from tqdm import tqdm
from glob import glob
from PIL import ImageEnhance as ie
from PIL import Image

# set parameters
#######################################################################################################################
inDir = r"c:\data\Original_Images"
outDir = r"c:\data\Adjusted_Images"
inFormat = "jpg"  # "png" or "jpg"
outFormat = "jpg"  # "png" or "jpg"

# A brightness enhancement factor of 0.0 gives a black image. A factor of 1.0 gives the original image.
brightness_Factor = 2

# A sharpness enhancement factor of 0.0 gives a fully blured image. A factor of 1.0 gives the original image. And a
# factor of 2 gives a sharpened image.
sharpness_Factor = 2
#######################################################################################################################

# create a working folder where intermediate files will be created
workingDir = os.path.join(outDir, "contrastStretched")

if os.path.isdir(workingDir):
    pass
else:
    os.mkdir(workingDir)

# create the folder where the final adjusted images will be written to
finalDir = os.path.join(outDir, "Final")

if os.path.isdir(finalDir):
    pass
else:
    os.mkdir(finalDir)

# get a list of the input images
imgList = glob(inDir + "/*.{}".format(inFormat))


print("Applying contrast stretch...")
# loop through the original images and apply the CLAHE contrast stretching method
for i in tqdm(imgList):

    # read the image
    bgr = cv2.imread(i)

    # convert the color to LAB
    lab = cv2.cvtColor(bgr, cv2.COLOR_BGR2LAB)

    # split the image to process the 3 bands
    lab_planes = cv2.split(lab)

    # set the CLAHE parameters
    clahe = cv2.createCLAHE(clipLimit=4, tileGridSize=(16,16))

    # apply the CLAHE stretch to the image bands
    lab_planes[0] = clahe.apply(lab_planes[0])  # + 40

    # merge the bands back together
    lab = cv2.merge(lab_planes)

    # convert the LAB colorspace image back to RGB
    bgr = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

    # create output path
    outImg = os.path.join(workingDir, os.path.basename(i).replace(".tif", "_stretch{}".format(outFormat)))

    # write the processed image back out to the disk
    cv2.imwrite(outImg, bgr)


imgList2 = glob(workingDir + "/*{}".format(outFormat))

print("\nAdjusting brightness...")
# loop through stretched images and brighten them using PIL
for i in tqdm(imgList2):

    # open the image with PIL
    img = Image.open(i)

    # perform brightness adjustment
    img2 = ie.Brightness(img)
    manBrightImg = img2.enhance(brightness_Factor)

    # perform sharpness adjustment
    img3 = ie.Sharpness(manBrightImg)
    manSharpImg = img3.enhance(sharpness_Factor)

    # create output path
    outImg = os.path.join(finalDir, os.path.basename(i).replace("{}".format(outFormat), "_Final{}".format(outFormat)))

    # write image to disk
    if "jpg" in outFormat:
        manSharpImg.save(outImg, "JPEG")

    elif "tif" in outFormat:
        manSharpImg.save(outImg, "TIFF")

