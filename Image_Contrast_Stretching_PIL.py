# this script was written by Daniel Clement
# Python-3
"""
this script will adjust the input images (JPEG) contrast and brightness using the PIL- Image Enhance module
"""

# do imports
import os
from glob import glob
from PIL import ImageEnhance as ie
from PIL import Image
from tqdm import tqdm

# Input Parameters
#######################################################################################################################
# the folder with the images you want to process
inDir = r""

# the folder where you want your processed images to be saved to
outDir = r""

# A contrast enhancement factor of 0.0 gives a solid grey image. A factor of 1.0 gives the original image.
contrast_Factor = 2

# A brightness enhancement factor of 0.0 gives a black image. A factor of 1.0 gives the original image.
brightness_Factor = 2

# A sharpness enhancement factor of 0.0 gives a fully blured image. A factor of 1.0 gives the original image. And a
# factor of 2 gives a sharpened image.
sharpness_Factor = 2
#######################################################################################################################

# get list of all images in inDir
inImgs = glob(inDir + "/*.jpg")
numImgs = len(inImgs)

# for image in inImgs list, adjust images, and save the outputs
for i in tqdm(inImgs):

    # open the image with PIL
    img = Image.open(i)

    obj = ie.Contrast(img)
    manualContrastImg = obj.enhance(contrast_Factor)

    # perform brightness adjustment
    obj2 = ie.Brightness(manualContrastImg)
    manBrightImg = obj2.enhance(brightness_Factor)

    # perform sharpness adjustment
    obj3 = ie.Sharpness(manBrightImg)
    manSharpImg = obj3.enhance(sharpness_Factor)

    # create output path
    outImg = os.path.join(outDir, os.path.basename(i).replace(".jpg", "_adjusted.jpg"))

    # write image to disk
    manSharpImg.save(outImg, "JPEG")

# get number of images processed and output
outImgs = glob(outDir + "/*.jpg")
numOutImgs = len(outImgs)

# soft error handling to make sure all input images were processed
if numImgs == numOutImgs:
    print("All images processed successfully!!!")
else:
    print("ERROR - All images not processed successfully :'(")
