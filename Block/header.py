import datetime

from attr import attrib, attrs

consensus_args = ["POW"]


@attrs
class Header:
    prev_block_hash = attrib(default=0)
    version = attrib(default="1.0", converter=str)
    consensus = attrib(default="POW")
    nonce = attrib(default=0)
    bits = attrib(default=0)
    timestamp = attrib(init=False)

    @timestamp.default
    def __timestamp_default(self):
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


if __name__ == '__main__':
    a = Header()
    print(a.timestamp)
