import requests
import os
from time import sleep
from pathlib import Path

# You need to set this after you have registered for the competition here
#  https://scrollprize.org/data
USERNAME = ""
PASSWORD = ""

IMAGES_DIR="../data/images"


segments = []

# Lazily hardcoded the list for the moment

with open("scroll1.paths.txt") as segment_list:
    for line in segment_list:
        segments.append(line.strip())

for segment in segments:
  print(f"Retrieving segment {segment}")

  Path(f"{IMAGES_DIR}/{segment}").mkdir(parents=True, exist_ok=True)

  retrieved = False

  for layer in range(0,65):
      print(f"Retrieving segment {segment} {layer}")

      segment_layer = f"{IMAGES_DIR}/{segment}/%.2d.tif" % layer

      if os.path.isfile(segment_layer):
          print(f"Segment {segment} layer %.2d already exists, skipping" % layer)
          continue

      retrieved = True

      r = requests.get(f"http://dl.ash2txt.org/full-scrolls/Scroll1.volpkg/paths/{segment}/layers/%.2d.tif" % layer, auth=(USERNAME, PASSWORD))

      with open(f"{IMAGES_DIR}/{segment}/%.2d.tif" % layer, "wb") as tiff_file:
          tiff_file.write(r.content)

  if retrieved:
    # Try to be a bit nice to the server
    sleep(5)                  
