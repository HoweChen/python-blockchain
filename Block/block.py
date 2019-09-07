from attr import attrs, attrib
import datetime
from Block.body import Body
import hashlib
from functools import partial

from Block.head import Head
from Consensus.pow import POW
import sys


@attrs()
class Block:
    # in this case we don't have a head of blockchain because a Block class can have such function
    head = attrib(init=False, factory=Head)
    body = attrib(init=False, factory=Body)
    transaction_counter = attrib(init=False)
    block_size = attrib(init=False)
    magic_no = attrib(init=False, default=0xD9B4BEF9)  # https://en.bitcoin.it/wiki/Block

    def __attrs_post_init__(self):
        self.transaction_counter = len(self.body.txs)
        self.block_size = sys.getsizeof(self)


if __name__ == '__main__':
    a = Block()
    b = Block()
    print(id(a))
    print(id(b))
    print(a == b)
    print(a.head.timestamp)
