from attr import attrs, attrib
import hashlib

# TODO: 支持两次hash
# TODO：支持 Big Endian to Little Endian 的转换
# https://livc.io/blog/209

@attrs()
class POW:
    difficulty = attrib(init=False, default=20, type=int)
    max_nonce = attrib(init=False, default=2 ** 64, type=int)
    target = attrib(init=False)

    @target.default
    def target_default(self):
        return 2 ** (256 - self.difficulty)

    def mine(self, data):
        for nonce in range(self.max_nonce):
            hash_result = hashlib.sha256(("".join(data) + str(nonce)).encode()).hexdigest()
            decimal_hash = int(hash_result, 16)
            if decimal_hash < self.target:
                return True, hash_result, nonce, self.target

    def check(self, **kwargs):
        data = ""
        nonce = ""
        for key, value in kwargs.items():
            if key == "DATA":
                data = value
            if key == "NONCE":
                nonce = str(value)
        if int(hashlib.sha256(("".join(data) + nonce).encode()).hexdigest(), 16) < self.target:
            return True
        else:
            return False


pow = POW()
