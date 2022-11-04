fname = input('Please enter file name: ')
fhandle = open(fname)
cnt = 0
tot = 0
for x in fhandle :
    if 'X-DSPAM-Confidence:' in x :
        cnt = cnt + 1
        cpos = x.find(':')
        nx = x[cpos+1:]
        nx = nx.lstrip()
        num = float(nx)
        tot = tot + num
print('Average spam confidence:',tot/cnt)
