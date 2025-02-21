#!/usr/bin/env python3

def print_fibonacci(length):
    """Prints a list of Fibonacci numbers up to the given length."""
    if length <= 0:
        print([])
        return
    
    fibonacci = [0, 1] if length > 1 else [0]  

    while len(fibonacci) < length:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    
    print(fibonacci)
    pass