#! /usr/bin/env python3

# This function will have three parameters:
# - array
# - left, right: indexes that determine the part of the array
# that we want to sort. In the beginning, we'll sort the whole
# array, hence left will be zero and right will be the length
# of the array.
def quicksort(arr, left, right):
    # If the length of the sub-array to sort is 1, quicksort
    # does nothing. In other words, we're checking if the
    # sub-array has at least 2 elements.
    if left < right:
        # Calling another function with the same parameters.
        # It will store the index of the pivot element.
        partition_pos = partition(arr, left, right)
        # Calling quicksort on all elements that are less than
        # the pivot element.
        quicksort(arr, left, partition_pos - 1)
        # Calling quicksort on all elements that are greater
        # than the pivot element.
        quicksort(arr, partition_pos + 1, right)

# This function returns the index of the pivot element after
# the first step of quicksort.
def partition(arr, left, right):
    # i moves to the right
    i = left
    # j moves to the left
    j = right - 1
    pivot = arr[right]
    
    # i and j keep moving in their respective directions until
    # they cross. The while loop will check that.
    while i < j:
        # Moving i to the right while i is not at the end of
        # the array and the element at index i is less than
        # pivot.
        while i < right and arr[i] < pivot:
            i += 1
        # Moving j to the left while j is greater than left
        # and the element at index j is greater or equal to
        # pivot.
        while j > left and arr[j] >= pivot:
            j -= 1
        
        # When both loops are finished, we check if the two
        # element crossed. If they did, we swap them.
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    
    # If i and j crossed, we check if the element at index i
    # is greater than the pivot element. If that's the case,
    # we swap again.
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    
    # Returning i, because the quicksort function needs it to
    # determine where to split the array to call quicksort
    # recursively.
    return i

# Testing by defining a test array
arr = [22, 11, 88, 66, 55, 77, 33, 44]
print(f"Original array: {arr}")
# Calling quicksort on the array above, not forgetting the
# three parameters (at the beginning, left is 0 and right is)
# the length of the array -1).
quicksort(arr, 0, len(arr) - 1)

# Printing the sorted list
print(f"Sorted array: {arr}")

print()

# Testing one more time
another_arr = [11, 100, 3, 23, 91, 200, 17]
print(f"Original array: {another_arr}")
quicksort(another_arr, 0, len(another_arr) - 1)
print(f"Sorted array: {another_arr}")