from datetime import datetime, timedelta


class ExpirationHandler:

    def set_expiration(self, name, expiration):
        raise NotImplemented

    def exists(self, name):
        raise NotImplemented

    def is_expired(self, name):
        raise NotImplemented

    def remove(self, name):
        raise NotImplemented


class MemoryExpirationHandler(ExpirationHandler):

    def __init__(self):
        self.time_holders = {}

    @staticmethod
    def get_now():
        return datetime.now()

    def set_expiration(self, name, expiration):
        self.time_holders[name] = self.get_now() + timedelta(seconds=expiration)

    def exists(self, name):
        return name in self.time_holders

    def is_expired(self, name):
        try:
            expiration = self.time_holders.get(name)
            return expiration < self.get_now()
        except KeyError:
            return True

    def remove(self, name):
        try:
            self.time_holders.pop(name)
        except KeyError:
            pass

    def clear_expired(self):
        for k, v in self.time_holders.items():
            if v < self.get_now():
                del self.time_holders[k]


class RedisExpirationHandler(ExpirationHandler):
    def __init__(self, get_connection_fn):
        self.get_connection_fn = get_connection_fn

    def get_connection(self):
        try:
            return self.get_connection_fn()
        except Exception:
            return None

    def set_expiration(self, name, expiration):
        redis_connection = self.get_connection()
        redis_connection.set(name=name, value='locked', ex=expiration, nx=True)

    def exists(self, name):
        redis_connection = self.get_connection()
        return redis_connection.exists(name)

    def is_expired(self, name):
        redis_connection = self.get_connection()
        ttl = redis_connection.ttl(name)
        return ttl and ttl > 0

    def remove(self, name):
        redis_connection = self.get_connection()
        redis_connection.delete(name)
