from player import HumanPlayer, RandomCompPlayer
import time
class TicTacToe:
    def __init__(self):
        self.board = [" " for i in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:3*i+3] for i in range(3)]:
            # print("| " + " | ".join(row) + " |")  --> Another usefull way
            print(f"| {row[0]} | {row[1]} | {row[2]} |")

    @staticmethod
    def print_board_nums():
            number_board = [[str(j+1) for j in range(i*3, (3*i+3))] for i in range(3)]
            for row in number_board:
                print(f"| {row[0]} | {row[1]} | {row[2]} |")

    def available_moves(self):
        # moves = []
        # for i, j in enumerate(self.board):
        #     if j == " ":
        #         moves.append(i)
        # return moves
        return [i for i, j in enumerate(self.board) if j == " "]

    def empty_squares(self):
        return " " in self.board

    def num_empty_squares(self):
        return self.board.count(" ")

    def make_move(self, square, letter):
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_ind = square//3
        row = self.board[row_ind*3:row_ind*3+3]
        if all([square == letter for square in row]):
            return True

        col_ind = square%3
        col = [self.board[col_ind+i*3] for i in range(3)]
        if all([square == letter for square in col]):
            return True

        if square%2 == 0:
            diognel1 = [self.board[i] for i in [0, 4, 8]]
            if all([square == letter for square in diognel1]):
                return True
            diognel2 = [self.board[i] for i in [2, 4, 6]]
            if all([square == letter for square in diognel2]):
                return True
        return False


def play(game , x_player, o_player):
    game.print_board_nums()
    letter = "X"
    while game.empty_squares():
        if letter == "O":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            print(f"{letter} makes a move to square {square}")
            game.print_board()
            print("")

            if game.current_winner:
                print(f"{letter} wins the game.")
                return letter

            letter = "O" if letter == "X" else "X"
        time.sleep(1)
    print("It's a tie.")

if __name__ == "__main__":
    x_player = HumanPlayer("X")
    o_player = RandomCompPlayer("O")
    t = TicTacToe()
    play(t, x_player,o_player)



