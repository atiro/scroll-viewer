# Scroll Viewer

A (mostly) self-contained [IIIF](https://iiif.io) powered Scroll Segment viewer.

To get it running you need to (in brief):

  - Retrieve the scrolls segment path images (for all of Volume 1 this is around 450GB, ideally the pyramidified TIFF
    images would be stored on the server so we don't all have to create our own (and also they compress down to around 50GB
    thanks to [VIPS](https://https://github.com/libvips/libvips))).
  - Pyramidify them to turn the tiffs in Pyramid Tiffs (as per https://iipimage.sourceforge.io/documentation/images) (you need to have libvips installed, on Debian/Ubuntu apt install libvips-tools)
  - Start the IIPImage server running as a docker container to serve up the images via the IIIF Image API
  - Create IIIF manifests for each segment and an IIIF Collection manifest for the first volume.

Once you have done this, you can then run the Electron app and it should show the segments browsable via the [Mirador](https://projectmirador.org/) interface.

Other features could be added into the viewer, such as linking together the different viewers (scroll/segment) to illustrate where
in the scroll the segment is.

The IIIF manifest can also be used to annotate the images with identified text.

## Instructions 

### Retrieve scroll segments

You will need to register to retrieve the scroll data at https://scrollprize.org/data.

Once you have registered you can add the username and password into the script 'retrieve-scrolls.py' and run it
to download all the scroll layers for Volume 1. This will take some time (days...) depending on your connection speed.

(Ideally this step could be sped up if the pyramid TIFFs could be stored on the server, reducing the download time)

### Pyramidfy scroll segments

The TIFF images need to be turned into Pyramid TIFF images to be used for zooming in. The script pyramid_images.py
will do this.

### Setup IIIF Image server

The IIPImage server is dockerised, you can start running it with: docker-compose up

### Generate IIIF manifests

The IIIF manifests gather together all the 65 layer images per segment into one manifest.

There are two possible ways to create this manifest for each segment, one presents all the 65 layers on top of each other (a
stacked canvas) which means Mirador can then show you options such as opacity for each layer to let you blend them together.
The downside is you will be requesting tiles from 65 layers simultaneously which might slow your computer down, and there
is no way to address each layer individually for annotations (i.e. you can set x,y but not z)

The alternative manifest build uses a canvas per layer, so you can see each layer individually and address each one if you 
want to annotate something on a particular layer. (TODO)

The script will build both. (TODO)

You will probably also want to build a collection manifest which gathers together all the created manifests in one, 

### Build Scroll Viewer app

A very simple electron app using [Mirador](https://projectmirador.org/) to browse the local manifests and images. This
can be developed a lot more...

Build using npm install in app directory

### Read (sort-of) the scrolls

npm start in app directory

Good luck!
