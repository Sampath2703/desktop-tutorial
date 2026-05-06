# average
def find_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

numbers = [10,20,30,40,50]
print(find_average(numbers))

# 2nd task
def remove_vowels(a):
    result = ""
    for i in a:
        if i not in "AEIOUaeiou":
            result += i
    return result

a = "Apple"
print(remove_vowels(a))

# max 
def max_value(num):
    return max(num)

num = [10,20,30,40,20,43,0]
print(max_value(num))

# 4th task
def calculator(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b != 0:
            return a / b
        else:
            return "Division by zero error"
    else:
        return "Invalid operation"

print(calculator(10, 5, "+"))

# 5th task
def longest_string(strings):
    if len(strings) == 0:
        return None
    longest = strings[0]
    for s in strings:
        if len(s) > len(longest):
            longest = s
    return longest
strings = ["cat", "elephant", "dog"]
print(longest_string(strings))

def area(length, width):
    return length * width

def perimeter(length, width):
    return 2 * (length + width)


print(area(5, 3))      
print(perimeter(5, 3)) 