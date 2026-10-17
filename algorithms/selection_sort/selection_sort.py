# The algorithm looks through the array again and again, moving the next lowest values to the front, until the array is sorted.
# How it works:

#     Go through the array to find the lowest value.
#     Move the lowest value to the front of the unsorted part of the array.
#     Go through the array again as many times as there are values in the array.

# Selection Sort Implementation

# To implement the Selection Sort algorithm in a programming language, we need:

#     An array with values to sort.
#     An inner loop that goes through the array, finds the lowest value, and moves it to the front of the array. This loop must loop through one less value each time it runs.
#     An outer loop that controls how many times the inner loop must run. For an array with n values, this outer loop must run n−1 times.


my_array = [64, 34, 25, 5, 22, 11, 90, 12]
my_array2 = [34, 7, 23, 32, 5, 62, 32, 1, 99, 12]

def selection_sort(my_array):
    n = len(my_array)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if my_array[j] < my_array[min_index]:
                min_index = j
        my_array[i], my_array[min_index] = my_array[min_index], my_array[i]

    return my_array

print('Sorted array:', selection_sort(my_array2))
# print("Sorted array", my_array)