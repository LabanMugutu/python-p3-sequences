#!/usr/bin/env python3

#!/usr/bin/env python3

def print_fibonacci(length):
    """
    Prints a list containing the Fibonacci sequence up to the given length.
    
    Example:
    >>> print_fibonacci(9)
    [0, 1, 1, 2, 3, 5, 8, 13, 21]
    """
    # Handle edge cases for small lengths
    if length <= 0:
        print([])
        return
    elif length == 1:
        print([0])
        return
    elif length == 2:
        print([0, 1])
        return

    # Start the list with the first two Fibonacci numbers
    fib_sequence = [0, 1]

    # Build the sequence
    for i in range(2, length):
        next_num = fib_sequence[-1] + fib_sequence[-2]  # sum of last two elements
        fib_sequence.append(next_num)

    # Print the final list
    print(fib_sequence)
