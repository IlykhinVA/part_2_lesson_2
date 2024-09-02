my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
list_index = 0
while len(my_list) > list_index:
    if my_list[list_index] < 0:
        break
    else:
        if my_list[list_index] != 0:
            print(my_list[list_index])
    list_index += 1

