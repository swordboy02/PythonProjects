import re
fname = input('Input File Name ')
fhandle = open(fname)
l = list()
l2 = list()
for i in fhandle :
    j = re.findall('[0-9]+',i)
    l.append(j)
for x in l :
    l2 = l2 + x
sum = 0
for c in l2 :
    c = int(c)
    sum = sum+c
print(sum)
