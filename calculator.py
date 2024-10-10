def calculator():
    print("Simple Calculator!")
    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    print("Choose an operation:")
    print("1. Addition (+),2. Subtraction (-),3. Multiplication (*),4. Division (/)")
    
    operation = input("Enter the number corresponding to the operation (1/2/3/4): ")

    if operation == '1':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == '2':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == '3':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("invalid")
    else:
        print("Please select a valid option.")

calculator()