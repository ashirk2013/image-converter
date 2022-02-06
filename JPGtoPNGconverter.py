from logging import root
import sys, os
from PIL import Image

root_asset_dir = './assets'

# grab first and second arguments
n = len(sys.argv)
if (n < 3):
    raise ValueError('Requires 2 arguments')

from_folder = f'{root_asset_dir}/{sys.argv[1]}'
to_folder = f'{root_asset_dir}/{sys.argv[2]}'

# check if 2nd argument (folder) exists
if (not os.path.isdir(from_folder)):
    raise ValueError(f'first argument: {from_folder} -- not a valid directory')

if (not os.path.isdir(to_folder)):
    os.mkdir(to_folder)


# loop through 1st argument (folder)
# convert each image to png
# save to the new folder
for infile in os.listdir(from_folder):
    f, e = os.path.splitext(infile)
    outfile = to_folder + f + '.png'
    try:
        with Image.open(f'{from_folder}/{infile}') as img:
            img.save(outfile, 'png')
    except OSError:
            print('cannot convert', infile)