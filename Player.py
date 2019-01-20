#Player Class

from uuid import uuid4
from Bank import Bank

class Player:


    def __init__(self):
        self.id = uuid4()
        self.cash = 0
        self.properties = []
        self.position = 0
        self.bankrupt = False
        self.addresses = []


    def move(self, roll):
        """Mooves player around the board"""
        self.position += roll

        if self.position >= 40:
            self.position = 0
            self.cash += 200

        print("Player moved %d spaces to position %d" % (roll, self.position))

    def visit(self, property):
        """Visit a property"""

        isOwned = property.owner is not None
        isUnmortgaged = not property.mortgage
        canAffordRent = self.cash >= property.rent_current
        canPurchase = self.cash >= property.price

        if isOwned and isUnmortgaged:
            if canAffordRent:
                self.pay(payment=property.rent_current, recipient=property.owner)
                Bank.send(property.rent_current, property.owner)
            else:
                self.goBankrupt(creditor=property.owner)

        elif not isOwned and canPurchase:
            self.buy(property)

    def pay(self, payment, recipient):
        pass