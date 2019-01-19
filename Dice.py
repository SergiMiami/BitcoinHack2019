import numpy as np

class Dice:

    def __init__(selfself):
        self.sum = None
        self.double = False
        self.doubleCount = 0


    def roll(self):
        """Rolls two fair 6-sided dice"""

        roll = np.random.choice(np.arange(1,7), 2)

        self.sum = roll.sum()
        self.double = roll[0] == roll[1]
        self.doubleCount += self.double

        if self.doubleCount > 3:
            print("3x double roll. Its a problem.")
