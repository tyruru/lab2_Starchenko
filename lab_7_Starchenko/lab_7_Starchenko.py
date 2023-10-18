##################################

korteg = (3,10,25,-1,0,9)

n = 10
newKorteg = ()

for num in korteg:
    if num < n:
        newKorteg += (num,)

print (newKorteg)

##################################

korteg =("apple", "souce", "Miami")
str = ', '.join(korteg)

print (str)

##################################

def printInfo(book):
    print("author:", book["avtor"])
    print("year:", book["year"])
    print("pages:", book["pages"])


books ={
    "33Bogaturya" : {"avtor" : "Shevchenko", "year" : "1337", "pages" : 1337},
    "Sherlock Holmes" : {"avtor" : "Hmelnickiy", "year" : "1978", "pages" : 10},
    "1306" : {"avtor" : "1306", "year" : "1306", "pages" : 1306}
}

answer = input("Введіть бажану книгу: ")

if answer in books:
    book = books[answer]
    printInfo(book)
else:
    print("Такой книги не существует!")

##################################

def printStudents(students):
    for lastName, info in students.items():
         print(f"\nФамилия: {lastName}", 
               f"\nИмя: {info['name']}",
               f"\nКурс: {info['kurs']}")


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

    if lastName in students:
        students[lastName] = {"name" : name, "kurs" : kurs}
    else:
         students[lastName] = {"name" : name, "kurs" : kurs}
    

printStudents(students)


##################################

def addNumber():
    name = input("Enter the contact name: ")
    if (name == ""):
        print("Wrong name!")
        return
    phoneNumber = input("Enter the number: ")
    if (phoneNumber == ""):
        print("WrongNumber!")
        return
    global contacts
    contacts[name] = {"phoneNumber" : phoneNumber}

def printContacts():
    global contacts
    for name, num in contacts.items():
        print(f"Name: {name} \nPhone number: {num['phoneNumber']}\n")


contacts = {}
addNumber()
addNumber()
printContacts()


##################################