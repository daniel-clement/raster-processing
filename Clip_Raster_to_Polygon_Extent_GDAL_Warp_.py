# this script was written by Daniel Clement - 2021
"""
This script will use GDAL Warp to clip a raster dataset to the extent of a polygon feature
"""

# do imports
import os
import gdal
import time

# set parameters
########################################################################################################################
# the raster you want to clip
in_raster = r"C:\data\example.tif"

# the polygon feature you want to clip the raster to - ShapeFile or Feature Class
clip_feature = r"C:\data\aoi_polygon.shp"

# the output clipped raster
out_raster = r"C:\data\example_clipped.tif"
########################################################################################################################

# Start time measurement
startTime = time.time()


def clip_raster(clip_feature, in_raster, out_raster):
    """
    This function will create and execute a GDAL Warp command with the given inputs
    """
    
    print("Clipping raster...")
    
    # creates the gdal warp command
    command = f"gdalwarp -dstnodata NoData -cutline {clip_feature} {in_raster} {out_raster}"

    # runs the command
    os.system(command)


# run the clip_raster function
clip_raster(clip_feature, in_raster, out_raster)

# stop the timer and calculate run time
executionTimeSec = (time.time() - startTime)


def print_execution_time(executionTimeSec):
    """
    This function calculates and prints the time it took the script processing to complete
    """
    if executionTimeSec < 60:
        execTimeSecRound = round(executionTimeSec, 2)
        print("Process completed in {} second(s)".format(execTimeSecRound))
    elif 60 <= executionTimeSec < 3600:
        execTimeMin = executionTimeSec / 60
        execTimeMinRound = int(execTimeMin)
        execTimeMinRemain = round(executionTimeSec % 60)
        print("Process completed in {} min {} sec".format(execTimeMinRound, execTimeMinRemain))
    elif executionTimeSec >= 3600:
        execTimeHours = executionTimeSec / 3600
        execTimeHoursRound = int(execTimeHours)
        execTimeHoursRemain = round((executionTimeSec % 3600) / 60)
        print("Process completed in {} hour(s) {} min.".format(execTimeHoursRound, execTimeHoursRemain))



print("\n##################################################################################################")
print("Raster successfully clipped!")
print_execution_time(executionTimeSec)
print(f"Please find your result at: {out_raster}")
print("##################################################################################################")
