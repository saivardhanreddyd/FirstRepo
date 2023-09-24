def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter your choice (1-4): ")

if choice in ['1', '2', '3', '4','5','6']:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '3':
        print("Result:", subtract(num1, num2))
    elif choice == '5':
        print("Result:", multiply(num1, num2))
    else:
        if num2 != 0:
            print("Result:", divide(num1, num2))
        else:
            print("Error: Cannot divide by zero!")
else:
    print("Invalid answer!")
