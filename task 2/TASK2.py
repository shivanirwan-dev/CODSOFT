num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number:"))

# Asking user which operation is to be performed
print(" 1. Sum \n 2. Substraction \n 3. Multiplication \n 4. Division")
choice = int(input("Enter your choice: "))

if choice == 1:
    sum = num1 + num2
    print(f"The sum of entered numbers is: {sum}")
elif choice == 2:
    sub = num1 - num2
    print(f"The substraction of the entered numbers is: {sub}")
elif choice == 3:
    multiply = num1 * num2
    print("The multiplication of the entered number is: ", multiply)
elif choice == 4:
    if num1 == 0:
        print("The division of the numbers is: 0 ")
    elif num2 == 0:
        print("The number cannot be divided by 0 (zero division error)")
    else:
        division = num1/ num2
        print("The division of the entered numbers is: ",division)
else: 
    print("Invalid choice, Please choose again")
