
def playGame():
    exit = False  #exit is the variable that will break us out of the while loop
    #grid is a 2d array to keep track of the board
    grid = [[" ",'|'," ",'|'," "],["______"],[" ",'|'," ","|"," "],["______"],[" ",'|'," ",'|'," "]] 
    #see below for showBoard method
    showBoard(grid)
    while not(exit): #set exit to True when you want to stop playing
        turn = [8,8] #turn will be coordinates the player uses.  set to 8/8 for debugging.
        print("Type 'Exit' at any time to quit")
        # get coordinates from X player
        turn = xTurn() 
        #check for exit
        if turn ==[8,8]:
            exit = True 
            break
        #put x's play on the board
        grid = translateToBoard(turn, grid,"x")
        #show the board
        showBoard(grid)
        #check for winner
        exit = checkForWin(grid)
        #check for exit
        if exit: 
            break
        #repeat for O player
        turn = oTurn()
        if turn ==[8,8]:
            exit = True
            break
        grid = translateToBoard(turn, grid,"o")
        showBoard(grid)
        exit = checkForWin(grid)
        if exit: 
            break
        #just in case they haven't figured out the "type exit to exit" thing
        if input("Exit? Y/N  ").lower() == ("y" or "exit"):
            exit = True

#showBoard takes the current state of the board and displays it
#note: all this does is print, so it is a 'void' function
#     
def showBoard(board):
    print("           ")
    count = 0
    currentLine = ""
    for y in board:
        currentLine ="   "
        count = count +1
        #if the line is even, that means there's only one entry: _____
        #if i just just a standard nested for loop, it would throw an out of bounds exception on even rows
        if count%2 == 0:
            currentLine = currentLine+ y[0]
        else:
            for x in y:
                #because its a string, i'm concatenating the seperate array indexes, rather than just printing
                currentLine = currentLine+x
        print(currentLine)
    print("       ")


#X Turn conducts the X player's turn, and returns the coordinates that the player wants to put an X on
def xTurn():
    print("X turn")
    column = input("What Column? 1, 2, or 3 ")
    row = input("What Row? 1, 2, or 3 ")
    #if the player wants to exit, return a grid that we KNOW is out of bounds
    #note: setting Exit to true inside this function won't trigger the while loop in playGame()
    if ((column.lower() == "exit") or (row.lower() ==exit)):
        return [8,8]
    else:
        #return the coordinates
        return [int(column), int(row)]


#Same as X turn, but for O player
def oTurn():
    
    print("O turn")
    column = input("What Column? 1, 2, or 3 ")
    row = input("What Row? 1, 2, or 3 ")
    if ((column.lower() == "exit") or (row.lower() ==exit)):
        return [8,8]
    else:
        return [int(column), int(row)]


#Translate board takes the current player's coordinates, the current board, and the player,
# and updates the board, then returns it
def translateToBoard(coordinates, board, player):
    grid = board
    column = coordinates[0]
    row = coordinates[1]
    ans = [8,8]
    if column == 1:     #because the player enters 1,2, or 3
        ans[0] = 0      #we have to translate it to coordinates that correspond
    elif column == 2:   #to the 2D array the computer is using
        ans[0] = 2
    elif column == 3:
        ans[0] = 4
    if row == 1:
        ans[1] = 0
    elif row == 2:
        ans[1] = 2
    elif row == 3:
        ans[1] = 4
    boardColumn = ans[0]
    boardRow = ans[1]
    #here, we check to see if that space is occupied

    if (grid[boardRow][boardColumn] != " "):
        #if it is, we have to redo the current player's turn
        if player == "x":
            newCoordinates = xTurn()
            #note, this calls the function recursively, so we have to pass the arguments into itself
            grid = translateToBoard(newCoordinates,grid,player)
            return grid
        else:
            newCoordinates = oTurn()
            grid = translateToBoard(newCoordinates,grid,player)
            return grid
    grid[boardRow][boardColumn] = player
    return grid

#takes the current state of the board and checks for a winner
def checkForWin(board):
    #Below are the 8 possible winning board states
    if ((board[0][0] == board[0][2]==board[0][4]) and (board[0][0] != " ")):
        input(board[0][0]+ ' Wins!!')
        return True
    elif ((board[0][0] == board[2][2]==board[4][4])and (board[0][0] != " ")):
        input(board[0][0]+ ' Wins!!')
        return True
    elif ((board[0][0] == board[2][0]==board[4][0])and (board[0][0] != " ")):
        input(board[0][0]+ ' Wins!!')
        return True
    elif ((board[0][4] == board[2][4]==board[4][4])and (board[0][4] != " ")):
        input(board[0][4]+ ' Wins!!')
        return True
    elif ((board[4][0] == board[4][2]==board[4][4])and (board[4][0] != " ")):
        input(board[4][0]+ ' Wins!!')
        return True
    elif ((board[0][2] == board[2][2]==board[4][2])and (board[0][2] != " ")):
        input(board[0][2]+ ' Wins!!')
        return True
    elif ((board[2][0] == board[2][2]==board[2][4])and (board[2][0] != " ")):
        input(board[2][0]+ ' Wins!!')
        return True
    elif ((board[4][0] == board[2][2]==board[0][4])and (board[4][0] != " ")):
        input(board[4][0]+ ' Wins!!')
        return True
    else:
        return False
    

    #if it's none of those, nobody's won yet
    

    


playGame()