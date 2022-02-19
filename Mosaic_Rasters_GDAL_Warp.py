# this script was written by Daniel Clement -2022
# Python 3.7
"""
This script will mosaic all the rasters in the input directory.
"""

# do imports
import os
from glob import glob
import gdal

# set parameters
#################################################################################################
# the folder containing the rasters you want to mosaic together
inDir = r""

# the raster file format of the input images
inFormat = ".tif"
#################################################################################################

# make list of all rasters in the input folder which dont include the word "BROWSE" in the name
inImgs = [i for i in glob(inDir + "/*{}".format(inFormat)) if not 'BROWSE' in i]

# make string from inImgs list
inImgsString = " ".join(inImgs)

# create output mosaic name/path
outTif = inImgs[0][:-8] + "Mosaic{}".format(inFormat)

# create GDAL Warp command to merge rasters
command = "gdalwarp -co COMPRESS:LZW -co TILED=YES {} {}".format(inImgsString, outTif)

# run the command
print("Creating mosaic...")
os.system(command)
print("Mosaic created successfully!")
