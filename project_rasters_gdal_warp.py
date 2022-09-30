# this script was written by Daniel Clement -2022
# Python 3.9
"""
This script will re-project the rasters in the input directory.
"""

# do imports
import os
from glob import glob
from tqdm import tqdm

# set parameters
#################################################################################################
# the folder containing the rasters you want to mosaic together
raster_folder = r"C:\data\rasters"

# the raster file format of the input images
in_format = ".tif"

# EPSG of new projection
new_projection = 4326
#################################################################################################


def project_raster(in_raster, raster_format, out_projection):
    # create output mosaic name/path
    out_raster = in_raster.replace(f"{raster_format}", f"_prj{raster_format}")

    # create GDAL Warp command to project raster
    command = f"gdalwarp -t_srs EPSG:{out_projection} {in_raster} {out_raster}"

    # run the command
    os.system(command)


# make list of all rasters in the input folder
raster_list = glob(raster_folder + "/*{}".format(in_format))


for raster in tqdm(raster_list):
    project_raster(in_raster=raster,
                   raster_format=in_format,
                   out_projection=new_projection
                   )
