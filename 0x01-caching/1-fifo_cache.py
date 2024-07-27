#!/usr/bin/env python3
"""FiFO Cache Module"""
from collections import OrderedDict

BaseCache = __import__('base_caching').BaseCaching


class FIFOCache(BaseCache):
    """Class of Fifo Cache"""
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCache.MAX_ITEMS:
            first, _ = self.cache_data.popitem(False)
            print("DISCARD: ", first)

    def get(self, key):
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
