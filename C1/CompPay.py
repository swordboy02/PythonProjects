def computepay(h,r):
    if h>40:
        pay = (40*r)+((1.5*r)*(h-40))

    else:
        pay = (h*r)
    return pay

hrs = input("Enter Hours:")
hrs1 = float(hrs)
rate = input("Enter Rate:")
rph = float(rate)
p = computepay(hrs1,rph)
print("Pay",p)
