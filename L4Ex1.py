from sys import argv

name, time, rate, bonus = argv
try:
    time = int(time)
    rate = int(rate)
    bonus = int(bonus)
    salary = time * rate + bonus
    print(f'Employee salary  {salary}')
except ValueError:
    print('Not a number')