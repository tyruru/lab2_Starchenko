def printStudents(students):
    for lastName in students:
        adding = 0
        counter = 0
        for score in students[lastName]:
            adding += score
            counter += 1
            print (lastName, adding / counter)


students = {}

while True:
    name = input("Введіть імʼя студента:")
    if name == '':
        break

    lastName = input("Введіт прізвище:")
    if lastName == '':
        break

    kurs = int(input("Введіть номер курсу:"))
    if kurs < 1:
        break

    # if lastName in students:
    students[lastName] = {"name " : name, "kurs" : kurs}
    # else:
    #     students[lastName] = {"name " : name, "kurs" : kurs}
    

printStudents(students)

# for student in students["1"]:
#     print(student["lastName"])
