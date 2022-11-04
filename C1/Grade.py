score = input("Enter Score: ")
isc = float(score)
if isc >= 1:
    print("Out of range")
    quit()
elif isc >= 0.9:
    print("A")
elif isc >= 0.8:
    print("B")
elif isc >= 0.7:
    print("C")
elif isc >= 0.6:
    print("D")
elif isc < 0.6:
    print("F")
else :
    print("Out of range")
    quit()
