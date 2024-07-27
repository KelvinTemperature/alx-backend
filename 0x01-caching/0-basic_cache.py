#!/usr/bin/env python3
"""Basic Cache Module"""

BaseCache = __import__('base_caching').BaseCaching


class BasicCache(BaseCache):
    """Basic Cache Class"""
    def put(self, key, item):
        if key is None or item is None:
            pass
        self.cache_data[key] = item

    def get(self, key):
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
