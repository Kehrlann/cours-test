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
