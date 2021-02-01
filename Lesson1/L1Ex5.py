p = input('Enter proceeds: ')
p = int(p)
c = input('Enter costs: ')
c = int(c)

a = p - c

if a > 0:
    print('There is a profit')
    r = p / c
    print('The profitability of proceeds is ', r)
    n = input('Enter the number of employees: ')
    n = int(n)
    pn1 = a / n
    print('The profit per employee is ', pn1)
else:
    print('There is a loss')