#!/usr/bin/env python3
"""Simple Helper Function Module"""

from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple:
    """Index Range Function"""
    return (page_size * (page - 1), page * page_size)
