from __future__ import print_function
import sys
from ai import ImpossibleAI
from board import Board, OutOfBounds, InvalidMove


class Game(object):
    """
    The main Tic-Tac-Toe game.

    This forms the basis of the game & is UI-independent. With light extension,
    it can do console output, GUI clients, APIs, etc.

    Because overengineering.
    """
    def __init__(self, size=None, player_marker='X'):
        super(Game, self).__init__()
        self.board = Board(size=size)
        self.player_marker = player_marker

        if self.player_marker == 'X':
            self.computer_marker = 'O'
        else:
            self.computer_marker = 'X'

        self.ai = ImpossibleAI()

    def player_move(self, x, y):
        self.board.play(x, y, self.player_marker)
        return self.board.check_for_win() == self.player_marker

    def computer_move(self):
        x, y = self.ai.next_move(self.board)
        self.board.play(x, y, self.computer_marker)
        return self.board.check_for_win() == self.computer_marker

    def computer_turn(self):
        if not self.board.moves_left():
            return False

        if self.computer_move():
            return True

        return False

    def run(self):
        while self.board.moves_left():
            self.draw_board()

            if self.computer_turn():
                self.draw_win('The AI wins!')
                return

            self.draw_board()

            if self.player_turn():
                self.draw_win("You win!")
                return

        self.draw_win('Tie game. :(')

    # The unimplemented.
    def draw_board(self):
        raise NotImplementedError("Your subclass needs to implement `draw_board`.")

    def draw_win(self, message):
        raise NotImplementedError("Your subclass needs to implement `draw_board`.")

    def player_turn(self):
        raise NotImplementedError("Your subclass needs to implement `draw_board`.")


class ConsoleGame(Game):
    """
    This version does console output! Hooray!
    """
    def draw_board(self):
        # Hard-coded size. Sucks. :/
        print("   0   1   2")
        print("")
        print("0  {0} | {1} | {2}".format(self.board.check(0, 0) or ' ', self.board.check(1, 0) or ' ', self.board.check(2, 0) or ' '))
        print("  -----------")
        print("1  {0} | {1} | {2}".format(self.board.check(0, 1) or ' ', self.board.check(1, 1) or ' ', self.board.check(2, 1) or ' '))
        print("  -----------")
        print("2  {0} | {1} | {2}".format(self.board.check(0, 2) or ' ', self.board.check(1, 2) or ' ', self.board.check(2, 2) or ' '))
        print('')
        print("Moves Left: {0}".format(self.board.moves_left()))
        print('')

    def parse_location(self, the_input):
        if not ',' in the_input:
            return None

        try:
            bits = [int(bit.strip()) for bit in the_input.split(',')]
        except ValueError:
            return None

        if len(bits) != 2:
            return None

        return bits[0], bits[1]

    def draw_win(self, message):
        print('')
        print('')
        print('')
        print('')
        print('##############################')
        print('')
        print('  ' + message.upper())
        print('')
        self.draw_board()
        print('')
        print('')

    def player_turn(self):
        if not self.board.moves_left():
            return False

        location = None

        while location is None:
            move_location = raw_input('Where would you like to place your marker? (Ex: "2, 1" for bottom middle): ')
            location = self.parse_location(move_location)

            if location is None:
                print("Sorry, I couldn't recognize that. Please try again...")
                continue

            x, y = location

            try:
                # Player's play.
                if self.player_move(x, y):
                    return True
            except (OutOfBounds, InvalidMove) as e:
                print(e)
                location = None

        return False


def usage():
    print("Usage: {0} <marker>".format(__file__))
    print("")
    print("  Your <marker> should be either an X or an O.")
    sys.exit(0)


if __name__ == '__main__':
    marker = 'X'

    if len(sys.argv) == 2:
        if sys.argv[1] in ['-h', 'help']:
            usage()

        if not sys.argv[1] in ['X', 'O', 'x', 'o']:
            usage()

        marker = sys.argv[1]

    game = ConsoleGame(player_marker=marker)
    game.run()
