#!/usr/bin/env python3
'''Lab 3 Part 1 script - functions'''
# Author ID: lbudhathoki

def sum_numbers(number1, number2):
    # This function adds two numbers and returns the result
    return number1 + number2

def subtract_numbers(number1, number2):
    # This function subtracts the second number from the first number and returns the result
    return number1 - number2

def multiply_numbers(number1, number2):
    # This function multiplies two numbers and returns the result
    return number1 * number2

if __name__ == '__main__':
    print(sum_numbers(10, 5))  # This will return 15
    print(subtract_numbers(10, 5))  # This will return 5
    print(multiply_numbers(10, 5))  # This will return 50
