# FOR LOOP
for i in range(-1, -101, -1):
    print(i)

for i in range(-100, 0, 1):
    print(i)

# WHILE LOOP

i = 1
even_product = 1
odd_product = 1

while i <= 10:
    if i % 2 == 0:
        even_product *= i
    else:
        odd_product *= i
    i += 1

print("Even Product:", even_product)
print("Odd Product:", odd_product)


i = 1
even_sum = 0
odd_sum = 0

while i <= 10:
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
    i += 1

print("Even Sum:", even_sum)
print("Odd Sum:", odd_sum)