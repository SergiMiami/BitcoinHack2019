#
# Cryptopoly Bank Module
#
#   Examples:
#
#   *spending
#   Bank.send(0.069165, '2NE5w7x2L9YWbY2NNJAfjT8zwaoGbgfCqi2', '2Mwse58gJGpgudj47a59KfKGWxdxHwxpCJ1')
#
#   *lists all addresses and balances
#   for address in Bank.getAddresses():
#     Bank.getAddressBalance(address=address['address'])
#
from block_io import BlockIo
from uuid import uuid4
import qrcode


class Bank:

    # create API Gateway
    io = BlockIo('226a-4ade-8eb4-1fed', '696996969')

    def __init__(self):
        self.id = uuid4()
        self.balance = 0


    def genAddress():
        address = Bank.io.get_new_address(label=uuid4())
        print("Generated Address: %s" % address)
        return address


    def printAddresses():
        data = Bank.io.get_my_addresses()
        for item in data['data']['addresses']:
            print(item['address'])
        print('\n')


    def getAddresses():
        addresses = []
        data = Bank.io.get_my_addresses()
        for item in data['data']['addresses']:
            addresses.append(item)
        return addresses



    def getAddressBalance(address):
        balance = Bank.io.get_address_balance(address=address)
        print('Address: %s, Available Balance: %s\n' %
                        (address, balance['data']['available_balance']))


    def getWalletBalance():
        balance = Bank.io.get_balance()
        print('Account Balance: %s, Pending Balance: %s\n' %
                        (balance['data']['available_balance'], balance['data']['pending_received_balance']))


    def send(amounts, inputs, outputs):
        Bank.io.withdraw_from_addresses(amounts=amounts, from_addresses=inputs, to_addresses=outputs)


    def generateQR(address):
        #Create qr code instance
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )

        #add data
        qr.add_data(address)
        qr.make(fit=True)

        #generate
        img = qr.make_image()

        #save image
        img.save('img/%s.png' % address)


