class TicTacToe:
    def __init__(self):
        self.board = [['-' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def initialize_board(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = '-'

    def print_board(self):
        for row in self.board:
            print(" ".join(row))
        print("\n")

    def make_move(self, row, col):
        if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == '-':
            self.board[row][col] = self.current_player
            return True
        return False

    def check_winner(self):
        return self.check_rows() or self.check_columns() or self.check_diagonals()

    def check_rows(self):
        for row in self.board:
            if row[0] == self.current_player and row[1] == self.current_player and row[2] == self.current_player:
                return True
        return False

    def check_columns(self):
        for col in range(3):
            if self.board[0][col] == self.current_player and self.board[1][col] == self.current_player and self.board[2][col] == self.current_player:
                return True
        return False

    def check_diagonals(self):
        return (
            (self.board[0][0] == self.current_player and self.board[1][1] == self.current_player and self.board[2][2] == self.current_player) or
            (self.board[0][2] == self.current_player and self.board[1][1] == self.current_player and self.board[2][0] == self.current_player)
        )

    def is_board_full(self):
        return all(cell != '-' for row in self.board for cell in row)

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play_game(self):
        while not self.is_board_full() and not self.check_winner():
            self.print_board()
            row, col = map(int, input(f"Player {self.current_player}, enter your move (row and column): ").split())
            if self.make_move(row, col):
                if self.check_winner():
                    self.print_board()
                    print(f"Player {self.current_player} wins!")
                    return
                self.switch_player()
            else:
                print("This move is not valid")
        
        self.print_board()
        if self.is_board_full() and not self.check_winner():
            print("It's a draw!")

if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
