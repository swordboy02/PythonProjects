fname = input('Enter FileName')
fhandle = open(fname)
count = 0
for x in fhandle :
    x = x.rstrip()
    if x.startswith("From ") == True :
        count = count+1
        l = x.split()
        print(l[1])
print("There were", count, "lines in the file with From as the first word")
