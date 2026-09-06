units = int(input("enter units: "))
connection_type = input("enter connection type(non-commercial or commercial): ")
if connection_type == "non-commercial":
    if 0<=units<=200:
        print("Total Bill: Free(no charge) ",)
    elif 201<=units<=500:
        print("Total Bill: ₹",4*units)
    elif 501<=units<=2000:
        print("Total Bill: ₹",8*units)
    else:
        print("Total Bill: ₹",10*units)
elif connection_type == "commercial":
    if 0<units<=500:
        print("Total Bill: ₹",6*units)
    elif 501<units<=1000:
        print("Total Bill: ₹",9*units)
    elif 1001<units<=5000:
        print("Total Bill: ₹",12*units)
    else:
        print("Total Bill: ₹",15*units)
else:
    print("Invalid connection type!! please enter the correct connection type")