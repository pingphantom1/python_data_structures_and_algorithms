# The Insertion Sort algorithm uses one part of the array to hold the sorted values, and the other part of the array to hold values that are not sorted yet.
# The algorithm takes one value at a time from the unsorted part of the array and puts it into the right place in the sorted part of the array, until the array is sorted.

# How it works:

#     Take the first value from the unsorted part of the array.
#     Move the value into the correct place in the sorted part of the array.
#     Go through the unsorted part of the array again as many times as there are values.

# Insertion Sort Implementation

# To implement the Insertion Sort algorithm in a programming language, we need:

#     An array with values to sort.
#     An outer loop that picks a value to be sorted. For an array with n values, this outer loop skips the first value, and must run n−1 times.
#     An inner loop that goes through the sorted part of the array, to find where to insert the value. If the value to be sorted is at index i, the sorted part of the array starts at index 0 and ends at index i−1.

# The resulting code looks like this:

my_array = [64, 34, 25, 12, 22, 11, 90, 3,  78, 74, 53, 12, 3, 8, 11, 23, 54, 39, 90, 67, 36, 23, 15, 2, 34, 91, 43, 6, 6, 5]

def insertion_sort(my_array):
    n = len(my_array) # length of the array
    for i in range(1,n):
        insert_index = i
        current_value = my_array[i]
        for j in range(i-1, -1, -1):
            if my_array[j] > current_value:
                my_array[j + 1] = my_array[j]
                insert_index = j
            else:
                break
        my_array[insert_index] = current_value

    return my_array
    

print("Sorted array: ", insertion_sort(my_array))