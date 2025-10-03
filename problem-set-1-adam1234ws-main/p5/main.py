# main.py

def read_and_build_string(current=""):
    n = int(input())
    if n < 0:
        return current
    else:
        return read_and_build_string(current + str(n))

result = read_and_build_string()
print(result)
