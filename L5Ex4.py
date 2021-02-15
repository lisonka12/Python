translation = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open('English_numbers.txt', 'r') as file_obj:
    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(translation[i[0]] + '  ' + i[1])
    print(new_file)

with open('Russian_numbers.txt', 'w') as file_obj_2:
    file_obj_2.writelines(new_file)