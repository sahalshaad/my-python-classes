num1= input("enter number 1: ")
num2= input("enter number 2: ")

while True:
    print("choose one option")
    print("1. is addision : ")
    print("2. is multiplication : ")
    print("3. is division : ")
    print("4. is substraction : ")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        addision= (int(num1)+ int(num2))
        print("Result is: "+num1+"+"+num2+"="+str(addision))
    elif choice == 2:
        mult = (int(num1)* int(num2))
        print(num1+"*"+num2+"="+str(mult))
    elif choice == 3:
        divsion = (int(num1)/int(num2))
        print(num1+"/"+num2+"="+str(divsion))
    elif choice == 4:
        substraction = (int(num1)-int(num2))
        print(num1+"-"+num2+"="+str(substraction))
    else:
        print("Invalid choice.")
