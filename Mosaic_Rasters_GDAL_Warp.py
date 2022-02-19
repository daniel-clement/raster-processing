# this script was written by Daniel Clement -2022

# do imports
import os
from glob import glob

#######################################################################################################################
# set parameters
inDir = r"O:\Analytics\Mexico\PRC_Yucatan_2022\Working\Dan\Imagery\DosBocas_GE1_7_11_2021"
inFormat = ".tif"
#######################################################################################################################

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
