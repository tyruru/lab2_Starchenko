hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

num = int(input("Введіть число: "))
hat_list[2] = num
print(f"Новий массив чисел:", hat_list)

del hat_list[len(hat_list)-1]
print(f"Массив чисел без останнього елемента:", hat_list)

print("Довжина массиву:", len(hat_list))

########################################################

numsList = [1,6,4,8,4,0,-6,0,0,0,0,-88]

flag = True
while flag == True:
    flag = False
    for i in range(len(numsList)-1):
        if(numsList[i] > numsList[i+1]):
            temp = numsList[i]
            numsList[i] = numsList[i+1]
            numsList[i+1] = temp
            flag = True
  


print(numsList)


########################################################

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
uniqueArray = []

length = 1
for i in range (len(my_list)):
    if(my_list[i] not in uniqueArray):
        uniqueArray.append(my_list[i])

print("The list with unique elements only:")
print(uniqueArray)

########################################################

field = [["_" for i in range(8)] for j in range (8)]

field[0][0] = "T"
field[0][7] = "T"
field[7][0] = "T"
field[7][7] = "T"

for row in field:
    print(' '.join(row))

########################################################
