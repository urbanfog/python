class Player:
    def __init__(self, mark):
        self.mark = mark

    def turn(self):
        '''Returns the player's mark and the location they have selected'''
        print(f"Player '{self.mark}' turn.")
        while True:
            try:
                x = int(
                    input('Choose a row to place your mark (from 0 to 2): '))
                y = int(
                    input('Choose a column to place your mark (from 0 to 2): '))
                if x >= 3 or y >= 3:
                    raise ValueError
                break
            except ValueError:
                print('You have selected an invalid number.')
        return self.mark, x, y
