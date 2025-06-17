#!/usr/bin/env python3
my_list = [1, 2, 3, 4, 5] 

def add_item_to_list(ordered_list):
    # Appends new item to end of list with the value (last item + 1)
    ordered_list.append(ordered_list[-1] + 1)

def remove_items_from_list(ordered_list, items_to_remove):
    # Removes all values, found in items_to_remove list, from ordered_list
    for item in items_to_remove:
        while item in ordered_list:  # Ensures all occurrences are removed
            ordered_list.remove(item)

# Main code
if __name__ == '__main__':
    print("Original list:", my_list)
    
    # Adding items
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    
    print("After adding items:", my_list)
    
    # Removing specified items
    remove_items_from_list(my_list, [1, 5, 6])
    print("After removing items [1, 5, 6]:", my_list)
