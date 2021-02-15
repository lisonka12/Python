my_file = []
while True:
    line = input("Enter text: ")
    if line == '':
        print(my_file)
        exit()
    else:
        newline = line + '\n'
        my_file.append(newline)

    with open("text.txt", "w") as file_obj:
        file_obj.writelines(my_file)