# main.py

X = int(input())
k = int(input())

if k >= X:
    print(0)
else:
    result = (X - 1) // k * k
    print(result)
