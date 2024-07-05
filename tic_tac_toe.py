import tkinter as tk
import random

class TicTacToeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic-Tac-Toe")
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_buttons()

    def create_buttons(self):
        for r in range(3):
            for c in range(3):
                button = tk.Button(self.master, text=" ", font='normal 20 bold', height=3, width=6,
                                   command=lambda r=r, c=c: self.on_button_click(r, c))
                button.grid(row=r, column=c)
                self.buttons[r][c] = button

    def on_button_click(self, r, c):
        if self.board[r][c] == " " and self.current_player == "X":
            self.board[r][c] = self.current_player
            self.buttons[r][c].config(text=self.current_player)
            if self.check_winner():
                self.end_game(f"Player {self.current_player} wins!")
            elif self.check_draw():
                self.end_game("It's a draw!")
            else:
                self.current_player = "O"
                self.master.after(500, self.ai_move)

    def ai_move(self):
        best_score = float('-inf')
        best_move = None
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == " ":
                    self.board[row][col] = "O"
                    score = self.minimax(self.board, 0, False)
                    self.board[row][col] = " "
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)
        if best_move:
            r, c = best_move
            self.board[r][c] = "O"
            self.buttons[r][c].config(text="O")
            if self.check_winner():
                self.end_game("Player O wins!")
            elif self.check_draw():
                self.end_game("It's a draw!")
            else:
                self.current_player = "X"

    def minimax(self, board, depth, is_maximizing):
        winner = self.check_winner()
        if winner == "O":
            return 1
        if winner == "X":
            return -1
        if self.check_draw():
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for row in range(3):
                for col in range(3):
                    if board[row][col] == " ":
                        board[row][col] = "O"
                        score = self.minimax(board, depth + 1, False)
                        board[row][col] = " "
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for row in range(3):
                for col in range(3):
                    if board[row][col] == " ":
                        board[row][col] = "X"
                        score = self.minimax(board, depth + 1, True)
                        board[row][col] = " "
                        best_score = min(score, best_score)
            return best_score

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return self.board[0][2]
        return None

    def check_draw(self):
        for row in self.board:
            if " " in row:
                return False
        return True

    def end_game(self, message):
        for row in self.buttons:
            for button in row:
                button.config(state="disabled")
        self.display_winner(message)

    def display_winner(self, message):
        winner_label = tk.Label(self.master, text=message, font='normal 20 bold')
        winner_label.grid(row=3, columnspan=3)

def main():
    root = tk.Tk()
    game = TicTacToeGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
