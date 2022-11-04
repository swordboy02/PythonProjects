fname = input('Enter FileName')
fhandle = open(fname)
i = list()
for x in fhandle :
        x = x.lstrip()
        l = x.split()
        for y in l :
            if not y in i:
                i.append(y)
i.sort()
print(i)
