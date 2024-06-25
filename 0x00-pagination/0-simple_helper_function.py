#!/usr/bin/env python3
"""
a function that return a tuple of size two containing
a start index and an end inndex corresponding to the range
of indexes to return in a list for those particular
pagination parameters
"""


def index_range(page, page_size):
    """
    pagination function
    """
    start_index = page * page_size - page_size
    end_index = page * page_size
    return (start_index, end_index)