#!/usr/bin/env python3

# Author ID: lbudhathoki

# Declaring the list called my_list
my_list = [100, 200, 300, 'six hundred']

# Function to return all items in the global my_list unchanged
def give_list():
    return my_list

# Function to return the first item in my_list as a string
def give_first_item():
    return str(my_list[0])

# Function to return a list that includes the first and last items in my_list
def give_first_and_last_item():
    return [my_list[0], my_list[-1]]

# Function to return a list that includes the second and third items in my_list
def give_second_and_third_item():
    return my_list[1:3]

# Main Program
if __name__ == '__main__':
    print(give_list())  # Prints the entire list
    print(give_first_item())  # Prints the first item as a string
    print(give_first_and_last_item())  # Prints the first and last items as a list
    print(give_second_and_third_item())  # Prints the second and third items as a list
