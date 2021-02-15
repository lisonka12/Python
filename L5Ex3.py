my_text = ['Ivanov: 25000\n', 'Sidorov: 10000\n', 'Mihailov: 30000\n']

try:
    with open("salary_list.txt", 'w+') as file_obj:
        file_obj.writelines(my_text)
finally:
    file_obj.close()

sum = 0
count = 0
employee = []
with open("salary_list.txt", "r") as file_obj:
    for line in file_obj:
        print(line, end="")
        tokens = line.split(':')
        if int(tokens[1]) <= 20000:
            employee.append(tokens[0])
        sum += int(tokens[1])
        count += 1
result = sum / count
print(f"Employee(s) with the lowest salary: {employee}")
print(f"Average salary: {result}")
