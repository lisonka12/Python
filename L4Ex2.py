my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_new_list = [element for i, element in enumerate(my_list) if my_list[i - 1] < my_list[i]]
print(f'Current list {my_list}')
print(f'New list {my_new_list}')