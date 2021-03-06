class UserCache:
    def __init__(self, base_cache):
        self.cache = base_cache
        self.KEY_PREFIX = 'user:query'
        self.DEFAULT_EXPIRY_SECONDS = 60

    def get(self, operation_name, *args):
        qualified_key = self._make_qualified_key(operation_name, *args)
        return self.cache.get(qualified_key)

    def set(self, operation_name, val, *args):
        qualified_key = self._make_qualified_key(operation_name, *args)
        self.cache.set(qualified_key, val, ex=self.DEFAULT_EXPIRY_SECONDS)
        return

    def delete(self, operation_name, *args):
        qualified_key = self._make_qualified_key(operation_name, *args)
        return self.cache.delete(qualified_key)

    def _make_qualified_key(self, operation_name, *args):
        args_tuple = ''
        if len(args) > 0:
            args_tuple = f':{args}'
        return f'{self.KEY_PREFIX}:{operation_name}{args_tuple}'