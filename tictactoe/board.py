class BoardException(Exception):
    pass


class OutOfBounds(BoardException):
    pass


class InvalidMove(BoardException):
    pass


class Board(object):
    default_size = 3

    def __init__(self, size=None):
        super(Board, self).__init__()

        if not size or size < 1:
            size = self.default_size

        self.width = size
        self.height = size

        # Initialize the board.
        # We start at top-left, indexing with x then y.
        self.board = [[None for i in range(self.width)] for j in range(self.height)]

    def within_bounds(self, x, y):
        if x < 0:
            raise OutOfBounds("{0} must be greater than or equal to 0.".format(x))

        if y < 0:
            raise OutOfBounds("{0} must be greater than or equal to 0.".format(y))

        if x >= self.width:
            raise OutOfBounds("{0} must be less than {1}.".format(x, self.width))

        if y >= self.height:
            raise OutOfBounds("{0} must be less than {1}.".format(y, self.height))

        return True

    def check(self, x, y):
        self.within_bounds(x, y)
        return self.board[y][x]

    def play(self, x, y, marker='X'):
        self.within_bounds(x, y)

        if not marker in ('X', 'O'):
            raise InvalidMove("Silly! Only X's & O's are allowed.")

        if self.board[y][x] is not None:
            raise InvalidMove("You can't play there. There's already a {0} there.".format(self.board[y][x]))

        self.board[y][x] = marker
        return True

    def check_for_win(self):
        # Check the horizontals.
        for y in range(self.height):
            results = [self.board[y][x] for x in range(self.width)]

            if not None in results:
                if len(set(results)) == 1:
                    # They're all the same value. A win!
                    return results[0]

        # Check the verticals.
        for x in range(self.width):
            results = [self.board[y][x] for y in range(self.height)]

            if not None in results:
                if len(set(results)) == 1:
                    # They're all the same value. A win!
                    return results[0]

        # Check the TL->BR diagonal.
        results = [self.board[off][off] for off in range(self.width)]

        if not None in results:
            if len(set(results)) == 1:
                # They're all the same value. A win!
                return results[0]

        # Check the BL->TR diagonal.
        results = [self.board[self.width - off - 1][off] for off in range(self.width - 1, -1, -1)]

        if not None in results:
            if len(set(results)) == 1:
                # They're all the same value. A win!
                return results[0]

        # No win found.
        return False

    def moves_left(self):
        moves = self.width * self.height

        for x in range(self.width):
            for y in range(self.height):
                if self.board[y][x] is not None:
                    moves -= 1

        return moves
