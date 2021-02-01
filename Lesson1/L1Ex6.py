a = input('Enter the result of the 1st day: ')
a = int(a)
b = input('Enter the desired result: ')
b = int(b)

c = a
i = 1

print('Day ', i, ': ', c)
while c < b:
    i = i + 1
    c = round(c * 1.1, 2)
    print('Day ', i, ': ', c)


print('On day ', i, ' the the result will be achieved')