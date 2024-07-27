#!/usr/bin/env python3
"""FiFO Cache Module"""
from collections import OrderedDict

BaseCache = __import__('base_caching').BaseCaching


class LIFOCache(BaseCache):
    """Class of Lifo Cache"""
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()
        
    def put(self, key, item):
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCache.MAX_ITEMS:
                last, _ = self.cache_data.popitem(True)
                print("DISCARD: ", last)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)
        
    def get(self, key):
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]