import urllib.request , urllib.parse , urllib.error
import xml.etree.ElementTree as ET
k = 0
url = input('enter url: ')
html = urllib.request.urlopen(url)
html1 = html.read()
c = ET.fromstring(html1)
l = c.findall('comments/comment')
for t in l :
    x = t.find('count').text
    x = int(x)
    k = k+x
print(k)
