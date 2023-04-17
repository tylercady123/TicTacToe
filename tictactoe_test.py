import unittest
from tictactoe import *
from unittest.mock import patch

class tests(unittest.TestCase):

    def test_cpuMove(self):
        # Test if the CPU's move is a valid integer within the range of the board size.
        size = 3
        board = [['X', '_', '_'], ['_', 'O', '_'], ['_', '_', '_']]
        # Ideal CPU move in defined board is in an available corner.
        availCorners = [(0,2), (2,0), (2,2)]
        move = cpuMove(board)
        self.assertIn(move, availCorners)



    def test_isWinnable(self):
        board1 = [
            ['X', '_', '_'],
            ['_', 'O', '_'],
            ['_', '_', '_']
        ]
        board2 = [
            ['X', 'O', 'X'],
            ['O', 'O', 'X'],
            ['_', 'X', 'O']
        ]
        # Test if the isWinnable function returns the correct move to win the game.
        # In this case isWinnable should return True
        self.assertTrue(isWinnable("X", board1))
        # In this case isWinnable should return False
        self.assertFalse(isWinnable("X", board2))


    def test_getMove(self):
        # Test if the getMove function returns a valid integer within the range of the board size.
        size = 3
        board = createBoard(size)
        # Simulate user input (1,1)


    def test_createBoard(self):
        # Test if the createBoard function returns a board of the correct size.
        size = 3
        board = createBoard(size)
        self.assertEqual(len(board), size)
    

    #End of tests

if __name__ == '__main__':
    unittest.main()
