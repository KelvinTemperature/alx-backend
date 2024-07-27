#!/usr/bin/env python3
"""FiFO Cache Module"""
from collections import OrderedDict

BaseCache = __import__('base_caching').BaseCaching


class LRUCache(BaseCache):
    """Class of LRU Cache"""
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add a key using LRU algo
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCache.MAX_ITEMS:
                lru, _ = self.cache_data.popitem(True)
                print("DISCARD: ", lru)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=False)

    def get(self, key):
        """Retrieves an item by key.
        """
        return self.cache_data.get(key, None)
