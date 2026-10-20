leaderboard = [
    {'name': 'zara',  'score': 1200, 'level': 5},
    {'name': 'alex',  'score': 1500, 'level': 8},
    {'name': 'bob',   'score': 1200, 'level': 4},
    {'name': 'chris', 'score': 900,  'level': 3},
    {'name': 'anna',  'score': 1500, 'level': 7},
]

def bubble_sort(list_to_sort):
    list_length = len(list_to_sort)
    for i in range(list_length - 1):
        swapped = False
        for j in range(list_length - i - 1):
            curr_score = list_to_sort[j]['score']
            next_score = list_to_sort[j + 1]['score']
            curr_name = list_to_sort[j]['name']
            next_name = list_to_sort[j + 1]['name']

            if (curr_score < next_score) or (curr_score == next_score and curr_name > next_name):
                list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j + 1], list_to_sort[j]
                swapped = True
            

        if not swapped:
            break

    return list_to_sort

print("Sorted leaderboard", bubble_sort(leaderboard))