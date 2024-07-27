#!/usr/bin/env python3
"""FiFO Cache Module"""
from collections import OrderedDict

from base_caching import BaseCaching


class MRUCache(BaseCache):
    """Class of MRU Cache"""
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add a key using MRU Algo
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                mru, _ = self.cache_data.popitem(False)
                print("DISCARD: ", mru)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=False)

    def get(self, key):
        """Retrieves an item by key.
        """
        return self.cache_data.get(key, None)
