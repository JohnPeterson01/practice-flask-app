import redis


class RedisBase:
    def __init__(self, config):
        
        self.redis = redis.Redis(host=config.REDIS_HOSTNAME, port=config.REDIS_PORT)

