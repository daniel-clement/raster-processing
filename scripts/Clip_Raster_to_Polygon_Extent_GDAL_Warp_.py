# this script was written by Daniel Clement - 2021
# Python 3.9
"""
This script will use GDAL Warp to clip a raster dataset to the extent of a polygon feature
"""

import os
from pathlib import Path

# set parameters
########################################################################################################################
# the raster you want to clip
in_raster = r"C:\data\example.tif"

# the polygon feature you want to clip the raster to - ShapeFile or Feature Class
clip_feature = r"C:\data\aoi_polygon.shp"
########################################################################################################################

# Start time measurement
startTime = time.time()


def clip_raster(clip_polygon: str, raster: str) -> str:
    """
    Clips a raster using GDAL Warp to the extent of an input polygon file
    Args:
        clip_polygon: The path to the clipping polygon file as a string
        raster: the path to the raster to clip as a string

    Returns:
        the path to the output clipped raster as a string
    """

    
    print("Clipping raster...")

    # create output raster name and path
    raster_path = Path(raster)
    out_raster = raster.replace(
        raster_path.suffix,
        f"_Clipped{raster_path.suffix}"
    )

    # creates the gdal warp command
    command = "gdalwarp " \
              "-dstnodata NoData " \
              f"-cutline {clip_polygon} " \
              f"{raster} " \
              f"{out_raster}"

    # runs the command
    os.system(command)

    return str(raster_path)


def main():
    # run the clip_raster function
    out_clipped_raster = clip_raster(clip_feature, in_raster)

    # check to ensure the vrt was actually created
    if not os.path.isfile(out_clipped_raster):
        print("\nProcess Unsuccessful :(")

    else:
        print("Raster Clipped Successfully! Please find your result at:")
        print(out_clipped_raster)

if __name__ == "__main__":
    main()
