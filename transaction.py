from collections import OrderedDict

from utility.printable import Printable

class Transaction(Printable):

    def __init__(self,sender,recipent,signature,productid):
        self.sender=sender
        self.recipent=recipent
        self.productid=productid
        self.signature = signature

    def to_ordered_dict(self):
        return OrderedDict([('sender',self.sender),('recipent',self.recipent),('productid',self.productid)])
