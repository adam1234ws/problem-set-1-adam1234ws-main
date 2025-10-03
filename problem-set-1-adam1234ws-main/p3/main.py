# main.py

def read_and_sum():
    n = int(input())
    if n < 0:
        return 0
    else:
        return n + read_and_sum()

total = read_and_sum()
print(total)
