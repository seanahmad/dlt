import json
import hashlib

from time import time


class Block(object):
    @staticmethod
    def f_hash(block):
        assert block is not None

        block_dict = {"timestamp": block.time, "transactions": block.transactions}
        block_string = json.dumps(block_dict, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()


    def __init__(self):
        self.__time = round(time(),3)
        self.__hash = None
        self.__transactions = []

    @property
    def time(self):
        return self.__time

    @property
    def transactions(self):
        return self.__transactions

    def append_transaction(self, sender, recipient, amount):
        """
        Creates a new transaction to go into the next mined Block
        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount
        :return: <int> The index of the Block that will hold this transaction
        """
        self.__transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

    def __repr__(self):
        return str({"timestamp": self.time, "hash": self.hash, "transactions": self.transactions})

    @property
    def hash(self):
        return self.__hash

    @hash.setter
    def hash(self, value):
        self.__hash = value




if __name__ == '__main__':
    b1 = Block()
    b1.append_transaction(sender="c", recipient="b", amount=20.0)

    b2 = Block()
    b2.append_transaction(sender="c", recipient="b", amount=20.0)
    b2.append_transaction(sender="a", recipient="d", amount=10.0)

    b3 = Block()
    b3.append_transaction(sender="c", recipient="b", amount=20.0)
    b3.append_transaction(sender="a", recipient="d", amount=10.0)

    chain = [b1, b2, b3]
    for block in chain:
        print(block)

    # attack the chain
    chain[1].transactions[0]["recipient"] = "t"

    # successful!
    for block in chain:
        print(block)

    for block in chain:
        block.hash = Block.f_hash(block)
        print(block)

    chain[1].transactions[0]["recipient"] = "l"
    #https://bitcoin.stackexchange.com/questions/71855/tampering-with-the-last-block

    for i, block in enumerate(chain):
        print(i)
        print(block)
        print(Block.f_hash(block))
        assert block.hash == Block.f_hash(block), "Assert Block {i} is corrupted".format(i=i)

    # attack still possible, Block are rather "isolated"
    # change data and update hash
    # remove entire block
    # need better method...
