def division(*args):
    try:
        dividend = int(input('Enter the dividend: '))
        divider = int(input('Enter the divider: '))
        calcresult = dividend / divider
    except ZeroDivisionError:
        return('The devider cannot be zero')
    return calcresult

print(f'{division()}')