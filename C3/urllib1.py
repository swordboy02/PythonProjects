import urllib.request , urllib.parse , urllib.error
import re
from bs4 import BeautifulSoup
l = list()
l2 = list()
url = input("Enter URL- ")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html , 'html.parser')

tags = soup('span')
for tag in tags :
    x = str(tag)
    j = re.findall('[0-9]+', x)
    l.append(j)
for x in l :
    l2 = l2 + x
sum = 0
for c in l2 :
    c = int(c)
    sum = sum+c
print(sum)
