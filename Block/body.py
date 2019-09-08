from functools import partial

from attr import attrs, attrib
from random import randint


@attrs
class Body:
    txs = attrib(default=[0])
