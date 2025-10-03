# main.py

N = int(input())
k = int(input())

m = N // k  # largest multiple count
result = k * (m * (m + 1) // 2)

print(result)
