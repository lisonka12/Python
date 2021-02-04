n_month = int(input('Enter the month number: '))

season_list = ['winter', 'spring', 'summer', 'autumn']

if n_month ==1 or n_month == 12 or n_month == 2:
        print(season_list[0])
elif n_month >= 3 and n_month <= 5:
    print(season_list[1])
elif n_month >= 6 and n_month <= 8:
    print(season_list[2])
elif n_month >= 9 and n_month <= 11:
    print(season_list[3])
else:
        print('No such month')