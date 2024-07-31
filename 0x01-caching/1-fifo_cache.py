#!/usr/bin/env python3
"""FiFO Cache Module"""
from collections import OrderedDict

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Class of Fifo Cache"""
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds content following FiFo Algo
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first, _ = self.cache_data.popitem(False)
            print("DISCARD: ", first)

    def get(self, key):
        """Retrieves an item by key.
        """
        return self.cache_data.get(key, None)
