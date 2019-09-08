from attr import attrs, attrib
import time

from Block.block import Block
from Consensus.pow import POW
from random import randint


@attrs()
class Blockchain:
    consensus_module = attrib(factory=POW)
    blocks = attrib(init=False)
    num = attrib(init=False, default=0)
    version = attrib(default="1.0", converter=str)

    @blocks.default
    def __blocks_default(self):
        # initialize the genesis block
        return [Block(block_hash=0)]

    @blocks.validator
    def __chain_checker(self, attribute, value):
        if not value:
            raise ValueError("the blocks are None")

    def add_block(self, data):
        self.num += 1
        is_appendable, hash_result, nonce, target = self.consensus_module.mine(data=data)
        try:

            if is_appendable and self.consensus_module.check(DATA=data, NONCE=nonce):
                new_block = Block.with_param(
                    BLOCK_HASH=hash_result,
                    PREVIOUS_HASH=self.blocks[-1].block_hash,
                    BODY=data,
                    TARGET=target,
                    NONCE=nonce,
                    VERSION=self.version)
                print_block(new_block)
                self.blocks.append(new_block)
        except Exception as e:
            print(e)
        # if self.consensus.check(
        #         ("{:%B %d, %Y}".format(new_block.head.timestamp) + str(new_block.body.txs)).encode()) is True:
        #     self.blocks.append(new_block)


def print_block(new_block):
    print(f'Block ID: {id(new_block)}')
    print(f'Block hash: {new_block.block_hash}')
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
    print_block(cyh_chain.blocks[0])
    for i in range(10):
        # time.sleep(1)
        data = list(map(str, [randint(0, 100000000) for _ in range(randint(0, 100))]))
        cyh_chain.add_block(data)
    # print(cyh_chain)
