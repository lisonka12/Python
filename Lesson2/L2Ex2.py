my_list = []
n = int(input('Enter the number of elements: '))

l = 0

while l < n:
    my_list.append(input('Enter the element: '))
    l = l + 1

print(my_list)

i = 0

for element in range(int(l//2)):
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    i = i + 2

print(my_list)