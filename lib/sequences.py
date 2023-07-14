#!/usr/bin/env python3

def print_fibonacci(length):
    sequence = [0, 1]  # Initialize the sequence with the first two numbers
    while len(sequence) < length:
        next_number = sequence[-1] + sequence[-2]  # Calculate the next number
        sequence.append(next_number)  # Add the next number to the sequence
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    else:
        print(sequence)
