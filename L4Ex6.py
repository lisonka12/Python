from itertools import count

for element in count(int(input('Enter number: '))):
    print(element)

from itertools import cycle

my_list = [True, 'ABC', 123, None]
for element in cycle(my_list):
    print(element)