# Radix Sort Algorithm

This radix sort algorithm sorts an array by individual digits, startting with the least significant digit (the rightmost one).
The radix (or base) is the number of unique digits in a number system. In the decimal system we normally use, there are 10 different digits from 0 till 9.

Radix Sort uses the radix so that decimal values are put into 10 different buckets (or containers) corresponding to the digit that is in focus, 
then put back into the array before moving on to the next digit.

Radix Sort is a non comparative algorithm that only works with non negative integers.

## How it works:

    1. Start with the least significant digit (rightmost digit).
    2. Sort the values based on the digit in focus by first putting the values in the correct bucket based on the digit in focus, and then put them back into array in the correct order.
    3. Move to the next digit, and sort again, like in the step above, until there are no digits left.

## Stable Sorting

Radix Sort must sort the elements in a stable way for the result to be sorted correctly.

A stable sorting algorithm is an algorithm that keeps the order of elements with the same value before and after the sorting. Let's say we have two elements "K" and "L", where "K" comes before "L", and they both have value "3". A sorting algorithm is considered stable if element "K" still comes before "L" after the array is sorted.

it is important for Radix Sort that the the sorting is done in a stable way because the elements are sorted by just one digit at a time.

## Radix Sort Implementation

### To implement the Radix Sort algorithm we need:

    An array with non negative integers that needs to be sorted.
    A two dimensional array with index 0 to 9 to hold values with the current radix in focus.
    A loop that takes values from the unsorted array and places them in the correct position in the two dimensional radix array.
    A loop that puts values back into the initial array from the radix array.
    An outer loop that runs as many times as there are digits in the highest value.
