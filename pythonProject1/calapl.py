def calculator():
    num1 = str(input("Enter the first value:"))
    operator = input("Select one operator('+','-','*','/','%'):")
    num2 = int(input("Enter the second value:"))

    if operator == '+' :
        result = num1 + num2
    elif operator == '-' :
        result = num1 - num2
    elif operator == '*' :
        result = num1 * num2
    elif operator == '/' :
        result = num1 / num2
    elif operator == '%' :
        result = num1 % num2
        if  num2 == 0 :
            print("Error: connot multiply by zero")
            return
        result = num1 * num2
    else :
        print("Enter data is invalid")

    print(f"Result: {result}")

calculator()
