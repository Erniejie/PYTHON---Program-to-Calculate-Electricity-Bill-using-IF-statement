#Program to Calculate Electricity Bill using ‘if’ statement.
"Computer Programming Tutor, Aug 17,2021"

nos = int(input("Enter Current Meter Number:"))
bill = 0

if(nos == 1111):
    print("1- Rural Area")
    print("2- Residential Cities")
    print("3- Commercial")

    op = int(input("Choose Category:"))
    if (op == 1):
        s = 15
        unit = int(input("Enter Number of Units Consumed: "))
        if (unit > 0 and unit < 50):
            bill = (unit*0.34) + s
        elif (unit >= 50 and unit < 150):
            bill = (unit*0.67) + s
        elif (unit >= 150 and unit < 300):
            bill = (unit*0.76) + s
        elif (unit >= 300 and unit < 500):
            bill = (unit*1.25) + s
        elif (unit >= 500 and unit < 1000):
            bill = (unit*1.95) + s
        else:
            print("Invalid Units")
        print("Current Meter Number: ", nos)
        print("Units Consumed:",unit)
        print("Selected Category:",op)
        print("Bill Amount,[£]: %.2f"% bill)
    elif (op == 2):
        s=45
        unit = int(input("Enter Number of Units Consumed: "))
        if (unit > 0 and unit < 50):
            bill = (unit*1.45) + s
        elif (unit >= 50 and unit < 150):
            bill = (unit*2.45) + s
        elif (unit >= 150 and unit < 300):
            bill = (unit*3) + s
        elif (unit >= 300 and unit < 500):
            bill = (unit*3.5) + s
        elif (unit >= 500 and unit < 1000):
            bill = (unit*5) + s

        else:
            print("Invalid Units")
        print("Current Meter Number: ", nos)
        print("Units Consumed:",unit)
        print("Selected Category:",op)
        print("Bill Amount,[£]: %.2f"% bill)
    elif(op == 3):
        s= 75
        unit = int(input("Enter Number of Units Consumed: "))
        if (unit > 0 and unit < 50):
            bill = (unit*3) + s
        elif (unit >= 50 and unit < 150):
            bill = (unit*5.5) + s
        elif (unit >= 150 and unit < 300):
            bill = (unit*6.5) + s
        elif (unit >= 300 and unit < 500):
            bill = (unit*7.8) + s
        elif (unit >= 500 and unit < 1000):
            bill = (unit*9) + s

        else:
            print("Invalid Units")
        print("Current Meter Number: ", nos)
        print("Units Consumed:",unit)
        print("Selected Category:",op)
        print("Bill Amount,[£]: %.2f"% bill)
    else:
        print("Wrong Choice")

else:
    print("Wrong Pin Number")
        
        
        
            
            
        
            
