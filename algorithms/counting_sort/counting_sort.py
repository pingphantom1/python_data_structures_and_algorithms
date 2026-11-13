def counting_sort(arr):
    # 1. Handle edge cases
    if not arr:
        return arr

    # 2. Find the maximum value to determine the range
    max_val = max(arr)
    
    # 3. Initialize a frequency list (count array) with zeros
    # We use (max_val + 1) so we can include index 0 up to max_val
    count = [0] * (max_val + 1)

    # 4. Count the frequency of each number in the original array
    for num in arr:
        count[num] += 1

    # 5. Clear the original array in-place so we can rebuild it sorted
    arr[:] = []

    # 6. Rebuild the array using the frequencies
    for num, freq in enumerate(count):
        # Extend the array by repeating 'num' 'freq' times
        arr.extend([num] * freq)
        
    return arr

unsortedArr = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
sortedArr = counting_sort(unsortedArr)
print("Sorted array:", sortedArr)