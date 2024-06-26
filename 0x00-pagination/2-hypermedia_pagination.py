#!/usr/bin/env python3
import csv
import math
from typing import List
"""
a function that return a tuple of size two containing
a start index and an end index corresponding to the range
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
        """
        return content of desired page and page size as a list
        empty list if page is out of range
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        start, end = index_range(page, page_size)
        try:
            return self.dataset()[start: end]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """returns an object with certain values"""
        dataset = self.dataset()
        len_dataset = len(dataset)
        hyper_data = {}
        hyper_data['page'] = page
        hyper_data['data'] = self.get_page(page, page_size)
        hyper_data['page_size'] = page_size
        hyper_data['total_pages'] = math.ceil(len_dataset / page_size)
        hyper_data['next_page'] = page + 1 if page < hyper_data['total_pages']\
            else None
        hyper_data['prev_page'] = page - 1 if page > 1 else None

        return hyper_data
