class Gameboard:
    def __init__(self) -> None:
        # create array to hold playable spaces 0 thru 8
        self.spaces = [" " for i in range(9)]
        self.render_board()

    def record_mark(self, space, player):
        self.spaces[space] = player
        self.render_board()

    def render_board(self):
        print(f'''
                     {self.spaces[0]} | {self.spaces[1]} | {self.spaces[2]}
                    ---+---+---
                     {self.spaces[3]} | {self.spaces[4]} | {self.spaces[5]}
                    ---+---+---
                     {self.spaces[6]} | {self.spaces[7]} | {self.spaces[8]}
                    ''')
