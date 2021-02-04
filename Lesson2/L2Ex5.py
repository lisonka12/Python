my_list = [7, 5, 3, 3, 2]

rating = int(input('Enter the next rating number: '))

for element in range(len(my_list)):
    if my_list[element] == rating:
            my_list.insert(element + 1, rating)
    elif my_list[0] < rating:
            my_list.insert(0, rating)
    elif my_list[-1] > rating:
            my_list.append(rating)
    elif my_list[element] > rating and my_list[element + 1] < rating:
            my_list.insert(element + 1, rating)

print(f'The current rating list is: {my_list}')