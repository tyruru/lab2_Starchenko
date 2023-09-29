##Приклад введення: `spathiphyllum`
##Очікуваний вивід: `No, I want a big Spathiphyllum!`
##Приклад введення: `pelargonium`
#Очікуваний вивід: `Spathiphyllum! Not pelargonium!`
#Приклад введення: `Spathiphyllum`
#Очікуваний вивід: `Yes - Spathiphyllum is the best plant ever!`

answer = "Spathiphyllum"

while True:
    str = input()
    if(str == answer):
        print("Yes - Spathiphyllum is the best plant ever!")
        break
    elif(str == answer.lower()):
        print("No, I want a big Spathiphyllum!")
    else:
        print("Spathiphyllum! Not ", str)
            