class Gameboard:
    def __init__(self) -> None:
        # create 2d array to hold playable spaces 0 thru 8
        self.spaces = [[" " for i in range(3)] for i in range(3)]
        self.render_board()

    def record_mark(self, x, y, player):
        if self.spaces[x][y] == " ":
            self.spaces[x][y] = player
            self.render_board()
            return 0
        else:
            raise ValueError

    def render_board(self):
        print(f'''
                      0   1   2

                 0    {self.spaces[0][0]} | {self.spaces[0][1]} | {self.spaces[0][2]}
                     ---+---+---
                 1    {self.spaces[1][0]} | {self.spaces[1][1]} | {self.spaces[1][2]}
                     ---+---+---
                 2    {self.spaces[2][0]} | {self.spaces[2][1]} | {self.spaces[2][2]}
                    ''')

    def check_for_winner(self, mark):
        rows_to_check = self.spaces
        rows_to_check.append(
            [self.spaces[0][0], self.spaces[1][1], self.spaces[2][2]])  # d1
        rows_to_check.append(
            [self.spaces[0][2], self.spaces[1][1], self.spaces[2][0]])  # d2
        rows_to_check.append(
            [self.spaces[0][0], self.spaces[1][0], self.spaces[2][0]])  # c1
        rows_to_check.append(
            [self.spaces[0][1], self.spaces[1][1], self.spaces[2][1]])  # c2
        rows_to_check.append(
            [self.spaces[0][2], self.spaces[1][2], self.spaces[2][2]])  # c3
        for row in rows_to_check:
            # a set will return an array of unique values
            if len(set(row)) == 1 and row[0] == mark:
                return True
        return False
