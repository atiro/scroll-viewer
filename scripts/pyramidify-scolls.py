import os
import pathlib

ORIGINAL_DIR="../data/images"
PYRAMID_DIR="images"


for root,dirs,files in os.walk(ORIGINAL_DIR):
    os.chdir(ORIGINAL_DIR)
    for dir in dirs:
      pathlib.Path(f"../../{PYRAMID_DIR}/{dir}/").mkdir(parents=True, exist_ok=True)
      if dir.startswith("2023"):
        print(f"Processing directory {dir}\n")
        os.chdir(dir)
        os.system("for filename in *.tif; do vips tiffsave $filename ${filename%.*} --compression=jpeg --Q=90 --tile --tile-width=256 --tile-height=256 --pyramid; done")
        os.system(f"mv 64 ../../../{PYRAMID_DIR}/{dir}/")
        os.chdir("..")
        print(f"Processed\n")
