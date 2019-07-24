# Python demo to run in docker ejoliet/pyindihub

- Run kstars

- spin up container and enter bash:

`docker run -v ~/Box/Astroinformatics2019/:/root/giss-2019 -it -p 7624:7624 ejoliet/pyindihub bash`

- If not running yet:

`indiserver -v indi_simulator_telescope indi_simulator_ccd`

- Make sure you cloned the python scripts

`git pull ~/indi-firely/`

- Connect kstar to remote server localhost:7624 as client to see telescope and exposure actions!

- Run demo on another console

Get container id: `dr container ls` OR see console bash: `root@<container-id>:/#`
then:

`docker exec -it <container-id> bash`

Go to python folder

`cd ~/indi-firefly`

- Run python3 copy paste the line below

`python3`

>>>
```
from firefly_client import FireflyClient

# == What is your localhost/IP/FQN? .. replace below, this is mine locally luke.ipac.caltech.edu

url='http://luke.ipac.caltech.edu:8080/firefly'

fc = FireflyClient(url)
import astropy.utils.data

image_url = ('http://irsa.ipac.caltech.edu/ibe/data/wise/allsky/4band_p1bm_frm/6a/02206a' + 
             '/149/02206a149-w1-int-1b.fits?center=70,20&size=200pix')
filename = astropy.utils.data.download_file(image_url, cache=True, timeout=120)

table_url = ("http://irsa.ipac.caltech.edu/TAP/sync?FORMAT=IPAC_TABLE&" +
                                             "QUERY=SELECT+*+FROM+fp_psc+WHERE+CONTAINS(POINT('J2000',ra,dec)," +
                                             "CIRCLE('J2000',70.0,20.0,0.1))=1")
tablename = astropy.utils.data.download_file(table_url, timeout=120, cache=True)

localbrowser, browser_url = fc.launch_browser()

fc.display_url()

#====

#imval = fc.upload_file(filename)
#status = fc.show_fits(file_on_server=imval, plot_id="wise-cutout", title='WISE Cutout')

file= fc.upload_file(tablename)
status = fc.show_table(file, tbl_id='tablemass', title='My 2MASS Catalog', page_size=50)

#=======

import fctgt.py


fc.add_listener(fctgt.print_coords)

fc.add_extension(ext_type='POINT', plot_id=None, title='Take Exposure!', extension_id='pickit')
```



See [fctgt.py](fctgt.py):
```
import json, subprocess

def pointTelescope(ra,dec):
    # write out json config - to take exposure with INDI client
    configindi = {'star': {'ra':ra, 'dec':dec, 'name':'test'}}
    with open('firefly-wpt-selected.json', 'w') as outfile:  
        json.dump(configindi, outfile)
    subprocess.call(["python3","takeExposure.py","firefly-wpt-selected.json"])
    
def print_coords(event):
    if 'wpt' in event['data']:
       wpt = event['data']['wpt']
       wdata = wpt.split(';')
       ra = float(wdata[0])
       dec = float(wdata[1])
       print('Selected ra={:.6f}, dec={:.6f}'.format(ra,dec))
#       with open('event.json', 'w') as outfile:  
#           json.dump(event['data'], outfile)
       pointTelescope(wdata[0],wdata[1])
```

- the demo will produce a json [config file](firefly-wpt-selected.json) and run the exposure CCD sequence and produce IMG-*.fits

- in python console, upload the exposure observed! (script can make use astrometry.net, astropy and WCS to convert image pixel into wcs ;-) ) 

```
imval = fc.upload_file('IMG-*.fits')
status = fc.show_fits(file_on_server=imval, plot_id="exposure-test", title='Test Exposure')
```
