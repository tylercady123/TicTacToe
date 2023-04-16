import unittest
from tictactoe import tic_tac_toe
from unittest.mock import patch

class tests(unittest.TestCase):

    def test_cpuMove(self):
        # Test if the CPU's move is a valid integer within the range of the board size.
        size = 3
        board = tic_tac_toe.createBoard(size)
        cpu_move = tic_tac_toe.cpuMove(board, size)
        self.assertTrue(isinstance(cpu_move, int))
        self.assertTrue(cpu_move >= 0 and cpu_move < size**2)

    def test_userMove(self):
        # Test if the user's move is a valid integer within the range of the board size.
        size = 3
        board = tic_tac_toe.createBoard(size)
        user_move = tic_tac_toe.userMove(board, size)
        self.assertTrue(isinstance(user_move, int))
        self.assertTrue(user_move >= 0 and user_move < size**2)

    def test_checkGameOver(self):
        # Test if the checkGameOver function correctly identifies a win, tie, or ongoing game.
        size = 3
        board = [["X", "O", "O"], ["O", "X", "X"], ["O", "X", "O"]] # board in win state
        self.assertEqual(tic_tac_toe.checkGameOver(board), "O wins!")
        board = [["X", "O", "X"], ["X", "O", "O"], ["O", "X", "X"]] # board in tie state
        self.assertEqual(tic_tac_toe.checkGameOver(board), "Tie game!")
        board = [["X", "O", "_"], ["X", "O", "_"], ["_", "_", "_"]] # board in ongoing game state
        self.assertEqual(tic_tac_toe.checkGameOver(board), None)

    def test_isWinnable(self):
        # Test if the isWinnable function correctly identifies a winnable state for the player.
        board = [["X", "_", "_"], ["O", "X", "_"], ["O", "_", "_"]] # player "X" in winnable state
        self.assertTrue(tic_tac_toe.isWinnable("X", board))
        board = [["X", "O", "_"], ["_", "O", "X"], ["_", "_", "X"]] # player "O" in winnable state
        self.assertTrue(tic_tac_toe.isWinnable("O", board))
        board = [["X", "O", "X"], ["X", "O", "O"], ["O", "X", "X"]] # no winnable state for either player
        self.assertFalse(tic_tac_toe.isWinnable("X", board))
        self.assertFalse(tic_tac_toe.isWinnable("O", board))

    def test_getMove(self):
        # Test if the getMove function returns a valid integer within the range of the board size.
        size = 3
        board = tic_tac_toe.createBoard(size)
        with patch('builtins.input', return_value="0"):
            move = tic_tac_toe.getMove(board, size)
            self.assertTrue(isinstance(move, int))
            self.assertTrue(move >= 0 and move < size**2)
        with patch('builtins.input', return_value="9"):
            move = tic_tac_toe.getMove(board, size)
            self.assertTrue(isinstance(move, int))
            self.assertTrue(move >= 0 and move < size**2)
        with patch('builtins.input', return_value="10"):
            move = tic_tac_toe.getMove(board, size)
            self.assertTrue(isinstance(move, int))
            self.assertTrue(move >= 0 and move < size**2)

    def test_createBoard(self):
        # Test if the createBoard function returns a board of the correct size.
        size = 3
        board = tic_tac_toe.createBoard(size)
        self.assertEqual(len(board), size)
        for row in board:
            self.assertEqual(len(row), size)
    #End of tests

if __name__ == '__main__':
    unittest.main()
