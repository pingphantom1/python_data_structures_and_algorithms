# Bubble Sort is an algorithm that sorts an array from the lowest value to the highest value.

# How it works:

#     Go through the array, one value at a time.
#     For each value, compare the value with the next value.
#     If the value is higher than the next one, swap the values so that the highest value comes last.
#     Go through the array as many times as there are values in the array.

my_array = [64, 34, 25, 30, 11, 9, 16, 12, 22, 11, 90, 5]

n = len(my_array)
for i in range(n - 1):
    swapped = False
    for j in range(n - i - 1):
        if my_array[j] > my_array[j + 1]:
            my_array[j], my_array[j + 1] = my_array[j + 1], my_array[j]
            swapped = True
    if not swapped:
        break


print("Sorted array:", my_array)



# Sort the dictionary elements in the list below based on their transaction amount using bubble sort
elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]

def bubble_sort(list_to_sort):
    list_length = len(list_to_sort)
    for i in range(list_length - 1):
        swapped = False
        for j in range(list_length - i - 1):
            if list_to_sort[j]['transaction_amount'] > list_to_sort[j + 1]['transaction_amount']:
                list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j + 1], list_to_sort[j]
                swapped = True

        if not swapped:
            break

    return list_to_sort


print(bubble_sort(elements))



# A more dynamic way to do the sorting in ascending order or descending order when needed
def dynamic_bubble_sort(list_to_sort, reverse=False):
    list_length = len(list_to_sort)
    
    for i in range(list_length - 1):
        swapped = False
        for j in range(list_length - i - 1):
            curr = list_to_sort[j]['transaction_amount']
            nxt = list_to_sort[j + 1]['transaction_amount']
            
            # Combine the direction logic cleanly
            if (reverse and curr < nxt) or (not reverse and curr > nxt):
                list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j + 1], list_to_sort[j]
                swapped = True

        if not swapped:
            break

    return list_to_sort

# Test ascending (default)
print(dynamic_bubble_sort(elements))

# Test descending
print(dynamic_bubble_sort(elements, reverse=True))