# this script was written by Daniel Clement - 2022
# Python 3.9
"""
This script will re-project the rasters in the input directory.
"""

import os
from glob import glob

from tqdm import tqdm

# set parameters
##############################################################################
# the folder containing the rasters you want to mosaic together
raster_folder = r"C:\data\rasters"

# the raster file format of the input images
in_format = "tif"  # "tif" or "img"

# EPSG of new projection
new_projection = 4326
##############################################################################


def project_raster(
        in_raster: str,
        raster_format: str,
        out_projection: int
) -> None:
    """
    re-projects a raster to the desired output projection using GDAL Warp
    Args:
        in_raster: the path to the raster to project as a string
        raster_format: the format of the raster files as a string
        out_projection: the desired output projection's EPSG code as an int

    Returns:

    """
    # create output mosaic name/path
    out_raster = in_raster.replace(f"{raster_format}", f"_prj{raster_format}")

    # create GDAL Warp command to project raster
    command = f"gdalwarp -t_srs EPSG:{out_projection} {in_raster} {out_raster}"

    # run the command
    os.system(command)


def main():
    # make list of all rasters in the input folder
    raster_list = glob(raster_folder + f"/*{in_format}")

    # loop through the rasters in the input folder and project them
    for raster in tqdm(raster_list, desc="Projecting Rasters"):
        project_raster(in_raster=raster,
                       raster_format=in_format,
                       out_projection=new_projection
                       )


if __name__ == "__main__":
    main()
