# indi-firefly

All started here: http://www.astro.caltech.edu/ai19/hackathon.html

Make use of INDI python client to control telescope pointing (or any INDI compatible devices) with Firefly - the idea is to select a target (ra,dec mainly) and take a picture from Firefly by passing the coordinates to the python client (see [script](takeExposure.py).

Once the exposure(s) is written out locally, we could also upload FITS produced into Firefly from the same python local session...
Another step could be included but not added here is to solve/extract wcs/sources - this can be done with astropy/machine learning!
See astrometry.net

INDI framework consist of connecting client and server to compatible devices, details: https://www.indilib.org

Docker image can be found here: https://hub.docker.com/r/ejoliet/pyindihub/tags

docker pull ejoliet/pyindihub

then run `docker run -it <image-id> bash`

Clone and get python scripts here

in another terminal : `docker exec -it <container-id> bash`, run `indiserver -v indi_simulator_telescope indi_simulator_ccd`.

Edit config.json files, and take picture `python3 takeExposure.py config.json` 
(if using python2, please see code to change, mainly `import cStringIO` instead of `import io`)

Python3 was tested with Firefly integration, see [demo guide](DEMO-guide.md)
