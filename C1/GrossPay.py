hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
rph = float(rate)
if h>40:
    pay = (40*rph)+((1.5*rph)*(h-40))
    print(pay)
else:
    pay = (h*rph)
    print(pay)
