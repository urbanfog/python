from gameboard import Gameboard


class Player:
    def __init__(self, mark, board):
        self.mark = mark
        self.board = board

    def turn(self):
        '''Returns the player's mark and the location they have selected'''
        print(f"Player '{self.mark}' turn.")
        while True:
            try:
                loc = int(
                    input('Choose a spot to place your mark (from 0 to 9): '))
                if loc >= 9:
                    raise ValueError
                break
            except ValueError:
                print('You have selected an invalid number.')
        return self.mark, loc


game = Gameboard()
p1 = Player('X', game)
p1.turn()
