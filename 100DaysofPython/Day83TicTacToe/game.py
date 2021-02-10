from gameboard import Gameboard
from player import Player


class Game:
    def __init__(self) -> None:
        self.board = Gameboard()
        self.p1 = Player('O')
        self.p2 = Player('X')
        self.player_turn = 0

    def new(self):
        pass

    def win(self, mark):

    def turn(self):
        # do stuff
        self.board.check_for_win()
