s = input('Enter the phrase: ')

my_list = []
n = 1

space = s.count(' ') + 1

for word in range(space):
    my_list = s.split()
    if len(str(my_list)) <= 10:
        print(f' {n} {my_list [word]}')
        n = n + 1
    else:
        print(f'{n} {my_list [word] [0:10]}')
        n = n + 1