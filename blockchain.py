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
        new_block = Block.with_param(PREVIOUS_HASH=self.blocks[-1].header)
        print_block(new_block)
        self.blocks.append(new_block)
        # if self.consensus.check(
        #         ("{:%B %d, %Y}".format(new_block.head.timestamp) + str(new_block.body.txs)).encode()) is True:
        #     self.blocks.append(new_block)


def print_block(new_block):
    print(f'Block ID: {id(new_block)}')
    print(f'Block header: ')
    print(f'\tPrevious block hash: {new_block.header.prev_block_hash}')
    print(f'\tNonce: {new_block.header.nonce}')
    print(f'\tDifficulty: {new_block.header.bits}')
    print(f'\tTimestamp: {new_block.header.timestamp}')

    print(f'Block body: ')
    print(f'\tBlock TXs: {new_block.body.txs}')
    print(f'Block size(bytes): {new_block.block_size}')

    print(f'Block transaction counter: {new_block.transaction_counter}')
    print(f'Block size(bytes): {new_block.block_size}')
    print("---------------------")


if __name__ == '__main__':
    cyh_chain = Blockchain()
    for i in range(10):
        cyh_chain.add_block()
        time.sleep(1)
    # print(cyh_chain)
