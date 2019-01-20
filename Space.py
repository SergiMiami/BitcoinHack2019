import dice

class Space:
    """Template for board spaces"""
    def __init__(self, attributes):
        self.name = attributes['name']
        self.pos = attributes['position']

class Property(Space):
    """Properties"""
    def __init__(self, attributes):

        Space.__init__(self, attributes)

        self.Cryptopoly = attributes['cryptopoly']
        self.cryptopoly_size = attributes['cryptopoly_size']
        self.price = attributes['price']
        self.price_mortgage = self.price / 2
        self.rent = attributes['rent']
        self.rent_current = self.rent
        self.mortgage = False
        self.owner = None

class Street(Property):
    """Street Object - more accurately a bitcoin technology, company, or service"""
    def __init__(self, attributes):

        Property.__init__(self, attributes)

        self.build_cost = attributes['build_cost']
        self.rent_monopoly = self.rent * 2
        self.rent_house_1 = attributes['rent_house_1']
        self.rent_house_2 = attributes['rent_house_2']
        self.rent_house_3 = attributes['rent_house_3']
        self.rent_house_4 = attributes['rent_house_4']
        self.rent_hotel = attributes['rent_hotel']
        self.n_buildings = 0

    def get_rent(self):

            return self.rent_current

class Railroad(Property):
    """Railroad object - more accurately Bitcoin exchanges"""
    def __init__(self,attributes):

        Property.__init__(self,attributes)

        self.rent_railroad_2 = self.rent * 2
        self.rent_railroad_3 = self.rent * 3
        self.rent_railroad_4 = self.rent * 4

        def get_rent(self):
            return self.rent_current

class Utility(Property):
    """Utility object - more accurately blockchain explorers"""
    def __init__(self,attributes):

        Property.__init__(self,attributes)

        self.rent_monopoly = self.rent + 6

    def get_rent(self):

        d = dice.Dice()
        d.roll()

        return self.rent_current * d.roll_sum

class Tax(Space):
    """Tax object - more accurately aggravating Bitcoin regulations"""
    #Taxes are static is a space really best?
    def __init__(self, attributes):

        Space.__init__(self, attributes)

        self.tax = attributes['tax']

class Card(object):
    pass

class Chance(Card):
    pass

class Chest(Card):
    pass
