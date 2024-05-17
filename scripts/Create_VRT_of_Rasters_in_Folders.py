# This script was written by Daniel Clement - 2021
# Python 3.7
"""
this script will make a VRT from all the rasters inside a folder,
even if they are in sub-folders.
"""

# do imports
import os
from pathlib import Path

##############################################################################
# folder with the raster files
in_dir = r"C:\data\images"

# input raster format - acceptable formats can be
# found here: https://gdal.org/drivers/raster/index.html
in_format = "tif"  # "tif" or "img"


##############################################################################


def make_vrt_of_rasters(input_folder: str, raster_format: str) -> str:
    """
    Makes a VRT from the raster files matching the input format in the input
    folder
    Args:
        input_folder: the path to the folder with the rasters as a string
        raster_format: the file format of the rasters

    Returns:
        the path to the output VRT file as a string
    """
    # get path of all tifs in the sub-folders of the inDir
    raster_list = [
        str(raster) for
        raster in
        Path(input_folder).rglob(f"*/*.{raster_format.lower()}")
    ]

    print(f"\nFound {len(raster_list)} rasters...")

    # create txt file with list of tifs in input folder
    out_txt = os.path.join(in_dir, "ImageList.txt")
    with open(out_txt, 'w') as f:
        for raster in raster_list:
            f.write("{}\n".format(raster))

    # create a vrt from the tifs in the outTxt file
    print("\nCreating VRT...")

    out_vrt = str(Path(input_folder) / "mosaic.vrt")

    # create the command for the gdal build vrt process
    command = f'gdalbuildvrt "{out_vrt}" -input_file_list {out_txt}'

    # run the gdal build vrt command
    os.system(command)

    return out_vrt


def main():
    # make the vrt
    out_vrt = make_vrt_of_rasters(
        input_folder=in_dir,
        raster_format=in_format,
    )

    # check to ensure the vrt was actually created
    if not os.path.isfile(out_vrt):
        print("\nVRT Creation Unsuccessful :(")

    else:
        print("VRT Created Successfully! Please find your result at:")
        print(out_vrt)


if __name__ == "__main__":
    main()
