#!/usr/bin/env python3
"""
Basic Cache Module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Basic Cache Class
    """
    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item by key.
        """
        return self.cache_data.get(key, None)
