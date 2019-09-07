from functools import partial

from attr import attrs, attrib
from random import randint


@attrs
class Body:
    txs = attrib(init=False)

    @txs.default
    def __txs_default(self):
        return [randint(0, 100000000) for _ in range(100)]
