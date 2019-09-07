from attr import attrs, attrib
import time

from Block.block import Block
from Consensus.pow import POW


@attrs()
class Blockchain:
    consensus = attrib(factory=POW)
    blocks = attrib(init=False)
    num = attrib(init=False, default=0)

    @blocks.default
    def __blocks_default(self):
        return [Block()]

    @blocks.validator
    def __chain_checker(self, attribute, value):
        if not value:
            raise ValueError("the blocks are None")

    def add_block(self):
        self.num += 1
        new_block = Block()
        print(id(new_block))
        print(new_block.head.timestamp)
        print(new_block.body.txs)
        self.blocks.append(new_block)
        print("---------------------")
        # if self.consensus.check(
        #         ("{:%B %d, %Y}".format(new_block.head.timestamp) + str(new_block.body.txs)).encode()) is True:
        #     self.blocks.append(new_block)


if __name__ == '__main__':
    cyh_chain = Blockchain()
    for i in range(10):
        cyh_chain.add_block()
        time.sleep(1)
    # print(cyh_chain)
