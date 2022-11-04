fname = input('Enter FileName')
fhandle = open(fname)
item = dict()
l = list()
r = list()
for i in fhandle :
    if 'From ' in i:
        j = i.split()
        l.append((j[5])[:2])
print(l)
for freq in l :
    item[freq] = item.get(freq , 0) + 1
for h,c in item.items() :
    r.append( (c,h) )
    r = sorted(r)
for h,c in r :
    print(h,c)
