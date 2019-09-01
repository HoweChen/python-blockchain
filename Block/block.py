from attr import attrs, attrib
import datetime
from Block.body import Body
from Consensus.pow import POW
import hashlib


@attrs()
class Block:
    # in this case we don't have a head of blockchain because a Block class can have such function

    num = attrib()
    prev_hash = attrib()
    hash = attrib(init=False)
    timestamp = attrib(init=False, factory=datetime.datetime.now)
    body = attrib(factory=Body)
    consensus = attrib(factory=POW)
    magic_no = attrib(default=0xD9B4BEF9)  # https://en.bitcoin.it/wiki/Block

    def __attrs_post_init__(self):
        self.hash = hashlib.sha256(
            bytes("{:%B %d, %Y}".format(self.timestamp) + str(self.num), encoding="utf8")).hexdigest()
        print(f"block num: {self.num}")
        print(f"prev hash: {self.prev_hash}")
        print(f"self hash: {self.hash}")
        # print(f"head hash: {hash(self.head)}")
        print(f"head timestamp: {self.timestamp}")
        # print(f"body hash: {hash(self.body)}")
        print(f"txs: {self.body.txs}")
        print("------------------------------")


if __name__ == '__main__':
    test = Block(num=0, prev_hash=0)
    another = Block(num=1, prev_hash=1)
    print(test)
    print(another)
    print(another == test)
