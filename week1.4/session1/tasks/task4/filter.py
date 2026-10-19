# Week 4, Session 1: 

# Your are given the function filter_positive_numbers with a docstring.
# Can you identify the inconsistency between the docstring and the implementation?

# Your task is to update the docstring to reflect what the function does.


def filter_positive_numbers(numbers):

    
    """
    Filters out positive numbers from the list, keeping only the negative ones.
    The function returns a list of all the positive numbers in the input.

    Args:
        numbers (list of int): A list of integers.

    Returns:
        list of int: A list containing only the positive integers.
    """

    for i in range(0, len(numbers)):
            if numbers[i] > 0:
                print(numbers[i])
                numbers[i] = 0
    
    return [num for num in numbers if num < 0]

n = [5, 7 ,-4, -12, 0 ,4, -1]
print(filter_positive_numbers(n))