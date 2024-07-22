#!/usr/bin/env python3
"""Simple Pagination Module"""
import csv
import math
from typing import List, Dict

index_range = __import__('0-simple_helper_function').index_range

class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get page function
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        range = index_range(page, page_size)
    
        r_data = self.dataset()

        return r_data[range[0]:range[1]]
    
    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """get hypermedia Pagination details
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
            
        data_set = self.dataset()
        range_data = self.get_page(page, page_size)
        page_length = int(len(data_set) / page_size)
        r_hyper = {
            'page_size': len(range_data),
            'page': page,
            'data': range_data,
            'next_page': page + 1 if (self.get_page(page + 1, page_size) != []) else None,
            'prev_page': page - 1 if page - 1 != 0 else None,
            'total_pages': int(len(data_set) / page_size) if len(data_set) % page_size == 0 \
                else page_length + 1,
        }
        return r_hyper