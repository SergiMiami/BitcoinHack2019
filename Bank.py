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


    def getAddresses():
        addresses = Bank.io.get_my_addresses()
        for item in addresses['data']['addresses']:
            print(item['address'])
        print('\n')


    def getAddressBalance(address):
        balance = Bank.io.get_address_balance(address)
        print('Address: %s, Available Balance: %s, Pending Balance: %s\n' %
                        (address, balance['data']['available_balance'], balance['data']['pending_received_balance']))


    def getWalletBalance():
        balance = Bank.io.get_balance()
        return balance


    def send(amounts, inputs, outputs):
        Bank.io.withdraw_from_addresses(amounts=amounts, from_addresses=inputs, to_addresses=outputs)


    def generateQR(address):
        # Create qr code instance
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )

        qr.add_data(address)
        qr.make(fit=True)

        img = qr.make_image()

        img.save('img/%s.img' % address)


