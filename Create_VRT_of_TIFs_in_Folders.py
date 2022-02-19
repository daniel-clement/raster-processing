# This script was written by Daniel Clement - 2021
# Python 3.7
"""
this script will make a VRT from all of the images inside of a folder, even if they are in sub-folders.
"""

# do imports
import os
import glob2 as glob
import gdal

#######################################################################################################################
# folder with the tif files
inDir = r""

# output VRT file
outVrt = r""

# input image format
inImgFormat = "tif"  # "tif" or "img"
#######################################################################################################################


# get path of all tifs in the sub-folders of the inDir
tifList = glob.glob(r"{}\**\*.{}".format(inDir, inImgFormat))

print("\nFound {} images...".format(len(tifList)))

# create txt file with list of tifs in input folder
outTxt = os.path.join(inDir, "ImageList.txt")
with open(outTxt, 'w') as f:
    for tif in tifList:
        f.write("{}\n".format(tif))

# create a vrt from the tifs in the outTxt file
print("\nCreating VRT...")
# create the command for the gdal build vrt process
command = 'gdalbuildvrt "{}" -input_file_list {}'.format(outVrt, outTxt)

# run the gdal build vrt command
os.system(command)

print("\nVRT Created Successfully!")
