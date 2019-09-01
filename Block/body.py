from attr import attrs, attrib
from random import randint


@attrs(frozen=True)
class Body:
    # txs = attrib(init=False, factory=list)
    txs = attrib(init=False, default=randint(0, 10000000000))

    # @txs.validator
    # def data_check(self, attribute, value):
    #     if len(value) >= 10:
    #         raise ValueError("the length of transactions should be less then 10")
    #     pass
