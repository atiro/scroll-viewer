from iiif_prezi3 import Manifest, Collection, config
import os
import pathlib

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"

single_canvas = True
create_collection = False

IIIF_IMAGE_API_BASE = "http://localhost:8180/iiif"
IIIF_PRES_API_BASE = "http://localhost:8080/"
SCROLL_DIR = "../images"
MANIFESTS_DIR = "../manifests"

coll_manifest = None

scroll = 1

create_collection = True

if create_collection:
    coll_manifest = Collection(
            id=f"{IIIF_PRES_API_BASE}/collection/scroll1/manifest.json",
            label="Scroll 1")

for root,dirs,files in os.walk(SCROLL_DIR):
  for segment in sorted(dirs):
     if not segment.startswith("2023"):
         print(f"skipping {segment}")
         continue

     if segment == "20230507175928":
         print(f"Segment 20230507175928 is breaking IIPimage, skipping")
         continue

     if segment == "20230503225234":
         print(f"Segment 20230503225234 is breaking IIPimage, skipping")
         continue

     if segment == "20230601192025":
         print(f"Segment 20230601192025 needs image 34.tif adding Richard, skipping")
         continue

     if segment == "20230929220921":
         print(f"Segment 20230929220921 has no layers, skipping")
         continue

     if segment == "20230514182829":
         print(f"Segment 20230514182829 has no layers, skipping")
         continue

     print(f"Creating manifest for segment {segment}")

     manifest = Manifest(id=f"{IIIF_PRES_API_BASE}/{segment}/manifest.json", 
        label=f"Scroll {scroll} Segment {segment}")

     if single_canvas:
     # Use choice (in forked prezi3 at the moment)
       canvas = manifest.make_canvas_from_iiif(
           url=f"{IIIF_IMAGE_API_BASE}/{segment}/00/info.json",
           id=f"{IIIF_PRES_API_BASE}/{segment}/canvas/0",
           anno_page_id=f"{IIIF_PRES_API_BASE}/annotation-service/page/0/1",
           anno_id=f"{IIIF_PRES_API_BASE}/annotation/p0-image",
           choice=True,
           label="")
       for p in range(1,65):
#      canvas.add_choice_iiif_image(
#        image_url="http://localhost:8080/images/segment-20230827161846/%.2d/full/full/0/default.jpg" % p)
         canvas.add_choice_iiif_image(image_url=f"{IIIF_IMAGE_API_BASE}/{segment}/%.2d/info.json" % p)
     else:
         # Todo - Create canvas per layer
         pass

     coll_manifest.add_item(manifest)

     pathlib.Path(f"{MANIFESTS_DIR}/{segment}/").mkdir(parents=True, exist_ok=True)

     with open(f"{MANIFESTS_DIR}/{segment}/manifest.json", "w") as manifest_json:
       manifest_json.write((manifest.json(indent=2)))

pathlib.Path(f"{MANIFESTS_DIR}/collection/volume1/").mkdir(parents=True, exist_ok=True)

with open(f"{MANIFESTS_DIR}/collection/volume1/manifest.json", "w") as collection_json:
  collection_json.write((coll_manifest.json(indent=2)))

