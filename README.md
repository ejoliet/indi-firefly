# indi-firefly
Integrate Firefly with INDI python client

INDI framework consist of connecting client and server to compatible devices, details: https://www.indilib.org

Docker image can be found here: https://hub.docker.com/r/ejoliet/pyindihub/tags

docker pull ejoliet/pyindihub

then run `docker run -it <image-id> bash`

Clone and get python scripts here

in another terminal : `docker exec -it <container-id> bash`, run `indiserver -v indi_simulator_telescope indi_simulator_ccd`.

Edit config.json files, and take picture `python takeExposure.py config.json` 
