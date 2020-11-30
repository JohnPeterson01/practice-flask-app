import redis


class BaseCache:
    def __init__(self, config):
        self.cache = redis.Redis(
            host=config.REDIS_HOSTNAME,
            port=config.REDIS_PORT,
            db=0
        )
        self.DEFAULT_EXPIRY_SECONDS = 60
    
    def get(self, key):
        val = self.cache.get(key)
        return val
    
    def set(self, key, val, ex=None):
        if ex is None:
            ex = self.DEFAULT_EXPIRY_SECONDS

        self.cache.set(key, val, ex=ex)
    
    def delete(self, key):
        self.cache.delete(key)