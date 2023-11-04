
# while True:
#     try:
#         while True:
#             date = input("Введіть дату народження у форматі YYYYMMDD:")
#             if(len(date) == 8):
#                 break
#             else:
#                 print("Неверное значение!")

#         while True:
#             sum = 0
#             for simbol in date:
#                 sum += int(simbol)

#             date = str(sum)

#             if len(date) == 1:
#                 break

#         print(sum)
#         break

#     except ValueError:
#         print("Неверное значение!")


# try:
#     print("Let`s try to do this")
#     print("#"[2])
#     print("We succeeded!")
# except:
#     print("We failed")
# print("We're done")

try:
    print("alpha"[1/0])
except ZeroDivisionError:
    print("zero")
except IndexError:
    print("index")
except:
    print("some")