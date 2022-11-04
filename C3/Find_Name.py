import urllib.request , urllib.parse , urllib.error
from bs4 import BeautifulSoup
url = input("Enter URL- ")
c = input('Enter Count: ')
c = int(c)
p = input('Enter Position: ')
for i in range(c) :
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html,'html.parser')
    tags = soup('a')
    x1 = int(p)
    for tag in tags :
        x1 = x1 - 1
        if x1 == 0 :
            x = str(tag.get('href',None))
            print('URL-> ',x)
    url = x
