class ImpossibleAI(object):
    # This is actually not impossible at all right now.
    # Kinda brain-dead but need something that plays the game.
    def next_move(self, board):
        # Center.
        if self.board.check(1, 1) is None:
            return 1, 1

        # Top-Left.
        if self.board.check(0, 0) is None:
            return 0, 0

        # Bottom-right.
        if self.board.check(2, 2) is None:
            return 2, 2

        # Top-right.
        if self.board.check(2, 0) is None:
            return 2, 0

        # Bottom-left.
        if self.board.check(0, 2) is None:
            return 0, 2

        # Top-center.
        if self.board.check(1, 0) is None:
            return 1, 0

        # Bottom-center.
        if self.board.check(1, 2) is None:
            return 1, 2

        # Center-left.
        if self.board.check(0, 1) is None:
            return 0, 1

        # Center-right
        if self.board.check(2, 1) is None:
            return 2, 1
