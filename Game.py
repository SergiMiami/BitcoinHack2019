import pandas as pd

from Bank import Bank
from Player import Player
from Dice import Dice
from Space import Space
import config.py


class Game():
    """Tracks gameplay"""

    def __init__(self):
        self.round = 0
        self.players = None
        self.bank = Bank()
        self.board = []
        self.dice = Dice()
        self.playersRemain = []  # wut

        self.get_players(config.num_players)


    def __addPlayers(self, num_players):
        if (num_players < 2) or (8 < num_players):
            raise ValueError('A game must have 2-8 players. You input %d ')



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

for i in range(1, 5000):
    game.dice.roll()
