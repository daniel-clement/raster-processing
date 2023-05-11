# This script was written by Daniel Clement - 2021
# Python 3.7
"""
this script will make a VRT from all of the rasters inside of a folder, even if they are in sub-folders.
"""

# do imports
import os
from pathlib import Path

#######################################################################################################################
# folder with the raster files
in_dir = r"C:\data\images"

# output VRT file
out_vrt = r"C:\data\images\example.vrt"

# input raster format - acceptable formats can be found here: https://gdal.org/drivers/raster/index.html
in_format = "tif"  # "tif" or "img"
#######################################################################################################################


# get path of all tifs in the sub-folders of the inDir
raster_list = [str(raster) for raster in Path(in_dir).rglob(f"*/*.{in_format.lower()}")]

print(f"\nFound {len(raster_list)} rasters...")

# create txt file with list of tifs in input folder
out_txt = os.path.join(in_dir, "ImageList.txt")
with open(out_txt, 'w') as f:
    for raster in raster_list:
        f.write("{}\n".format(raster))

# create a vrt from the tifs in the outTxt file
print("\nCreating VRT...")

# create the command for the gdal build vrt process
command = f'gdalbuildvrt "{out_vrt}" -input_file_list {out_txt}'

# run the gdal build vrt command
os.system(command)

# check to ensure the vrt was actually created
if not os.path.isfile(out_vrt):
    print("\nVRT Creation Unsuccessful :(")

else:
    print("VRT Created Successfully!")
