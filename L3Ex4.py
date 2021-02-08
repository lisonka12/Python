x = int(input('Enter number: '))
y = int(input('Enter extent: '))

def my_func(x, y):
    return 1 / x ** abs(y)

print(my_func(x, y))