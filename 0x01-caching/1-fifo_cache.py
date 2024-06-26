#!/usr/bin/env python3
"""
FIFO cache class
"""
from collections import deque


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
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
            self.queue.append(key)
            self.cache_data[key] = item

        if len(self.cache_data.keys()) > self.MAX_ITEMS:
            k = self.queue.popleft()
            del self.cache_data[k]
            print(f"DISCARD: {k}")


    def get(self, key):
        """get method"""
        if key:
            return self.cache_data.get(key, None)
