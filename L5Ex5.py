def summary():
    try:
        with open('numbers.txt', 'w+') as file_obj:
            line = input('Enter numbers with spaces in between: \n')
            file_obj.writelines(line)
            my_numbers = line.split()
            print(sum(map(int, my_numbers)))
    except IOError:
        print('Error')
    except ValueError:
        print('Error')
summary()