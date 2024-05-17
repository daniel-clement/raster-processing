# this script was written by Daniel Clement
# Python 3.9
"""
this script will adjust the input images (JPEG, PNG, TIFF)
contrast and brightness
"""

import os
from glob import glob

from PIL import Image
from PIL import ImageEnhance as ie
from tqdm import tqdm

# Input Parameters
##############################################################################
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
# A factor of 1.0 gives the original image. And a factor of 2 gives a
# sharpened image.
sharpness_Factor = 1.5

# the file format of the input images
input_format = "jpg"  # "jpg" or "tif" or "png"

# the file format you want the output images to be
output_format = "tif"  # "jpg" or "tif" or "png"
##############################################################################


def adjustment_process(
        input_image: str,
        contrast_factor: float,
        brightness_factor: float,
        sharpness_factor: float,
        out_dir: str,
):
    """
    Processes the images using the user defined input parameters
    and outputs an adjusted image.

    Args:
        input_image: the path to the input image as a string
        contrast_factor: the contrast factor to adjust the image by
        brightness_factor: the brightness factor to adjust the image by
        sharpness_factor: the sharpness factor to adjust the image by
        out_dir: the output folder where you want the adjusted images saved

    Returns:
        None
    """

    # open the image with PIL
    img = Image.open(input_image)

    # perform the contrast adjustment
    obj = ie.Contrast(img)
    manual_contrast_img = obj.enhance(contrast_factor)

    # perform brightness adjustment
    obj2 = ie.Brightness(manual_contrast_img)
    man_bright_img = obj2.enhance(brightness_factor)

    # perform sharpness adjustment
    obj3 = ie.Sharpness(man_bright_img)
    man_sharp_img = obj3.enhance(sharpness_factor)

    # create output path
    # get the input image name
    in_file_name = os.path.basename(input_image)

    # create the output files name by adding "_adjusted" to the end of the
    # input file's name, and make the file format equal the output_format param
    out_file_name = in_file_name.replace(
        f".{input_format}",
        f"_adjusted.{output_format}"
    )

    # join the output folder and the output file
    # name to create the output file path
    out_img = os.path.join(out_dir, out_file_name)

    # write the adjusted image to the disk
    man_sharp_img.save(out_img)


def main():
    # get list of all images in inDir
    in_imgs = glob(inDir + f"/*.{input_format}")

    # for image in inImgs list, adjust images, and save the outputs
    for image in tqdm(in_imgs):
        # run the adjustment processor function on the image
        adjustment_process(input_image=image,
                           contrast_factor=contrast_Factor,
                           brightness_factor=brightness_Factor,
                           sharpness_factor=sharpness_Factor,
                           out_dir=outDir)

    # use glob to get a list of all the output images
    out_imgs = glob(outDir + f"/*.{output_format}")

    # use the len function to get the number of files in the outImgs list
    num_out_imgs = len(out_imgs)

    # use the len function to get the number of files in the inImgs list
    num_imgs = len(in_imgs)

    # ensure the number of output images matches the number of input images
    if num_imgs == num_out_imgs:
        print("All images processed successfully!!!")
    elif num_imgs > num_out_imgs:
        print("ERROR - All images not processed successfully :'(")


if __name__ == "__main__":
    main()
