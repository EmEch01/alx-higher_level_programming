#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    This function adds all unique integers in a list.

    Args:
        my_list: The list of integers to process. Defaults to an empty list.

    Returns:
        The sum of all unique integers in the list.
    """

    sum_of_uniques = 0
    seen = set()  # Use a set to track seen integers

    # Loop through each element in the list
    for num in my_list:
        # Check if the element is an integer
        if isinstance(num, int):
            # Check if the element is not already seen
            if num not in seen:
                # Add the element to the set of seen integers
                seen.add(num)
                # Add the element to the sum
                sum_of_uniques += num

    return sum_of_uniques
