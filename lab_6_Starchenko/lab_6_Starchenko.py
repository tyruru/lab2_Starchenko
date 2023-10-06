
def is_year_leap(year):
     
    if (year < 1582):
     return False

    elif(year %4 != 0):
        return False

    elif(year % 100 != 0):
       return True

    elif(year % 400 != 0):
       return False

    else:   
         return True


test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]

for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"->",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
    	print("Failed")

##############################################################################

def days_in_month(year, month):
     days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

     if month < 1 or month > 12 or year < 1:
        return None
     
     # Если год высокосный и это февраль
     if month == 2 and (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        return 29
     
     return days_per_month[month - 1]


test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")


##############################################################################


def day_on_year(year, month, day):
         days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
         if(month < 1 or month > 12 or day < 1 or year < 1):
                 return None
         
         #если высокосный - добавим один день до февраля
         if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
                 days_per_month[1] = 29
         
         #не больше ли дней чем есть в месяце
         if(day > days_per_month[month-1]):
                 return None
 
         answer = 0
         for i in range(month-1):
                 answer += days_per_month[i]
         
         answer += day
         return answer  


  
    
print(day_on_year(2000, 12, 31))


##############################################################################

def is_prime(num):
	devideNums = [2,3,5,7,]
	for i in range(len(devideNums)):
		if(num != devideNums[i] and num % devideNums[i] == 0 or num ** 0.5 % 1 == 0 ):
			return False
	return True
		

count = 0
for i in range(1, 2000):
	if is_prime(i + 1):
			count += 1
			print(i + 1, end=" ")
print(count)


##############################################################################

##############################################################################

def if_a_triangle(a,b,c):
    return a < b+c and b < a+c and c < a+b

print (if_a_triangle(3,4,6))

##############################################################################

def if_a_triangle(a,b,c):
    return a < b+c and b < a+c and c < a+b

def is_a_rigth_triangle(a,b,c):
    max_side = max(a, b, c)

    # Знаходимо квадрат гіпотенузи
    max_side_square = max_side ** 2

    # Знаходимо суму квадратів інших двох сторін
    sum_of_squares = a**2 + b**2 + c**2 - max_side_square

    # Перевірка теореми Піфагора
    return max_side_square == sum_of_squares


a,b,c = 3,4,5
if(if_a_triangle(a,b,c)):
    print(is_a_rigth_triangle(a,b,c))


##############################################################################


