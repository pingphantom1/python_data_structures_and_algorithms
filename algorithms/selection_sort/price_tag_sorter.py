catalog = [
    {'item': 'Wireless Mouse', 'price': 29.99},
    {'item': 'Mechanical Keyboard', 'price': 89.50},
    {'item': 'USB-C Cable', 'price': 12.00},
    {'item': 'Gaming Monitor', 'price': 249.99},
    {'item': 'Desk Lamp', 'price': 45.00}
]

def selection_sort(list_to_sort):
    n = len(list_to_sort)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if list_to_sort[j]['price'] < list_to_sort[min_index]['price']:
                min_index = j
        list_to_sort[i], list_to_sort[min_index] = list_to_sort[min_index], list_to_sort[i]

    return list_to_sort


sorted_price_tags = selection_sort(catalog)
print("Sorted list: ", sorted_price_tags)