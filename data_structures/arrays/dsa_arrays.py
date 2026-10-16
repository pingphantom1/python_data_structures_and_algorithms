my_array = [7, 12, 9, 8, 4, 7, 3, 11, 9]
minVal = my_array[0]    # Step 1 minimum value = first value

for i in my_array:  # Step 2 Check values one after the other 
    if i < minVal:  # Step 3 Compare values with minVal 
        minVal = i   # Store value to minVal if less than current minVal value


print('Lowest Value: ', minVal)  #Step 4 Display minimum value