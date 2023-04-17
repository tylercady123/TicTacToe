Documentation for Tic Tac Toe Game

Overview:

This is an implementation of the game Tic Tac Toe in python. The game has two play modes "Pass and Play" and "Play CPU". The user can choose the dimensions of the board between 3x3 to 10x10. The game checks for a winner or a tie after each move.

Functions:

    clearScreen():
        - This function clears the console screen
    
    printIntro():
        - This function prints the game intro and gets user choices for the play mode and dimensions.
        - Returns the chosen play mode and board dimensions.

    createBoard(size):
        - Draws 
    
    checkBoardFull(board):
        - This function checks if the board is full.

    checkWin(player, board):
        - This function checks if player has won the game on the board. It returns True if the player wins, otherwise it returns False.

    checkTie(board)
        - This function checks if the game is a tie. It returns True if the game is a tie, otherwise it returns False.

    isWinnable(player, board):
        - This function checks if the player can win the game on the board. It returns True if the player can win, otherwise it returns False.

    userMove(board):
        - This function allows the user to input their move by selecting a row and column number.
        - The input is validated to ensure that it is within the range of the board size and that the selected space is not already occupied.
        - If the input is valid, the function returns the selected row and column as a tuple, with each value decremented by 1 to convert it from 1-indexed to 0-indexed.

    randCpuMove(board):
        - This function generates a random move for the computer player.
        - The row and column are selected randomly within the range of the board size.
        - The function checks if the selected space is already occupied, and if so, generates a new random move.
        - If the selected space is valid, the function returns the row and column as a tuple, with each value being 1-indexed.

    cpuMove(board):
        - This function determines the computer player's move.
        - The function first checks if the computer player can win the game immediately. If so, it returns the winning move.
        - If the computer player cannot win immediately, the function checks if the human player can win immediately. If so, it blocks the human player's winning move by selecting the space that would prevent the win.
        - If neither player can win immediately, the function selects a corner space if available.
        - If a corner space is not available, the function selects the center space if available.
        - If neither a corner nor center space is available, the function selects a side space.
        - If no valid space is available, the function generates a random move.

    getMove(mode,player,board):
        - This function gets the player's move based on the game mode and player turn.
        If the game mode is 1 (two-player mode), the function calls the userMove() function to get the user's move.
        - If the game mode is 2 (single-player mode), the function calls the userMove() function if it is the human player's turn, and the cpuMove() function if it is the computer player's turn.
        - The function returns the selected row and column as a tuple, with each value being 0-indexed.

    makeMove(player, row, col, board):
        - This function makes the selected move on the game board.
        - The function checks if the selected move is valid by ensuring that it is within the range of the board size and that the selected space is not already occupied.
        - If the selected move is valid, the function updates the board with the player's move and returns True.
        - If the selected move is not valid, the function returns False and prints an error message.