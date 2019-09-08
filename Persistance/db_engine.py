from attr import attrs, attrib
from Persistance.redis import RedisEngine


@attrs()
class Engine:
    engine = attrib(factory=RedisEngine)
