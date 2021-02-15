subject = {}
with open('file.txt', 'r') as file_obj:
    for line in file_obj:
        lesson, lecture, practice, lab = line.split()
        subject[lesson] = int(lecture) + int(practice) + int(lab)
    print(f'Hours - \n {subject}')


#file.txt
#Informatic 100 50 20
#Physics 30 0 10
#PE 0 30 0