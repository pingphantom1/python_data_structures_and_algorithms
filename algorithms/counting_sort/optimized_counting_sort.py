def optimized_counting_sort(arr):
    if not arr:
        return arr

    min_val = min(arr)
    max_val = max(arr)
    
    # Calculate the range span
    range_of_elements = max_val - min_val + 1
    
    # Initialize count array with zeros, shifted by min_val
    count = [0] * range_of_elements

    # Store frequencies with the offset adjustment
    for num in arr:
        count[num - min_val] += 1

    # Clear and rebuild the array in-place, adding min_val back
    arr[:] = []
    for i, freq in enumerate(count):
        num = i + min_val
        arr.extend([num] * freq)
        
    return arr

# --- Example Usage with Negative Numbers ---
unsortedArr = [4, -2, 2, -2, 6, 3, 3, 1, 6, 5, 2, 3]
sortedArr = optimized_counting_sort(unsortedArr)
print("Sorted array:", sortedArr)