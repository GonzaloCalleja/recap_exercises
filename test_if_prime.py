print("This program asks for a number and tests if it is prime")
while True:
    try:
        read_line = input("Please give me an integer number ")
        num = int(read_line)
    except ValueError:
        print("That was not a valid integer number")
        continue
    break

# This loop doesn't look doesn't work for number 4 bc the for loop doesn't execute
for i in range(2, num // 2):
    if num % i == 0:
        print("The number", num, "is not prime")
        break
# print("The number", num, "is prime")

# generate 100 numbers, print only the prime ones
import random

a = []
for i in range(0, 100):
    a.append(random.randint(1, 10000))

print(a)

for num in a:
    is_prime = True
    for i in range(2, num // 2):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=", ")

