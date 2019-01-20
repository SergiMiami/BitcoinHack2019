from uuid import uuid4
from block_io import BlockIo


class Bank:

    #API Gateway
    io = BlockIo('226a-4ade-8eb4-1fed', '696996969')

    def __init__(self):
        self.id = uuid4()
        self.balance = 0
        self.addresses = []


    def genAddress(self):
        return Bank.io.get_new_address()

    def genAddress(self, label=uuid4()):
        address = Bank.io.get_new_address(label=label)
        return address

    def getAddresses(self):
        addresses = Bank.io.get_my_addresses()
        return addresses

    def getAddressBalance(address):
        balance = Bank.io.get_address_balance()
        return balance

    def getWalletBalance(self):
        balance = Bank.io.get_balance()
        return balance
