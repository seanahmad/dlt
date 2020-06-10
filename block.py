import json
import hashlib

from time import time

class Bblock(object):

    def __enter__(self):
        # make a database connection and return it
        self.block = Block()
        return self.block

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(self.block.time)
        print(self.block.transactions)
        print(self.block.proof)
        print(self.block)
        # make sure the dbconnection gets closed
        # self.__time = round(time(), 3)

        #self.dbconn.close()

    # def append_transaction(self, sender, recipient, amount):
    #     """
    #     Creates a new transaction to go into the next mined Block
    #     :param sender: <str> Address of the Sender
    #     :param recipient: <str> Address of the Recipient
    #     :param amount: <int> Amount
    #     :return: <int> The index of the Block that will hold this transaction
    #     """
    #     self.__transactions.append({
    #         'sender': sender,
    #         'recipient': recipient,
    #         'amount': amount,
    #     })




class Block(object):
    @staticmethod
    def f_hash(block):
        assert block is not None

        block_dict = {"timestamp": block.time, "previous": block.previous, "transactions": block.transactions, "proof": block.proof}
        block_string = json.dumps(block_dict, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()


    def __init__(self, previous=None, proof=1):
        self.__time = round(time(),3)
        self.__previous = previous
        self.__transactions = []
        self.__proof = proof

    @property
    def proof(self):
        return self.__proof

    @property
    def time(self):
        return self.__time

    @property
    def previous(self):
        return self.__previous

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
        return str({"timestamp": self.time, "previous": self.previous, "transactions": self.transactions, "proof": self.proof})


class Chain(object):
    def __init__(self):
        # always prefer composition over inheritance
        self.__chain = []

    def create_block(self):
        if not self.__chain:
            return Block()
        else:
            previous_block = self.__chain[-1]
            # get the hash code of the previous block
            hash = Block.f_hash(previous_block)
            # get the proof
            proof = self.proof_of_work(previous_block.proof)
            # construct a new block.
            return Block(previous = hash, proof = proof)

    def append(self, block):
        self.__chain.append(block)

    #def __getitem__(self, item):
    #    return self.__chain[item]

    def verify(self):
        for a1, a2 in zip(self.__chain[:-1], self.__chain[1:]):
            assert a2.previous == Block.f_hash(a1), "Corrupted data"


    @property
    def validate(self):
        return True

    def proof_of_work(self, last_proof):
        """
        Simple Proof of Work Algorithm:
         - Find a number p' such that hash(pp') contains leading 4 zeroes, where p is the previous p'
         - p is the previous proof, and p' is the new proof
        :param last_proof: <int>
        :return: <int>
        """

        proof = last_proof
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

    def __iter__(self):
        for block in self.__chain:
            yield block


    @staticmethod
    def valid_proof(last_proof, proof):
        """
        Validates the Proof: Does hash(last_proof, proof) contain 4 leading zeroes?
        :param last_proof: <int> Previous Proof
        :param proof: <int> Current Proof
        :return: <bool> True if correct, False if not.
        """

        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()

        return guess_hash[:4] == "0000"


# if __name__ == '__main__':
#     chain = Chain()
#
#     # construct the Genesis Block
#     b1 = chain.create_block()
#     # append some transactions
#     b1.append_transaction(sender="a", recipient="b", amount=10.0)
#     b1.append_transaction(sender="a", recipient="c", amount=30.0)
#     chain.append(b1)
#
#     # mine a second block
#     b2 = chain.create_block()
#     b2.append_transaction(sender="c", recipient="b", amount=20.0)
#     chain.append(b2)
#
#
#     # various miners are now trying to validate and solve the Proof by Work problem:
#     if chain.validate:
#
#         #b2 = chain.append_block()
#         #print(b2)
#
#         #b2.append_transaction(sender="c", recipient="b", amount=20.0)
#         #b2.hash = Block.f_hash(b2)
#
#         chain.verify()
#
#         for block in chain:
#             print(block)
#
#     #assert False
#
#     #for a1, a2 in zip(chain[:-1], chain[1:]):
#     #    assert a2.previous == Block.hash(a1)
#
#
#

if __name__ == '__main__':
    with Bblock() as block:
        block.append_transaction(sender="c", recipient="b", amount=20.0)
