# Obviously, this program doesn't work. Most of the functions
# are not event defined. The idea is to show you how you could
# structure a program to make it testable.
#
# Here, the game logic if contained in the Minesweeper class,
# which can be tested in isolation, without reading from the
# command line.
#
# You can also test "print_board" by itself.
#
# Compare it with a program that was not designed with tests in
# mind, which is very hard to test:
#
# https://gist.github.com/mohd-akram/3057736
#
class Minesweeper:
    def reveal(self, x, y):
        pass

    def is_finished(self):
        pass

    def current_state(self):
        pass


if __name__ == "__main__":
    game = Minesweeper()

    while not game.is_finished():
        print_board(game.current_state())
        print_help_message()
        x, y = read_input()
        game.reveal(x, y)

    print_board(game.current_state())
    game.print_result()
