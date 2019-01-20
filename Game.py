import pandas as pd

from Bank import Bank
from Player import Player
from Dice import Dice
from Space import Space
import config


class Game:
    """Tracks gameplay"""

    def __init__(self):
        self.round = 0
        self.players = None
        self.bank = Bank()
        self.board = []
        self.dice = Dice()

        self.getplayers(config.num_players)
        self.getBoard(config.board_filename)
        self.passDice()

    def getPlayers(self, num_players):
        if (num_players < 2) or (8 < num_players):
            raise ValueError('A game must have 2-8 players. You input %d ')

        self.players = [Player(p) for p in range(1, num_players + 1)]
        self.playersRemain = num_players  # wut


    def getBoard(self, file):
        board_df = pd.read_csv(file)

        for _, attributes in board_df.iterrows():

            if attributes['class'] == 'Street':
                self.board.append(Space.Street(attributes))

            if attributes['class'] == 'Utility':
                self.board.append(Space.Utility(attributes))


            if attributes['class'] == 'Railroad':
                self.board.append(Space.Railroad(attributes))


            if attributes['class'] == 'Tax':
                self.board.append(Space.Tax(attributes))


            if attributes['class'] == 'Chance':
                self.board.append(Space.Chance())


            if attributes['class'] == 'Chest':
                self.board.append(Space.Chest())


            if attributes['class'] in ['Jail', 'Idle']:
                self.board.append([])

    def passDice(self):
        self.dice = Dice()

    def updateRound(self):
        self.round += 1
