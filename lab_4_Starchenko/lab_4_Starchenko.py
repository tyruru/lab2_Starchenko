

n = int(input("Введіть n: "))
print (n>=100)


#=====================================================

a  = 5
b  = 5

if(a > b):
    print("a > b")
elif (b > a):
    print("b > a")
else:
    print("a == b")

#=====================================================

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

#=====================================================

income = float(input("Enter the annual income: "))

if(income < 85528):
    tax = (income / 100 * 18)-556.2

else:
    income -= 85528
    tax = (income / 100  * 32) + 14839.2

if(tax < 0):
    tax = 0.0
#excess

tax = round(tax, 0) 
print("The tax is:", tax, "thalers")

#=====================================================

year = int(input("Введіть рік: ") )
if (year < 1582):
    print("Not within the Gregorian calendar period.")

elif(year %4 != 0):
    print("Common year`")

elif(year % 100 != 0):
    print("Leap year")

elif(year % 400 != 0):
    print("Common year")

else:
    print("Leap year")

#=====================================================

odd_numbers = 0
even_numbers = 0

# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution.
while number != 0:
    # Check if the number is odd.
    if number % 2 == 1:
        # Increase the odd_numbers counter.
        odd_numbers += 1
    else:
        # Increase the even_numbers counter.
        even_numbers += 1
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))

# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)

#=====================================================

counter = 5
while counter:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)

#=====================================================

secret_number = 777
answer = 0

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

while True:
    answer = int(input("Введіть цисло"))
    if(answer == secret_number):
        print("Молодець, магле! Тепер ти вільний")
        break;

    else:
        print("Ха-ха! Ви застрягли у моїй петлі!")

#=====================================================

import time

for i in range(5):
    print(f"{i+1} Міссісіпі")
    time.sleep(1)

print ("Ready or not, here I come!")

#=====================================================

while True:
    answer = input()
    if (answer == "chupacabra"):
        print("You've successfully left the loop.")
        break


#=====================================================


word_without_vowels = input("Введіть слово").upper()
alphabet = "AEIOU"

for i in range(len(word_without_vowels)):
    if(alphabet.__contains__(word_without_vowels[i])):
        continue
    print(word_without_vowels[i])

#=====================================================

word_without_vowels = input("Введіть слово: ").upper()
alphabet = "AEIOU"
newWord = ""


for i in range(len(word_without_vowels)):
    if(alphabet.__contains__(word_without_vowels[i])):
        continue

    newWord += word_without_vowels[i]

print (newWord)

#=====================================================

blockCount = 1000
blockNeeded = 1
level = 0

while blockCount >= blockNeeded:
    level += 1
    blockCount -= blockNeeded + level

print (f"The height of pyramid: {level}")

#=====================================================

c0 = 15
steps = 0

while c0 != 1:
    steps += 1

    if(c0 % 2 == 0):
        c0 = c0/2

    else:
        c0 = c0 * 3 + 1
    
    print(c0)

print (f"steps = {steps}")

#=====================================================

x, y, z = 5, 10, 8

print(x > z)

print((y-5) == x)