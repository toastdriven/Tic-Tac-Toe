import unittest2
from ..board import Board, OutOfBounds, InvalidMove


class BoardTestCase(unittest2.TestCase):
    def setUp(self):
        super(BoardTestCase, self).setUp()
        self.board = Board()

    def test_standard_init(self):
        board = Board()
        self.assertEqual(board.width, 3)
        self.assertEqual(board.height, 3)
        self.assertEqual(board.board, [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ])

    def test_smaller_init(self):
        board = Board(size=2)
        self.assertEqual(board.width, 2)
        self.assertEqual(board.height, 2)
        self.assertEqual(board.board, [
            [None, None],
            [None, None],
        ])

    def test_negative_init(self):
        board = Board(size=-2)
        self.assertEqual(board.width, 3)
        self.assertEqual(board.height, 3)
        self.assertEqual(board.board, [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ])

    def test_within_bounds(self):
        self.assertTrue(self.board.within_bounds(0, 0))
        self.assertTrue(self.board.within_bounds(1, 1))
        # Test the extremes.
        self.assertTrue(self.board.within_bounds(0, 2))
        self.assertTrue(self.board.within_bounds(2, 0))
        self.assertTrue(self.board.within_bounds(2, 2))
        # Test ouside.
        self.assertRaises(OutOfBounds, self.board.within_bounds, 0, -1)
        self.assertRaises(OutOfBounds, self.board.within_bounds, -1, 0)
        self.assertRaises(OutOfBounds, self.board.within_bounds, 0, 3)
        self.assertRaises(OutOfBounds, self.board.within_bounds, 3, 0)

    def test_check(self):
        self.board.board = [
            ['X', None, 'O'],
            ['X', 'X', 'O'],
            ['O', None, None],
        ]

        # Outside the bounds.
        self.assertRaises(OutOfBounds, self.board.check, 0, -1)
        self.assertRaises(OutOfBounds, self.board.check, -1, 0)
        self.assertRaises(OutOfBounds, self.board.check, 0, 3)
        self.assertRaises(OutOfBounds, self.board.check, 3, 0)

        self.assertEqual(self.board.check(0, 0), 'X')
        self.assertEqual(self.board.check(1, 0), None)
        self.assertEqual(self.board.check(2, 0), 'O')
        self.assertEqual(self.board.check(0, 1), 'X')
        self.assertEqual(self.board.check(1, 1), 'X')
        self.assertEqual(self.board.check(2, 1), 'O')
        self.assertEqual(self.board.check(0, 2), 'O')
        self.assertEqual(self.board.check(1, 2), None)
        self.assertEqual(self.board.check(2, 2), None)

    def test_play(self):
        self.board.board = [
            ['X', None, 'O'],
            ['X', 'X', 'O'],
            ['O', None, None],
        ]

        # There's already a marker there.
        self.assertRaises(InvalidMove, self.board.play, 0, 0, 'O')
        self.assertRaises(InvalidMove, self.board.play, 2, 0, 'O')
        # Open spot, invalid marker.
        self.assertRaises(InvalidMove, self.board.play, 2, 2, 'Z')

        self.assertTrue(self.board.play(2, 2, 'X'))

    def test_moves_left(self):
        self.assertEqual(self.board.moves_left(), 9)

        self.board.board = [
            ['X', None, 'O'],
            ['X', 'X', 'O'],
            ['O', None, None],
        ]
        self.assertEqual(self.board.moves_left(), 3)

        self.board.board = [
            ['X', 'O', 'O'],
            ['X', 'X', 'O'],
            ['O', 'X', 'O'],
        ]
        self.assertEqual(self.board.moves_left(), 0)

    def test_check_for_win(self):
        # Empty board, no one has won.
        self.assertFalse(self.board.check_for_win())

        # No wins yet.
        self.board.board = [
            ['X', None, 'O'],
            ['X', 'X', 'O'],
            ['O', None, None],
        ]
        self.assertFalse(self.board.check_for_win())

        # X wins horizontally.
        self.board.board = [
            ['X', 'X', 'X'],
            ['X', 'O', 'O'],
            ['O', 'O', None],
        ]
        self.assertEqual(self.board.check_for_win(), 'X')
        self.board.board = [
            ['X', 'O', 'O'],
            ['X', 'X', 'X'],
            ['O', 'O', None],
        ]
        self.assertEqual(self.board.check_for_win(), 'X')
        self.board.board = [
            ['X', 'O', 'O'],
            ['O', 'O', None],
            ['X', 'X', 'X'],
        ]
        self.assertEqual(self.board.check_for_win(), 'X')

        # O wins vertically.
        self.board.board = [
            ['O', 'X', 'X'],
            ['O', 'X', 'O'],
            ['O', 'O', None],
        ]
        self.assertEqual(self.board.check_for_win(), 'O')
        self.board.board = [
            ['X', 'O', 'O'],
            ['X', 'O', 'X'],
            ['O', 'O', None],
        ]
        self.assertEqual(self.board.check_for_win(), 'O')
        self.board.board = [
            ['X', 'O', 'O'],
            ['O', None, 'O'],
            ['X', 'X', 'O'],
        ]
        self.assertEqual(self.board.check_for_win(), 'O')

        # X wins diagonally.
        self.board.board = [
            ['X', None, 'O'],
            ['X', 'X', 'O'],
            ['O', None, 'X'],
        ]
        self.assertEqual(self.board.check_for_win(), 'X')

        # O wins diagonally.
        self.board.board = [
            ['X', None, 'O'],
            ['X', 'O', 'O'],
            ['O', None, 'X'],
        ]
        self.assertEqual(self.board.check_for_win(), 'O')
