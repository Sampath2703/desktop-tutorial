a = input("Enter word here : -- ")


if len(a) % 2 != 0:
    print("String length must be even")
else:
    b = len(a) // 2
    c = a[:b]
    d = a[b:]

    count1 = 0
    count2 = 0


    
    for i in c:
        if i in "AEIOUaeiou":
            count1 += 1

    
    for j in d:
        if j in "AEIOUaeiou":
            count2 += 1

   
    if count1 == count2:
        print(True)
    else:
        print(False)

# 2
arr = [121, 343, 456, 787, 90, 11]

count = 0

for num in arr:
    s = str(num) 
    if s[0] == s[-1]:
        count += 1

print("Count:", count)

# 3
num = int(input("enter number : --"))

s = str(num)
duplicate_sum = 0

for i in range(len(s)):
    count = 0
    for j in range(len(s)):
        if s[i] == s[j]:
            count += 1
    
    if count > 1:
        duplicate_sum += int(s[i])

print("Sum of duplicate digits:", duplicate_sum)

# 4
a = int(input("Enter number : --"))
for i in range(1,a+1):
    for j in range(1, i+1):
        print(j,end=" ")
    print()

# 5
a = int(input("Enter number : --"))
for i in range(a, 0, -1):
    for j in range(i, 0, -1):
        print(j,end=" ")
    print()

# 6
a = input("enter number : -- ")
sum = 0
for i in a:
    sum += int(i)
print(sum)


# 7
a = input("enter Number : -- ")
sum = 0
for i in a:
    sum += int(i) ** 3

if sum == int(a):
    print("Armstrong number")    
else:
    print("Not")
    

    