a = [2,3,4,2,3,4,5,7]
b = sorted(set(a))
print(b)

# 2nd 
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_numbers(arr):
    result = []
    
    for num in arr:
        if is_prime(num + 1):
            result.append(num)
    
    return result

arr = [7, 4, 7, 23, 10, 6]

output = find_numbers(arr)
print(*output)

# 3rd

a = " aaabbaaccdd"

a = a.strip()   
result = ""
count = 1

for i in range(len(a)):
    if i < len(a) - 1 and a[i] == a[i + 1]:
        count += 1
    else:
        result += a[i] + str(count)
        count = 1

print(result)