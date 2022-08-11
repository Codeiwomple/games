"""A basic command line tic tac toe game"""
import os
import sys

gameBoard       = [['' for j in range(3)] for i in range(3)]
displayBoard    = [[' ' for j in range(46)] for i in range(25)]

def main():
    """Main method to control game"""
    player = 'X'#Player x to go first
    moveCounter = 1 #Keeps track of how many turns have been taken

    #Setup game
    initGame()
    printInitScreen()

    while True:
        #Get player input
        square = input(f"Player {player}, choose your square ->")

        if validateInput(square):
            updateGameBoard(square, player)
            updateDisplayBoard(square, player)
            printDisplayBoard()

            if moveCounter >= 4:
                checkIfWon(player)

            #Switch player
            if player == 'X':
                player = 'O'
            else:
                player = 'X'

            moveCounter += 1

        else:
            print("Please try again")

def initGame():
    """Create and set up game components"""

    #Fill board
    for i in range(25):
        #If on a row boarder set to _
        if i == 8 or i == 17:
            for j in range(46):
                displayBoard[i][j] = '_'
        else:
            for j in range(46):
                #If on column boarder set |
                if j == 15 or j == 31:
                    displayBoard[i][j] = '|'

    #Put numbers in corner of square
    displayBoard[0][0]   = '1'
    displayBoard[0][16]  = '2'
    displayBoard[0][32]  = '3'
    displayBoard[9][0]   = '4'
    displayBoard[9][16]  = '5'
    displayBoard[9][32]  = '6'
    displayBoard[18][0]  = '7'
    displayBoard[18][16] = '8'
    displayBoard[18][32] = '9'


def validateInput(input):
    """Validates user input"""
    #Check given char is allowed
    try:
        square = int(input[0]) #Check first char of input is number
    except:
        return False

    #Check nothing already in that square
    #Get the gameBoard index of users chosen square
    index = numToIndex(input)
    if gameBoard[index[0]][index[1]] != '':
        return False

    #If all ok
    return True

def updateGameBoard(input, player):
    """Keeps track of users moves"""
    #Update the array with new move
    index = numToIndex(input[0])
    gameBoard[index[0]][index[1]] = player

def printDisplayBoard():
    """Prints a string representation of board"""
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen

    for row in displayBoard:
        print(''.join(row))

    print("")

def checkIfWon(player):
    """Checks to see if the last move won the game"""
    gameWon = False
    #Check Horiz
    for row in gameBoard:
        if row[0] == row[1] == row[2] == player:
            gameWon = True

    #Check Vert
    for i in range(3):
        if gameBoard[0][i] == gameBoard[1][i] == gameBoard[2][i] == player:
            gameWon = True

    #Check Diag
    if gameBoard[0][0] == gameBoard[1][1] == gameBoard[2][2] == player:
        gameWon = True
    if gameBoard[0][2] == gameBoard[1][1] == gameBoard[2][0] == player:
        gameWon = True

    if gameWon:
        print(f"Congratualtions player {player}, you won!")
        sys.exit()

def printGameBoard():
    """For debugging, prints gameboard"""
    for row in gameBoard:
        print(row)

def printInitScreen():
    """Prints the initial welcome screen"""
    header = """
    888   d8b        888                   888
    888   Y8P        888                   888
    888              888                   888
    888888888 .d8888b888888 8888b.  .d8888b888888 .d88b.  .d88b.
    888   888d88P"   888       "88bd88P"   888   d88""88bd8P  Y8b
    888   888888     888   .d888888888     888   888  88888888888
    Y88b. 888Y88b.   Y88b. 888  888Y88b.   Y88b. Y88..88PY8b.
     "Y888888 "Y8888P "Y888"Y888888 "Y8888P "Y888 "Y88P"  "Y8888
    """
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
    print(header)
    input("Press enter to start!")
    printDisplayBoard()

def updateDisplayBoard(num, player):
    """Add the players shape to the chosen position on display board"""
    shapes = {"X":
              [[' ',' ',' ',' ','?','8','8','8','8','P',' ',' ',' ',' '],
               [' ',' ',' ',' ',' ','`','8','8','`',' ',' ',' ',' ',' '],
               ['8','b',',','_',' ',' ','8','8',' ',' ','_',',','d','8'],
               ['8','8','8','8','8','S','I','C','K','8','8','8','8','8'],
               ['8','P','~',' ',' ',' ','8','8',' ',' ',' ','~','?','8'],
               [' ',' ',' ',' ',' ',',','8','8','.',' ',' ',' ',' ',' '],
               [' ',' ',' ',' ','d','8','8','8','8','b',' ',' ',' ',' ']],
               "O":
              [[' ',' ',' ',' ',' ',' ','%','%',' ',' ',' ',' ',' ',' '],
               [' ',' ',' ',' ','%','%',' ',' ','%','%',' ',' ',' ',' '],
               [' ',' ','%','%',' ',' ',' ',' ',' ',' ','%','%',' ',' '],
               ['%','%',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','%','%'],
               [' ',' ','%','%',' ',' ',' ',' ',' ',' ','%','%',' ',' '],
               [' ',' ',' ',' ','%','%',' ',' ','%','%',' ',' ',' ',' '],
               [' ',' ',' ',' ',' ',' ','%','%',' ',' ',' ',' ',' ',' ']]}

    shape = shapes[player]
    num = int(num[0])

    offsets = [[0 ,0],[0 ,16],[0 ,32],
               [9 ,0],[9 ,16],[9 ,32],
               [17,0],[17,16],[17,32]]

    iOffset = offsets[num-1][0]
    jOffset = offsets[num-1][1]

    for i in range(iOffset, iOffset + 7):
        for j in range(jOffset, jOffset + 14):
            displayBoard[i+1][j] = shape[i - iOffset][j - jOffset]

def numToIndex(num):
    """Returns index [i,j] for given 'square' on board"""
    num = int(num[0])
    indexList = []
    for i in range (3):
        for j in range(3):
            indexList.append([i,j])

    return indexList[int(num)-1]

if __name__ == '__main__':
    main()
