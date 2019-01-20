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

        if self.double:
            doubleCount += 1
            print("Double. Count is %d" % (doubleCount))
            if doubleCount == 3:
                print("3x double roll. It's a problem. Go to cold storage.")
            else: self.roll(doubleCount)

        self.double = False

