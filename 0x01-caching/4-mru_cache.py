#!/usr/bin/env python3
"""
MRUCache class
"""

BaseCaching = __import__('0-basic_cache').BaseCaching


class MRUCache(BaseCaching):
    """MRUCache class"""
    def __init__(self):
        """init method"""
        super().__init__()
        self.MRU_cache = {}

    def put(self, key, item):
        """put method"""
        if key and item:
            if (
                len(self.cache_data.keys()) == self.MAX_ITEMS
                and key not in self.cache_data.keys()
                and self.MRU_cache  # Least recently used item
            ):
                k = max(self.MRU_cache, key=self.MRU_cache.get)
                del self.cache_data[k]
                del self.MRU_cache[k]
                print(f"DISCARD: {k}")

            v = max(self.MRU_cache.values())\
                if self.MRU_cache else 0
            self.MRU_cache[key] = v + 1
            self.cache_data[key] = item

    def get(self, key):
        """get method"""
        if key and key in self.cache_data.keys():
            v = max(self.MRU_cache.values())
            self.MRU_cache[key] = v + 1

        return self.cache_data.get(key, None)
