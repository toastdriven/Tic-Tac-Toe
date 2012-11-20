import unittest2
from ..ai import ImpossibleAI
from ..board import Board


class ImpossibleAITestCase(unittest2.TestCase):
    def setUp(self):
        super(ImpossibleAITestCase, self).setUp()
        self.board = Board()
        self.ai = ImpossibleAI()

    def test_next_move(self):
        self.assertEqual(self.ai.next_move(self.board), (1, 1))

        self.board.play(1, 1)
        self.assertEqual(self.ai.next_move(self.board), (0, 0))

        self.board.play(0, 0)
        self.assertEqual(self.ai.next_move(self.board), (2, 2))

        self.board.play(2, 2)
        self.assertEqual(self.ai.next_move(self.board), (2, 0))

        self.board.play(2, 0)
        self.assertEqual(self.ai.next_move(self.board), (0, 2))

        self.board.play(0, 2)
        self.assertEqual(self.ai.next_move(self.board), (1, 0))

        self.board.play(1, 0)
        self.assertEqual(self.ai.next_move(self.board), (1, 2))

        self.board.play(1, 2)
        self.assertEqual(self.ai.next_move(self.board), (0, 1))

        self.board.play(0, 1)
        self.assertEqual(self.ai.next_move(self.board), (2, 1))
