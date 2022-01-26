import redis


class RedisCache(object):
    def __init__(self, logger, db_index):
        self.logger = logger
        self.redis_client = redis.Redis(host='localhost', port=6379, db=db_index)
        self.logger.info(self.redis_client.ping())

    def get(self, key):
        self.logger.info(f"getting value of {key} from redis cache")
        value = self.redis_client.get(key)
        self.logger.info(f"value of {key} is {value}")
        return value

    def set(self, key, value, duration):
        self.logger.info(f"saving value of {key} to redis cache")
        result = self.redis_client.set(key, value, ex=duration)
        return result

    def delete(self, key):
        self.logger.info(f"deleting value of {key} from redis cache")
        result = self.redis_client.delete(key)
        return result
