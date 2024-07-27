#!/usr/bin/env python3
"""
Basic Cache Module
"""

BaseCache = __import__('base_caching').BaseCaching


class BasicCache(BaseCache):
    """
    Basic Cache Class
    """
    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is None or item is None:
            pass
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item by key.
        """
        return self.cache_data.get(key, None)
