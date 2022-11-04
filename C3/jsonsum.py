import urllib.request , urllib.parse , urllib.error
import json
url = input('Enter URL- ')
con = urllib.request.urlopen(url).read()
js = json.loads(con)
k = 0
for c in js['comments'] :
    a = c['count']
    k = k+a
print(k)
