First = input("Enter your first number: ")
Operator = input("Enter your operator (+, -, /, *): ")
Second = input("Enter your second number: ")

First = int(First)
Second = int(Second)

if Operator == "+":
    print(First + Second)
elif Operator == "-":
    print(First - Second)
elif Operator == "/":
    print(First / Second)
elif Operator == "*":
    print(First * Second)
else:
    print("Invalid operator")
