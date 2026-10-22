def insertion_sort(array, low, high):
    """
    Sorts a small sub-array using Insertion Sort. 
    This is faster for small collections (e.g., 10 or fewer items) 
    because it avoids the function-call overhead of recursion.
    """
    for i in range(low + 1, high + 1):
        key = array[i]
        j = i - 1
        
        # Shift elements greater than the key to the right
        while j >= low and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
            
        # Insert the key into its correct sorted position
        array[j + 1] = key


def median_of_three(array, low, high):
    """
    Finds the median value among the low, middle, and high elements, 
    and swaps it to the 'high' index to act as the pivot. 
    This prevents the O(N^2) worst-case performance on sorted arrays.
    """
    mid = (low + high) // 2
    
    # Sort the low, middle, and high elements relative to each other
    if array[low] > array[mid]:
        array[low], array[mid] = array[mid], array[low]
    if array[low] > array[high]:
        array[low], array[high] = array[high], array[low]
    if array[mid] > array[high]:
        array[mid], array[high] = array[high], array[mid]
        
    # Move the median element to the end to serve as our pivot
    array[mid], array[high] = array[high], array[mid]


def optimized_partition(array, low, high):
    """
    Partitions the array around the pivot chosen by median-of-three,
    placing smaller elements to the left and larger elements to the right.
    """
    # Optimize pivot choice using median-of-three
    median_of_three(array, low, high)
    pivot = array[high]
    i = low - 1

    # Traverse and rearrange elements based on the pivot
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    # Place the pivot into its final, permanent sorted position
    array[i + 1], array[high] = array[high], array[i + 1]
    
    # Return the index of the pivot
    return i + 1


def optimized_quicksort(array, low=0, high=None):
    """
    A robust, recursive Quicksort function incorporating performance 
    optimizations like small-array insertion sort and pivot balancing.
    """
    if high is None:
        high = len(array) - 1

    # Optimization: Switch to Insertion Sort when the sub-array is small
    if high - low <= 10:
        insertion_sort(array, low, high)
        return

    # Standard recursive divide-and-conquer steps
    if low < high:
        pivot_index = optimized_partition(array, low, high)
        optimized_quicksort(array, low, pivot_index - 1)
        optimized_quicksort(array, pivot_index + 1, high)


# --- Example Usage ---
my_array = [64, 34, 25, 12, 22, 11, 90, 5, 22, 34, 11]
optimized_quicksort(my_array)
print("Sorted array:", my_array)