import pickle

from attr import attrs, attrib
import datetime
from Block.body import Body
import hashlib
from functools import partial

from Block.header import Header
from Consensus.pow import POW
import sys


@attrs()
class Block:
    # in this case we don't have a head of blockchain because a Block class can have such function
    block_hash = attrib()
    header = attrib(factory=Header)
    body = attrib(factory=Body)
    transaction_counter = attrib(init=False)
    block_size = attrib(init=False)
    magic_no = attrib(init=False, default=0xD9B4BEF9)  # https://en.bitcoin.it/wiki/Block

    @classmethod
    def with_param(cls, **kwargs):
        block_hash = None
        previous_hash = None
        nonce = None
        target = None
        block_data = None
        version = None
        for key, value in kwargs.items():
            if key == 'PREVIOUS_HASH':
                previous_hash = value
            elif key == "BODY":
                block_data = value
            elif key == "TARGET":
                target = value
            elif key == "NONCE":
                nonce = value
            elif key == "VERSION":
                version = value
            elif key == "BLOCK_HASH":
                block_hash = value
        return cls(block_hash,
                   Header(prev_block_hash=previous_hash, nonce=nonce, bits=target, version=version),
                   Body(txs=block_data))

    def __attrs_post_init__(self):
        self.transaction_counter = len(self.body.txs)
        self.block_size = sys.getsizeof(self)


if __name__ == '__main__':
    # a = Block()
    # b = Block()
    # print(id(a))
    # print(id(b))
    # print(a == b)
    # print(a.header.timestamp)
    a = Block.with_param(BLOCK_HASH="123", PREVIOUS_HASH="123", BODY=["1", "2", "3"])
    print(a)
