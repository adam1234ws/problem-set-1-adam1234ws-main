# main.py

a = int(input())
b = int(input())
c = int(input())

# Assume first number is the largest
largest = a

if b > largest:
    largest = b

if c > largest:
    largest = c

print(largest)
