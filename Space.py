

class Space:

    def __init__(self, attributes):
        self.name = attributes['name']
        self.pos = attributes['position']


class Property(Space):

    def __init__(self, attributes):

        Space.__init__(self, attributes)

        self.price = attributes['price']
        self.rent = self.price/2
        self.mortgage = False
        self.owner = None

class Street(Property):
    pass

class Railroad(Property):
    pass

class Utility(Property):
    pass

class Tax(Space):
    """Tax Space"""
    #Taxes are static is a space really best?
    def __init__(selfself, attributes):
        Space.__init__(self, attributes)
        self.tax = attributes['tax']


class Card(object):
    pass

class Chance(Card):
    pass

class Chest(Card):
    pass