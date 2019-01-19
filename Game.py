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

        self.rollDice(self)


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


    def __rollDice(self):
            self.dice.roll(self)

game = Game()