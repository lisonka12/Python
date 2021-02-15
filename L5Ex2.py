my_text = ['Good\n', 'Morning\n', 'World\n']
with open("text.txt", 'w+') as file_obj:
    file_obj.writelines(my_text)
with open("text.txt") as file_obj:
    lines = 0
    letters = 0
    for line in file_obj:
        lines += line.count("\n")
        letters = len(line)-1
        print(f"{letters} - letters in a line")
    print(f"Number of strings: {lines}")