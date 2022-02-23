# This script was written by Daniel Clement - 2021
# Python 3.7
"""
this script will make a VRT from all of the rasters inside of a folder, even if they are in sub-folders.
"""

# do imports
import os
import glob2 as glob
import gdal

#######################################################################################################################
# folder with the raster files
inDir = r"C:\data\images"

# output VRT file
outVrt = r"C:\data\images\example.vrt"

# input raster format - acceptable formats can be found at the following link: https://gdal.org/drivers/raster/index.html
inImgFormat = "tif"  # "tif" or "img"
#######################################################################################################################


# get path of all tifs in the sub-folders of the inDir
rasterList = glob.glob(r"{}\**\*.{}".format(inDir, inImgFormat))

print("\nFound {} rasters...".format(len(tifList)))

# create txt file with list of tifs in input folder
outTxt = os.path.join(inDir, "ImageList.txt")
with open(outTxt, 'w') as f:
    for raster in rasterList:
        f.write("{}\n".format(raster))

# create a vrt from the tifs in the outTxt file
print("\nCreating VRT...")
# create the command for the gdal build vrt process
command = 'gdalbuildvrt "{}" -input_file_list {}'.format(outVrt, outTxt)

# run the gdal build vrt command
os.system(command)

print("\nVRT Created Successfully!")
