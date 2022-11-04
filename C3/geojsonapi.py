import urllib.request , urllib.parse , urllib.error
import json
api = False
if api is False:
    api = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
address = input('Enter address')
place = dict()
place['address'] = address
place['key'] = api
addurl = urllib.parse.urlencode(place)
url = serviceurl+addurl
print(url)
conn = urllib.request.urlopen(url)
conn1 = conn.read().decode()
js = json.loads(conn1)
for pl in js['results'] :
    print(pl['place_id'])
