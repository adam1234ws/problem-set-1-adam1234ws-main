# main.py

def read_numbers(smallest=None, second_smallest=None):
    n = int(input())
    if n < 0:   # stop condition
        return smallest, second_smallest

    if smallest is None or n < smallest:
        # shift current smallest down to second
        second_smallest = smallest
        smallest = n
    elif second_smallest is None or n < second_smallest:
        second_smallest = n

    return read_numbers(smallest, second_smallest)


smallest, second_smallest = read_numbers()
print(smallest, second_smallest)
