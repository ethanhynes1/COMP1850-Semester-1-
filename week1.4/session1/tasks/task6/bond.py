# Week 4, Session 1: 

# You are given an incomplete function isBond with a docstring. Your task
# is to complete the function based on the details in the docstring.


def isBond(intList):
    """
    This function accepts a list of integers and returns True if the
    sequence 0, 0, 7 appears in the list, in that order. Return False
    otherwise. The numbers do not need to be consecutive, but must appear
    in the specified order.
    """

    # pass is a Python keyword used as a placeholder for future code,
    # meaning you need to delete pass to write your code.
    # Nothing happens when pass is executed.

    for i in range(0,len(intList)-2):
        #print(f"{intList[i]} ,{intList[i+1]}, {intList[i+2]}")
        if intList[i] == 0 and intList[i+1] == 0 and intList[i+2] == 7:
            return True
    zeros = 0
    for num in intList:
        if num == 0:
            zeros += 1

        elif num == 7 and zeros == 2:
            return True 

    return False
# Check if the following lines of code produce the correct output
print(isBond([1, 2, 4, 0, 0, 7, 5]))   # True
print(isBond([1, 0, 2, 4, 0, 5, 7]))   # True
print(isBond([1, 7, 2, 0, 4, 5, 0]))   # False
