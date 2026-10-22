# How it works:

#     Choose a value in the array to be the pivot element.
#     Order the rest of the array so that lower values than the pivot element are on the left, and higher values are on the right.
#     Swap the pivot element with the first element of the higher values so that the pivot element lands in between the lower and higher values.
#     Do the same operations (recursively) for the sub-arrays on the left and right side of the pivot element.


# Quicksort Implementation

# To write a 'quickSort' method that splits the array into shorter and shorter sub-arrays we use recursion. 
# This means that the 'quickSort' method must call itself with the new sub-arrays to the left and right of the pivot element

def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    return i+1

def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index-1)
        quicksort(array, pivot_index+1, high)


def partition(array, low, high):
    """
    Takes the last element as the pivot, places the pivot element at its 
    correct position in the sorted array, places all smaller elements to 
    the left of the pivot, and all larger elements to the right.
    """
    pivot = array[high]  # Choose the last element as the pivot
    i = low - 1          # Pointer for tracking the boundary of smaller elements

    # Traverse through all elements from 'low' up to 'high - 1'
    for j in range(low, high):
        # If the current element is smaller than or equal to the pivot
        if array[j] <= pivot:
            i += 1  # Expand the region of smaller elements
            # Swap the current element with the element at index i
            array[i], array[j] = array[j], array[i]

    # Move the pivot to its final correct position (just after the smaller elements)
    array[i + 1], array[high] = array[high], array[i + 1]
    
    # Return the index where the pivot is now permanently located
    return i + 1


def quicksort(array, low=0, high=None):
    """
    A recursive function that implements the Quicksort algorithm 
    using a divide-and-conquer strategy.
    """
    # If the high index is not provided, default to the last index of the array
    if high is None:
        high = len(array) - 1

    # Base case: continue only if there is more than one element to sort
    if low < high:
        # Partition the array and get the index of the pivot element
        pivot_index = partition(array, low, high)
        
        # Recursively sort the sub-array to the left of the pivot
        quicksort(array, low, pivot_index - 1)
        
        # Recursively sort the sub-array to the right of the pivot
        quicksort(array, pivot_index + 1, high)


# --- Example Usage ---
my_array = [64, 34, 25, 12, 22, 11, 90, 5]
quicksort(my_array)
print("Sorted array:", my_array)