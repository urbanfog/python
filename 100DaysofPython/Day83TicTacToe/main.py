from gameboard import Gameboard
from player import Player

# initialize
board = Gameboard()
p1 = Player('X')
p2 = Player('O')
winner = False


def player_turn(player):
    while True:
        mark, x, y = player.turn()
        try:
            board.record_mark(x, y, mark)
            break
        except ValueError:
            print('You selected a row that is already taken, try again.')

    win = board.check_for_winner(mark)
    if win == True:
        return mark
    else:
        return 1


while True:
    winner = player_turn(p1)
    if not winner == 1:
        break
    winner = player_turn(p2)
    if not winner == 1:
        break

print(f'Congrats! Player {winner} won!')
