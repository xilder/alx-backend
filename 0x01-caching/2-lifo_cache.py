#!/usr/bin/env python3
"""
LIFO cache class
"""
from collections import deque


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    FIFOCache class
    """
    def __init__(self):
        """init"""
        super().__init__()
        self.queue = deque()


    def put(self, key, item):
        """put method"""
        if key and item:
            if (
                len(self.cache_data.keys()) == self.MAX_ITEMS
                and key not in self.cache_data.keys()
                ):
                k = self.queue.pop()
                del self.cache_data[k]
                print(f"DISCARD: {k}")

            self.queue.append(key)
            self.cache_data[key] = item


    def get(self, key):
        """get method"""
        if key:
            return self.cache_data.get(key, None)
