import random

board = []

def PlayerNumValidation(num):
    global board
    try:
        global answer
        answer = int(num)
        if answer < 1 or answer > 9:
            return False
        
        for i in range(3):
            for j in range (3):
                if answer == board[i][j]:
                    return True
                
        print("Поле уже занято. Попробуйте снова!")
        return False
    
    except ValueError:
        print("Не верное значение")
        return False
    
def BotNumValidation(answer):
    global board
    for i in range(3):
            for j in range (3):
                if answer == board[i][j]:
                    return True
                
    return False
    
def CreateBoard():
    global board
    a = 1
    for i in range(3):
        row = []
        for j in range(3):
            row.append(a)
            a += 1
        board.append(row)

    return board

def PrintBoard():
    global board
    print( "+---------+---------+---------+")
    print( "|         |         |         |")
    print(f"|    {board[0][0]}    |    {board[0][1]}    |    {board[0][2]}    |")
    print( "|         |         |         |")
    print( "+---------+---------+---------+")
    print( "|         |         |         |")
    print(f"|    {board[1][0]}    |    {board[1][1]}    |    {board[1][2]}    |")
    print( "|         |         |         |")
    print( "+---------+---------+---------+")
    print( "|         |         |         |")
    print(f"|    {board[2][0]}    |    {board[2][1]}    |    {board[2][2]}    |")
    print( "|         |         |         |")
    print( "+---------+---------+---------+")

def MakeMove(num, symbol):
    global board
    a = 1
    for i in range(3):
        for j in range(3):
            if a == num:
                board[i][j] = symbol
                return board
            else: 
                a += 1     
   
def CheckWinner():
    global board
    #Если есть одинаковые символы в рядке
    for row in range (3):
            if board [row][0] == board[row][1] and board[row][0] == board [row][2]:
                print(f"{board[row][0]} WINNER")
                return True

    #Если есть одинаковые символы в столбце
    for column in range (3):
        if board [0][column] == board[1][column] and board[0][column] == board [2][column]:
                print(f"{board[0][column]} WINNER")
                return True


    #Если есть одинаковые символы в диагоналях
    if board[0][0] == board [1][1] and board [0][0] == board[2][2]:
        print(f"{board[0][0]} WINNER")
        return True

    if board[0][2] == board [1][1] and board [0][2] == board[2][0]:
        print(f"{board[0][2]} WINNER")
        return True

    return False

def CheckDraw():
    global board
    a = 1
    for i in range (3):
        for j in range (3):
            if a == board[i][j]:
                return False
            else:
                a += 1

    print("Ничья")
    return True

while True:
    
    player = 0
    CreateBoard()
    MakeMove(5, "X")
    PrintBoard()

    while True:
        if player % 2 == 0:
            answer = input("Введите значение: ")
            if not PlayerNumValidation(answer):
                continue

            MakeMove(answer, 'O')
            player += 1
            PrintBoard()

        else:
            answer = random.randint(1,9)

            while BotNumValidation(answer) == False:
                if answer < 9:
                    answer += 1

                else: 
                    answer = 1
            
            MakeMove(answer, 'X')
            player += 1
            PrintBoard()

        if CheckWinner():
            break
        if CheckDraw():
            break

    print("\nСпасибо за игру!")
   






