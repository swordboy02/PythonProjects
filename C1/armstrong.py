num = input("Enter a Number")
a = len(num)
i = int(a)
tot = 0
for x in num:
    l = int(x)**i
    tot = tot+l
if tot == int(num) :
    print("Armstrong Num")
else: print("Not an Armstrong Num")
