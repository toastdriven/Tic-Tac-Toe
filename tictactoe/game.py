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


class ConsoleGame(Game):
    """
    This version does console output! Hooray!
    """
    def print_board(self):
        # Hard-coded size. Sucks. :/
        print("   0   1   2")
        print("")
        print("0  {0} | {1} | {2}".format(self.board.check(0, 0) or ' ', self.board.check(1, 0) or ' ', self.board.check(2, 0) or ' '))
        print("  -----------")
        print("1  {0} | {1} | {2}".format(self.board.check(0, 1) or ' ', self.board.check(1, 1) or ' ', self.board.check(2, 1) or ' '))
        print("  -----------")
        print("2  {0} | {1} | {2}".format(self.board.check(0, 2) or ' ', self.board.check(1, 2) or ' ', self.board.check(2, 2) or ' '))

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

    def print_win(self, message):
        print('')
        print('')
        print('')
        print('')
        print('##############################')
        print('')
        print('  ' + message.upper())
        print('')
        self.print_board()
        print('')
        print('')

    def run(self):
        while self.board.moves_left():
            self.print_board()
            print('')
            print("Moves Left: {0}".format(self.board.moves_left()))
            print('')
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
                        self.print_win("You win!")
                        return
                except (OutOfBounds, InvalidMove) as e:
                    print(e)
                    location = None

            if self.board.moves_left() and self.computer_move():
                self.print_win('The AI wins!')
                return

        self.print_win('Tie game. :(')


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
