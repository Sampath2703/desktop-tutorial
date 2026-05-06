# task-1
Age = input("Enter Your Age: ")
if int(Age) >=18:
    print("Eligible for Voting")
else:
    print("Not Eligible for Voting")

# task-2 
Grade = int(input("Enter input: "))
if Grade >= 85:
    print("Excellent")
elif Grade >= 70 and Grade < 85:
    print("Good")
elif Grade >= 50 and Grade < 70:
    print("Pass")
else:
    print("Fail")

# task-3
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print("Result:", num1 + num2)

elif operator == "-":
    print("Result:", num1 - num2)

elif operator == "*":
    print("Result:", num1 * num2)

elif operator == "/":
    if num2 == 0:
        print("Error: Division by zero is not allowed")
    else:
        print("Result:", num1 / num2)

else:
    print("Invalid operator")


# task-4
year = int(input("Enter Year: "))
if year % 4 == 0:
    print("Leap year")
else:
    print("Not Leap year")

# task-5
number = int(input("Enter Number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")