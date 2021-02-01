a = input('Enter number: ')
a = int(a)
b = 0

while a > 0:
    c = a % 10
    a //= 10
    if c > b:
        b = c

print("The greatest is: ", b)