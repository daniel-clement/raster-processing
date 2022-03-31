# this script was written by Daniel Clement
# Python-3
"""
this script will adjust the input images (JPEG, PNG, TIFF) contrast and brightness
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
inDir = r"c:\data\original_images"

# the folder where you want your processed images to be saved to
outDir = r"c:\data\adjusted_images"

# A contrast enhancement factor of 0.0 gives a solid grey image. 
# A factor of 1.0 gives the original image.
contrast_Factor = 1.5

# A brightness enhancement factor of 0.0 gives a black image. 
# A factor of 1.0 gives the original image.
brightness_Factor = 1.5

# A sharpness enhancement factor of 0.0 gives a fully blured image. 
# A factor of 1.0 gives the original image. And a factor of 2 gives a sharpened image.
sharpness_Factor = 1.5

# the file format of the input images
input_format = "jpg"  # "jpg" or "tif" or "png"

# the file format you want the output images to be
output_format = "tif"  # "jpg" or "tif" or "png"
#######################################################################################################################


def adjustment_process(input_image, contrast_factor, brightness_factor, sharpness_factor, out_dir):
    """
    This funtion processes the images using the user defined input parameters and outputs an adjusted image.
    :param input_image: the input image
    :param contrast_factor: the contrast factor to adjust the image by
    :param brightness_factor: the brightness factor to adjust the image by
    :param sharpness_factor: the sharpness factor to adjust the image by
    :param out_dir: the output folder where you want the adjusted images written to
    :return:
    """

   # open the image with PIL
    img = Image.open(input_image)

    # perform the contrast adjustment
    obj = ie.Contrast(img)
    manualContrastImg = obj.enhance(contrast_factor)

    # perform brightness adjustment
    obj2 = ie.Brightness(manualContrastImg)
    manBrightImg = obj2.enhance(brightness_factor)

    # perform sharpness adjustment
    obj3 = ie.Sharpness(manBrightImg)
    manSharpImg = obj3.enhance(sharpness_factor)

    # create output path
    # get the input image name
    inFileName = os.path.basename(input_image)

    # create the output files name by adding "_adjusted" to the end of the input file's name,
    # and make the file format equal the output_format parameter
    outFileName = inFileName.replace(".{}".format(input_format), 
                                     "_adjusted.{}".format(output_format))

    # join the output folder and the output file name to create the output file path
    outImg = os.path.join(out_dir, outFileName)

    # write the adjusted image to the disk
    manSharpImg.save(outImg)


# get list of all images in inDir
inImgs = glob(inDir + "/*.{}".format(input_format))

# for image in inImgs list, adjust images, and save the outputs
for image in tqdm(inImgs):

    # run the adjustment processor function on the image
    adjustment_process(input_image=image, 
                       contrast_factor=contrast_Factor, 
                       brightness_factor=brightness_Factor, 
                       sharpness_factor=sharpness_Factor, 
                       out_dir=outDir)

# use glob to get a list of all of the output images
outImgs = glob(outDir + "/*.{}".format(output_format))

# use the len function to get the number of files in the outImgs list
numOutImgs = len(outImgs)

# use the len function to get the number of files in the inImgs list
numImgs = len(inImgs)

# ensure the number of output images matches the number of input images
if numImgs == numOutImgs:
    print("All images processed successfully!!!")
elif numImgs > numOutImgs:
    print("ERROR - All images not processed successfully :'(")
