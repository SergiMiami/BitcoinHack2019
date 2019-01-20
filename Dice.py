#
#Dice Class
#
#for i in range(1, 5000):
#    game.dice.roll()
#
#
#
import numpy as np

class Dice:

    def __init__(self):
        self.sum = None
        self.double = False


    def roll(self, doubleCount=0):
        """Rolls two fair, 6-sided dice"""

        roll = np.random.choice(np.arange(1,7), 2)
        print("Rolled %d and %d" % (roll[0],roll[1]) )
        self.sum = roll.sum()
        self.double = (roll[0] == roll[1])
        self.doubleCounter = 0

        if self.double:
            self.doubleCount += 1
            print("Double. Count is %d" % (self.doubleCount))
