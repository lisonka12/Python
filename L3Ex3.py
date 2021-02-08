a = int(input('Enter 1st argument: '))
b = int(input('Enter 2nd argument: '))
c = int(input('Enter 3rd argument: '))

def my_func(a, b, c):
    sequence = [a, b, c]
    total = []
    max1 = max(sequence)
    total.append(max1)
    sequence.remove(max1)
    max2 = max(sequence)
    total.append(max2)
    print(sum(total))

my_func(a, b, c)