#!/usr/bin/env python3
"""
basic cache class
"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    basic cache class
    """
    def __init__(self):
        """
        constructor
        """
        super().__init__()

    def put(self, key, item):
        """
        put method
        """
        self.cache_data[key] = item

    def get(self, key):
        """
        get method
        """
        return self.cache_data.get(key, None)
