import unittest2
from ..board import OutOfBounds
from ..game import Game


class GameTestCase(unittest2.TestCase):
    def setUp(self):
        super(GameTestCase, self).setUp()
        self.game = Game()

    def test_init(self):
        game = Game()
        self.assertEqual(game.board.width, 3)
        self.assertEqual(game.board.height, 3)
        self.assertEqual(game.player_marker, 'X')
        self.assertEqual(game.computer_marker, 'O')

        game = Game(size=2, player_marker='O')
        self.assertEqual(game.board.width, 2)
        self.assertEqual(game.board.height, 2)
        self.assertEqual(game.player_marker, 'O')
        self.assertEqual(game.computer_marker, 'X')

    def test_player_move(self):
        self.assertRaises(OutOfBounds, self.game.player_move, 3, 3)
        self.assertFalse(self.game.player_move(1, 1))
        self.assertFalse(self.game.player_move(1, 0))
        self.assertTrue(self.game.player_move(1, 2))
        self.assertEqual(self.game.board.board, [
            [None, 'X', None],
            [None, 'X', None],
            [None, 'X', None],
        ])

    def test_computer_move(self):
        self.assertFalse(self.game.computer_move())
        self.assertFalse(self.game.computer_move())
        self.assertTrue(self.game.computer_move())
        self.assertEqual(self.game.board.board, [
            ['O', None, None],
            [None, 'O', None],
            [None, None, 'O'],
        ])