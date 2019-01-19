from uuid import uuid4
from block_io import BlockIo
from random import randint

class Bank:

    #API Gateway
    io = BlockIo('226a-4ade-8eb4-1fed', '696996969')

    def __init__(self):
        self.id = uuid4()
        self.balance = 0


    def genAddress(self):
        return(Bank.io.get_new_address())

    def genAddress(self, label=randint(0,100)):
        return(Bank.io.get_new_address(label=label))
