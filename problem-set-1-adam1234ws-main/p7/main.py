# main.py

import math

value = float(input())
unit = input().strip()

if unit == "C" or unit == "c":
    converted = (value * 9 / 5) + 32
    converted = math.floor(converted * 10) / 10
    print(f"{converted:.1f} F")
elif unit == "F" or unit == "f":
    converted = (value - 32) * 5 / 9
    converted = math.floor(converted * 10) / 10
    print(f"{converted:.1f} C")
