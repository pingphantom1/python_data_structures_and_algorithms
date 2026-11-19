
# List of numbers that we want to sort
myArray = [170, 45, 75, 90, 802, 24, 2, 66]

# Display the original, unsorted array
print("Original array: ", myArray)

# Create 10 empty buckets (indexes 0 to 9).
# Each bucket represents a possible digit from 0 to 9.
radixArray = [[], [], [], [], [], [], [], [], [], []]

# Find the largest number in the array.
# This helps determine how many digits we need to process.
maxVal = max(myArray)

# Set the initial exponent to 1.
# exp = 1  represents the units (ones) digit.
# exp = 10 represents the tens digit.
# exp = 100 represents the hundreds digit.
exp = 1

# Continue sorting as long as there are digits left
# to process in the largest number.
while maxVal // exp > 0:

    # Remove every number from the original array
    # and place it into the appropriate digit bucket.
    while len(myArray) > 0:

        # Remove the last element from the array.
        val = myArray.pop()

        # Extract the digit at the current position.
        # For example:
        # If val = 170 and exp = 1:
        # (170 // 1) % 10 = 0
        # Therefore, the number goes into bucket 0.
        radixIndex = (val // exp) % 10

        # Place the number into its corresponding bucket.
        radixArray[radixIndex].append(val)

    # Collect the numbers from the buckets
    # and put them back into the original array.
    for bucket in radixArray:

        # Continue until the current bucket is empty.
        while len(bucket) > 0:

            # Remove the last number from the bucket.
            val = bucket.pop()

            # Return the number to the original array.
            myArray.append(val)

    # Move to the next digit position.
    # 1 -> 10 -> 100 -> 1000, and so on.
    exp *= 10

# Display the final sorted array.
print("Sorted Array: ", myArray)
