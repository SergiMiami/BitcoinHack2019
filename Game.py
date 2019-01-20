import pandas as pd

from Bank import Bank
from Player import Player
from Dice import Dice
from Space import Space


class Game():

    def __init__(self):
        self.round = 0
        self.players = None
        self.playersRemain = []  # wut
        self.bank = Bank()
        self.board = []
        self.dice = Dice()



    def __getBoard(self, file):
        board_df = pd.read_csv(file)

        for _, attributes in board_df.iterrows():

            if attributes['class'] == 'Street':
                pass

            if attributes['class'] == 'Utility':
                pass

            if attributes['class'] == 'Railroad':
                pass

            if attributes['class'] == 'Tax':
                pass

            if attributes['class'] == 'Chance':
                pass

            if attributes['class'] == 'Chest':
                pass

            if attributes['class'] in ['Jail', 'Idle']:
                self.board.append([])


game = Game()

Bank.printAddresses()

#for address in Bank.getAddresses():
#    Bank.getAddressBalance(address=address['address'])

#spent
#Bank.send(0.069165, '2NE5w7x2L9YWbY2NNJAfjT8zwaoGbgfCqi2', '2Mwse58gJGpgudj47a59KfKGWxdxHwxpCJ1')