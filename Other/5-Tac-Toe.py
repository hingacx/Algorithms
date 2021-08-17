"""
An improvised version of the classic board game Tic-Tac-Toe. Instead of a 3x3 grid, we use a 5x5 grid.
A win is 5 pieces in a row horizontally, vertically or diagonally. Implemented via OOP.
"""


class fiveTackToe:
    """Takes two Player objects to initialize the game."""
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = [[None for x in range(5)] for y in range(5)]

        # starts with player1
        self.turn = player1

    def __str__(self):
        """Prints the game board out in a readable format for humans."""
        out = ""
        for row in self.board:
            out += str(row) + "\n"
        return out


    def make_move(self, player, move):
        """
        Makes a move on the game board.
        A move must contain the form of a tuple (X,Y).
        """

        if self.turn is not player:
            return "It's not your turn."
        if move[0] < 0 or move[1] > 4:
            return "Out of bounds."
        if self.board[move[0]][move[1]] is not None:
            return "Spot already taken."

        self.board[move[0]][move[1]] = player.get_piece()
        # Swaps turn to other player.
        self.swap_turns(player)
        # Check for winning condition
        ansr = self.check_board()
        if ansr == self.player1:
            return "Player1 has won!"
        if ansr == self.player2:
            return "Player2 has won!"
        return "Success"


    def swap_turns(self, player):
        """Swaps the turn to the other Player."""
        if player is self.player1:
            self.turn = self.player2
        else:
            self.turn = self.player1


    def check_board(self):
        """Checks the board to see if a Player won."""
        b = self.board
        m1, m2 = self.player1.get_piece(), self.player2.get_piece()
        s1, s2 = [m1, m1, m1, m1, m1], [m2, m2, m2, m2, m2]
        # Checking the rows for a win.
        for row in range(5):
            temp = []
            for col in range(5):
                temp.append(b[row][col])

            # Winning conditions
            if temp == s1:
                return self.player1
            if temp == s2:
                return self.player2
        # Checking the columns for a win.
        count = 0
        while count < 5:
            temp = []
            for row in range(5):
                temp.append(b[row][count])

            # Winning conditions
            if temp == s1:
                return self.player1
            if temp == s2:
                return self.player2
            count += 1

        # Checking diagonally for a win.
        count = 0
        temp = []
        temp2 = []
        while count < 5:
            temp.append(b[count][count])
            temp2.append(b[4-count][count])

            # Winning conditions
            if temp == s1 or temp2 == s1:
                return self.player1
            if temp == s2 or temp2 == s2:
                return self.player2
            count += 1

        return None

class Player:
    """Create Player's for 5-tac-toe."""
    def __init__(self, piece):
        self.piece = piece.lower()

    def get_piece(self):
        """Returns the Player's piece."""
        return self.piece




if __name__ == '__main__':
    p1 = Player('X')
    p2 = Player('Y')
    game = fiveTackToe(p1,p2)
    print(game)
    game.make_move(p1,(3,3))
    game.make_move(p2,(2,0))
    game.make_move(p1,(0,1))
    game.make_move(p2,(0,0))
    game.make_move(p1,(0,2))
    game.make_move(p2,(1,0))
    game.make_move(p1,(0,3))
    game.make_move(p2,(3,0))
    print(game.make_move(p1,(1,4)))
    print(game.make_move(p2,(4,0)))
    print(game)