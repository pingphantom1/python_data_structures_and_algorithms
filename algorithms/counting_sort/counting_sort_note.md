
# Counting Sort

## Introduction

The **Counting Sort** algorithm sorts an array by counting the number of times each value occurs.

Counting Sort does not compare values like the previous sorting algorithms we have looked at. It only works on **non-negative integers**.

Furthermore, Counting Sort is fast when the range of possible values (**K**) is smaller than the number of values (**N**).

## How Counting Sort Works

1. Create a new array for counting how many times each value occurs.
2. Go through the array that needs to be sorted.
3. For each value, count it by increasing the counting array at the corresponding index.
4. After counting the values, go through the counting array to create the sorted array.
5. For each count in the counting array, create the correct number of elements, with values corresponding to the counting array index.

## Conditions for Counting Sort

These are the reasons why Counting Sort is said to only work for a limited range of non-negative integer values:

### 1. Integer Values

Counting Sort relies on counting occurrences of distinct values, so they must be integers.

With integers, each value fits with an index (for non-negative values), and there is a limited number of different values. This means that the number of possible different values (**K**) is not too large compared to the number of values (**N**).

### 2. Non-Negative Values

Counting Sort is usually implemented by creating an array for counting.

When the algorithm goes through the values to be sorted, a value **X** is counted by increasing the counting array value at index **X**.

If we tried sorting negative values, we would encounter a problem when sorting a value such as **-3**, because index -3 would be outside the counting array.

### 3. Limited Range of Values

If the number of possible different values to be sorted (**K**) is larger than the number of values to be sorted (**N**), the counting array we need for sorting will be larger than the original array that needs sorting.

As a result, the algorithm becomes ineffective.

## Counting Sort Implementation

To implement the Counting Sort algorithm in a programming language, we need:

1. An array containing the values to sort.
2. A `countingSort` method that receives an array of integers.
3. An array inside the method to keep count of the values.
4. A loop inside the method that counts the values by incrementing elements in the counting array.
5. A loop inside the method that recreates the array using the counting array, ensuring that the elements appear in the correct order.

### Determining the Size of the Counting Array

One more thing: We need to find out what the **highest value** in the array is so that the counting array can be created with the correct size.

For example, if the highest value is **5**, the counting array must contain **6 elements** in total to be able to count all possible non-negative integers:

- 0
- 1
- 2
- 3
- 4
- 5

Therefore, the size of the counting array is:

```text
Maximum Value + 1
```

## Counting Sort vs. Comparison-Based Sorting Algorithms

Unlike **Bubble Sort, Selection Sort, Insertion Sort, or Quicksort**, which are comparison-based sorting algorithms, Counting Sort is a **non-comparative sorting algorithm**.

Instead of comparing elements against one another, Counting Sort works by counting the exact occurrences (frequencies) of each unique value.

## How Counting Sort Works Conceptually

### 1. The Core Idea

If you know how many times each number appears in an array, you can reconstruct the sorted array in order without making a single comparison.

### 2. The Frequency Map

You tally up the counts of every number from **0 (or the minimum value)** up to the maximum value.

### 3. Reconstruction

You loop through your tallies in order and write each number back into the array as many times as it appeared.

### 4. Efficiency

Because it does not perform pairwise comparisons, Counting Sort can run in:

$$
\mathcal{O}(N + K)
$$

Where:

- **N** is the number of elements in the array.
- **K** is the maximum value (or the range of values, depending on the implementation).

This makes Counting Sort extremely fast when the range of numbers is small compared to the number of elements being sorted.
