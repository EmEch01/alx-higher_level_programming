#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    This function replaces all occurrences of an element in a list with another

    Args:
        my_list: The list to modify.
        search: The element to replace.
        replace: The new element.

    Returns:
        A new list with all occurrences of `search` replaced with `replace`.
        The original list is not modified.
    """

    # Create a new list to store the replacements
    replaced_list = []

    # Loop through each element in the original list
    for element in my_list:
        # Check if the element is equal to the element to be replaced
        if element == search:
            # Append the replacement element to the new list
            replaced_list.append(replace)
        else:
            # Append the original element to the new list
            replaced_list.append(element)

    return (replaced_list)
