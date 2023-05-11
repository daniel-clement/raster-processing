# this script was written by Daniel Clement - 2021
"""
This script will use GDAL Warp to clip a raster dataset to the extent of a polygon feature
"""

# do imports
import os
import time
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


def clip_raster(clip_polygon: str, raster: str) -> None:
    """
    This function will create and execute a GDAL Warp command with the given inputs
    """
    
    print("Clipping raster...")

    # create output raster name and path
    raster_path = Path(raster)
    out_raster = raster.replace(raster_path.suffix, f"_Clipped{raster_path.suffix}")

    # creates the gdal warp command
    command = f"gdalwarp -dstnodata NoData -cutline {clip_polygon} {raster} {out_raster}"

    # runs the command
    os.system(command)


# run the clip_raster function
clip_raster(clip_feature, in_raster)

# stop the timer and calculate run time
executionTimeSec = (time.time() - startTime)


def print_execution_time(execution_time_sec: float):
    """
    This function calculates and prints the time it took the script processing to complete
    """
    if execution_time_sec < 60:
        execTimeSecRound = round(execution_time_sec, 2)
        print("Process completed in {} second(s)".format(execTimeSecRound))
    elif 60 <= execution_time_sec < 3600:
        execTimeMin = execution_time_sec / 60
        execTimeMinRound = int(execTimeMin)
        execTimeMinRemain = round(execution_time_sec % 60)
        print("Process completed in {} min {} sec".format(execTimeMinRound, execTimeMinRemain))
    elif execution_time_sec >= 3600:
        execTimeHours = execution_time_sec / 3600
        execTimeHoursRound = int(execTimeHours)
        execTimeHoursRemain = round((execution_time_sec % 3600) / 60)
        print("Process completed in {} hour(s) {} min.".format(execTimeHoursRound, execTimeHoursRemain))


print("\n##################################################################################################")
print("Raster successfully clipped!")
print_execution_time(executionTimeSec)
print("##################################################################################################")
