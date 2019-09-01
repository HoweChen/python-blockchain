from attr import attrs, attrib


@attrs()
class POW:
    difficulty = attrib(init=False, default=24, type=int)


pow = POW()