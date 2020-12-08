import redis
import json


class BaseCache:
    def __init__(self, config):
        self.cache = redis.Redis(
            host=config.REDIS_HOSTNAME,
            port=config.REDIS_PORT,
            db=0
        )
        self.DEFAULT_EXPIRY_SECONDS = 60
    
    def get(self, key):
        bytes_val = self.cache.get(key)
        if bytes_val is None:
            return bytes_val
        value_to_return = self._decode_bytes(bytes_val)
        return value_to_return
    
    def set(self, key, val, ex=None):
        if ex is None:
            ex = self.DEFAULT_EXPIRY_SECONDS

        self.cache.set(key, val, ex=ex)
    
    def delete(self, key):
        self.cache.delete(key)

    def _decode_bytes(self, raw_result):
        return raw_result.decode()

    def flush_all(self):
        return self.cache.flushall(asynchronous=False)
