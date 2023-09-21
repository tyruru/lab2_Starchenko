import math

a = 1
x = 2
mu = 0

x = (1/(a * ((2*math.pi) ** 0.5))) * (math.e ** (-(((x - mu) ** 2) / (2 * a**2))))

print (x)


##############

john = 3
mary = 5
adam = 100

print(john, mary, adam, sep = ", ")

totalApple = john + mary + adam

print(totalApple)

print("Усього яблок:", totalApple)

##############

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

##############

x =  1
x = float(x)
y = 3*x**3 - 2*x**2 + 3**x - 1
print("y =", y)

##############

hours = 3 
secondsInOur = 3600 

print("Seconds in hours:", secondsInOur * hours) 
print ("Goodbye")

##############

#a = float(input("Введіть перше число: "))
#b = float(input("Введіть друге число: "))

a = 4.5
b = 0

print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
if(b != 0):
    print("a / b =", a / b)
else:
    print("can't devide by zero")

print("\nThat's all, folks!")

##############

# x = float(input("Enter value for x: "))

x = -5.0

y = 1/(x+1/(x+1/(x+1/(x+1/x))))

print("y =", y)

##############

# hour = int(input("Starting time (hours): "))
# mins = int(input("Starting time (minutes): "))
# dura = int(input("Event duration (minutes): "))

hours = 0
minutes = 1
duration =   2939

temp = duration + minutes
while (True):
    # если минут >= чем 60, то отнимаем 60 у минут и добавляем в час +1
    if(temp >=60): 
        hours += 1
        temp -=60
    else:
        break
        # если часов больше чем 24 - онуляем их
    if(hours >=24): 
        hours = 0
    

newMinutes = temp

print(hours, newMinutes, sep=":")

##############



