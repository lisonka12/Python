n_month = int(input('Enter the month number: '))

season_list = ['winter', 'spring', 'summer', 'autumn']
season_dict = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'autumn'}

if n_month == 1 or n_month == 2 or n_month == 12:
        print(season_dict.get(1))
elif n_month >= 3 and n_month <= 5:
    print(season_dict.get(2))
elif n_month >= 6 and n_month <= 8:
    print(season_dict.get(3))
elif n_month >= 9 and n_month <= 11:
    print(season_dict.get(4))
else:
        print('No such month')