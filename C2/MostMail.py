fname = input('Enter File Name: ')
fhandle = open(fname)
i = list()
j = list()
count = dict()
for line in fhandle :
    if 'From ' in line :
        l = line.split()
        i.append(l[1])
for freq in i :
    count[freq] = count.get(freq , 0) + 1
bigw = None
bigc = None
for k,v in count.items() :
    if bigc == None or v > bigc :
        bigc = v
        bigw = k
print(bigw,bigc)
for k,v in count.items() :
    j.append( (k,v) )
print(j)
