#!/usr/bin/python3
def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.
    
    Parameters:
    - list_of_integers (list): A list of unsorted integers.
    
    Returns:
    - int: A peak element.
    
    Complexity: O(log(n))
    """
    if not list_of_integers:
        return None
    left = 0
    right = len(list_of_integers) - 1
    
    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid
    
    return list_of_integers[left]
