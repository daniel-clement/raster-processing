# this script was written by Daniel Clement -2022
# Python 3.9
"""
This script will mosaic all the rasters in the input directory.
"""

# do imports
import os
from glob import glob
from pathlib import Path

# set parameters
##############################################################################
# the folder containing the rasters you want to mosaic together
input_folder = r""

# the raster file format of the input images
in_format = "tif"  # "tif" or "img"
##############################################################################


def make_mosaic(input_dir: str, raster_format: str) -> str:
    """
    Makes a mosaicked raster from the rasters in the input folder
    using GDAL Warp
    Args:
        input_dir: the path to the input folder as a string
        raster_format: the file format of the input rasters as a string

    Returns:
        the path to the mosaicked raster as a string
    """
    # make list of all rasters in the input folder
    img_list = [raster for raster in glob(input_dir + f"/*.{raster_format}")]

    # make string from inImgs list
    in_img_string = " ".join(img_list)

    # create output mosaic name/path
    out_mosaic_path = Path(input_dir) / f"mosaic.{input_dir}"

    # create GDAL Warp command to merge rasters
    cmd = "gdalwarp " \
          "-co COMPRESS:LZW " \
          "-co TILED=YES " \
          f"{in_img_string} " \
          f"{out_mosaic_path}"

    # run the command
    os.system(cmd)

    return str(out_mosaic_path)


def main():
    # run the command
    print("Creating mosaic...")
    out_file = make_mosaic(input_dir=input_folder, raster_format=in_format)

    # check to ensure the vrt was actually created
    if not os.path.isfile(out_file):
        print("\nMosaic Creation Unsuccessful :(")

    else:
        print("Mosaic Created Successfully! Please find your result at:")
        print(out_file)


if __name__ == "__main__":
    main()
