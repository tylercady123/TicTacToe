import random
import os

# Utility functions


def clearScreen():
    # Clears the console screen.
    os.system('cls' if os.name == 'nt' else 'clear')

def printIntro():
    clearScreen()
    """Prints the game intro and gets user choices."""
    clearScreen()
    print("********************************************")
    print("**                                        **")
    print("**             PYTHON TIC TAC TOE         **")
    print("**                                        **")
    print("**                Tyler Cady              **")
    print("**                                        **")
    print("********************************************")
    print("**                                        **")
    print("**  Choose a play mode:                   **")
    print("**                                        **")
    print("**    1. Pass and play                    **")
    print("**    2. Play CPU                         **")
    print("**                                        **")
    print("********************************************")
    playMode = input("Enter your choice (1 or 2): ")
    while playMode not in ['1', '2']:
        playMode = input("Invalid input. Please enter your choice (1 or 2): ")

    clearScreen()
    print("********************************************")
    print("**                                        **")
    print("**             PYTHON TIC TAC TOE         **")
    print("**                                        **")
    print("**                Tyler Cady              **")
    print("**                                        **")
    print("********************************************")
    print("**                                        **")
    print("**  Choose dimensions (3-10):             **")
    print("**                                        **")
    print("**    3. 3x3                              **")
    print("**    4. 4x4                              **")
    print("**    5. 5x5                              **")
    print("**    6. 6x6                              **")
    print("**    7. 7x7                              **")
    print("**    8. 8x8                              **")
    print("**    9. 9x9                              **")
    print("**   10. 10x10                            **")
    print("**                                        **")
    print("********************************************")
    dimensions = input("Enter your choice (3-10): ")
    while dimensions not in ['3', '4', '5', '6', '7', '8', '9', '10']:
        dimensions = input("Invalid input. Please enter your choice (3-10): ")
    clearScreen()
    return int(playMode), int(dimensions)

# Board Creation and Manipulation Functions

def createBoard(size):
    # Creates a board of size x size
    board = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append("_")
        board.append(row)
    return board

def printBoard(board, size):
    clearScreen()
    line = "********************************************"
    print("********************************************")
    print("**                                        **")
    print("**             PYTHON TIC TAC TOE         **")
    print("**                                        **")
    print("**                Tyler Cady              **")
    print("**                                        **")
    print("********************************************")

    for i in range(size):
        row_str = ""
        for j in range(size):
            row_str += board[i][j] + " "  # Add the cell value and a space
        row_spaces = len(line) - len(row_str) - 4  # 4 for the "**"
        left_spaces = row_spaces // 2
        right_spaces = row_spaces - left_spaces
        print("**" + " "*left_spaces + row_str + " "*right_spaces + "**")
    print("**                                        **")

    print(line)

# Game Logic Functions
def checkBoardFull(board):
    # Check if the board is full
    for row in board:
        if "_" in row:
            return False
    return True

def checkWin(player, board):
    # Check if the player has won
    size = len(board)
    # Check rows and columns
    for i in range(size):
        if all([board[i][j] == player for j in range(size)]) or \
           all([board[j][i] == player for j in range(size)]):
            return True
    # Check diagonals
    if all([board[i][i] == player for i in range(size)]) or \
       all([board[i][size-i-1] == player for i in range(size)]):
        return True
    return False

def checkTie(board):
    # Check if the game is a tie
    if checkBoardFull(board) and not (checkWin("X", board) or checkWin("O", board)):
        return True
    return False

def isWinnable(player, board):
    # Check if the player can win
    size = len(board)
    empty_spaces_exist = False
    # Check rows and columns
    for i in range(size):
        if board[i].count(player) == size-1:
            empty_spaces = [j for j in range(size) if board[i][j] == "_"]
            for j in empty_spaces:
                if [board[i][k] for k in range(size) if k != j].count("XO".replace(player, "")) == 0:
                    return True
            empty_spaces_exist = True
        if [board[j][i] for j in range(size)].count(player) == size-1:
            empty_spaces = [j for j in range(size) if board[j][i] == "_"]
            for j in empty_spaces:
                if [board[k][i] for k in range(size) if k != j].count("XO".replace(player, "")) == 0:
                    return True
            empty_spaces_exist = True
    # Check diagonals
    if [board[i][i] for i in range(size)].count(player) == size-1:
        empty_spaces = [i for i in range(size) if board[i][i] == "_"]
        for i in empty_spaces:
            if [board[j][j] for j in range(size) if j != i].count("XO".replace(player, "")) == 0:
                return True
        empty_spaces_exist = True
    if [board[i][size-i-1] for i in range(size)].count(player) == size-1:
        empty_spaces = [i for i in range(size) if board[i][size-i-1] == "_"]
        for i in empty_spaces:
            if [board[j][size-j-1] for j in range(size) if j != i].count("XO".replace(player, "")) == 0:
                return True
        empty_spaces_exist = True
    return empty_spaces_exist
    
def checkGameOver(board):
    if checkWin("X", board) or checkWin("O", board) or checkTie(board):
        return True
    else:
        return False

def isValidMove(board, row, col):
    # Check if the move is valid
    return board[row][col] == "_"

# Move Functions

def userMove(board):
    while True:
        row = int(input("Enter row (1-{}): ".format(len(board))))
        col = int(input("Enter column (1-{}): ".format(len(board))))
        if row < 1 or row > len(board) or col < 1 or col > len(board):
            print("Invalid input. Please try again.")
        elif board[row-1][col-1] != "_":
            print("That space is already occupied. Please try again.")
        else:
            return row-1, col-1

def randCpuMove(board):
    # Row and column are 1-indexed
    size = len(board)
    row = random.randint(1, size)
    col = random.randint(1, size)
    while board[row-1][col-1] != "_":
        row = random.randint(1, size)
        col = random.randint(1, size)
    return (row, col)

def cpuMove(board):
    # Row and column are 1-indexed
    size = len(board)

    # Check for an immediate win condition
    for i in range(size):
        for j in range(size):
            if board[i][j] == "_":
                board[i][j] = "O"
                if checkWin("O", board):
                    return (i+1, j+1)
                else:
                    board[i][j] = "_"
    
    # Check for an immediate loss condition
    for i in range(size):
        for j in range(size):
            if board[i][j] == "_":
                board[i][j] = "X"
                if checkWin("X", board):
                    board[i][j] = "O"
                    return (i+1, j+1)
                else:
                    board[i][j] = "_"
    # Check for a corner move
    corners = [(0, 0), (0, size-1), (size-1, 0), (size-1, size-1)]
    emptyCorners = []
    for corner in corners:
        if board[corner[0]][corner[1]] == "_":
            emptyCorners.append(corner)
    if emptyCorners:
        return random.choice(emptyCorners)
    
    # Check for a center move
    if size % 2 == 1 and board[size//2][size//2] == "_":
        return (size // 2 + 1, size // 2 + 1)
    
    # Check for a side move
    sides = [(0, size//2), (size//2, 0), (size-1, size//2), (size//2, size-1)]
    emptySides = []
    for side in sides:
        if board[side[0]][side[1]] == "_":
            emptySides.append(side)
    if emptySides:
        return random.choice(emptySides)
    
    # If all else fails, make a random move
    return randCpuMove(board)

def getMove(mode,player,board):
    if mode == 1:
        (row,col) = userMove(board)
    else:
        if player == "X":
            (row,col) = userMove(board)
        else:
            (row,col) = cpuMove(board)
    return (row,col)

def makeMove(player, row, col, board):
    # Make a move on the board.
    if row < 0 or row >= len(board) or col < 0 or col >= len(board):
        print("Invalid move. Please try again.")
        return False
    elif board[row][col] != "_":
        print("That cell is already taken. Please try again.")
        return False
    else:
        board[row][col] = player
        return True

# main functions

def main():
    # Get user choices
    playMode, dimensions = printIntro()
    # Create the board
    board = createBoard(dimensions)
    # Set up the game
    player = "X"
    gameOver = False
    # Play the game
    while not gameOver:
        # Print the board
        printBoard(board, dimensions)
        # Get the move
        (row, col) = getMove(playMode,player,board)
        # Make the move
        makeMove(player, row, col, board)
        # Check for a win
        if checkWin(player, board):
            printBoard(board, dimensions)
            print("Player {} wins!".format(player))
            gameOver = True
        # Check for a tie
        elif checkTie(board):
            printBoard(board, dimensions)
            print("The game is a tie!")
            gameOver = True
        # Switch players
        if player == "X":
            player = "O"
        else:
            player = "X"
        # End the game
        if gameOver:
            # Ask if they want to play again
            while True:
                playAgain = input("Play again? (y/n): ")
                if playAgain == "y" or playAgain == "Y":
                    main()
                elif playAgain == "n" or playAgain == "N":
                    clearScreen()
                    print("Thanks for playing, and thank you for the opportunity!")
                    exit()
                else:
                    print("Invalid input. Try again.")
                    continue

if __name__ == "__main__":
    main()
