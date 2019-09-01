from attr import attrs, attrib
import time

from Block.block import Block
from Consensus.pow import POW


@attrs()
class Blockchain:
    blocks = attrib(init=False, default=[Block(num=0, prev_hash=0)])
    num = attrib(init=False, default=0)
    consensus = attrib(factory=POW)

    @blocks.validator
    def chain_checker(self, attribute, value):
        if not value:
            raise ValueError("the blocks are None")

    def add_block(self):
        self.num += 1
        self.blocks.append(Block(num=self.num, prev_hash=self.blocks[-1].hash))


if __name__ == '__main__':
    cyh_chain = Blockchain()
    for i in range(10):
        cyh_chain.add_block()
    # print(cyh_chain)
