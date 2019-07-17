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
#       with open('event.json', 'w') as outfile:
#           json.dump(event['data'], outfile)
       pointTelescope(wdata[0],wdata[1])
