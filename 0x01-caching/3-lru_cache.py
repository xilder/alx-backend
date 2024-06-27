#!/usr/bin/env python3
"""
LRUCache class
"""

BaseCaching = __import__('0-basic_cache').BaseCaching


class LRUCache(BaseCaching):
    """LRUCache class"""
    def __init__(self):
        """init method"""
        super().__init__()
        self.LRU_cache = {}

    def put(self, key, item):
        """put method"""
        if key and item:
            if (
                len(self.cache_data.keys()) == self.MAX_ITEMS
                and key not in self.cache_data.keys()
                and self.LRU_cache  # Least recently used item
            ):
                k = min(self.LRU_cache, key=self.LRU_cache.get)
                del self.cache_data[k]
                del self.LRU_cache[k]
                print(f"DISCARD: {k}")

            v = max(self.LRU_cache.values())\
                if self.LRU_cache else 0
            self.LRU_cache[key] = v + 1
            self.cache_data[key] = item

    def get(self, key):
        """get method"""
        if key and key in self.cache_data.keys():
            v = max(self.LRU_cache.values())
            self.LRU_cache[key] = v + 1

        return self.cache_data.get(key, None)
