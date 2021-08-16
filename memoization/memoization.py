def memoize(fn, key_generator):
    """
    This will return a memoized version of the given function.
    :param fn: The function to memoize.
    :param key_generator: The function that will generate the key based on the input parameters.
    :return:
    """
    cache = {}

    def memoized(*args, **kwargs):
        key = key_generator(*args, **kwargs)
        if key in cache:
            return cache[key]

        else:
            res = fn(*args, **kwargs)
            cache[key] = res
            return res

    def clear_keys(keys=None):
        if keys is None:  # clear all the cache
            cache.clear()
        else:
            for key in keys:
                if key in cache:
                    del cache[key]

    memoized.clear = clear_keys
    return memoized
