#!/usr/bin/env python3
import csv
import math
from typing import List, Dict
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
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """returns the an object with index
        of the current page, the next index, page_size and data"""
        indexed_dataset = self.__indexed_dataset
        assert (
            index >= 0
            and index < len(indexed_dataset)
            and isinstance(index, int)
        )
        hyper_index = {}
        data = []
        count = 0
        try:
            for k, v in indexed_dataset.items():
                if k >= index and count < page_size:
                    data.append(v)
                    count += 1
                elif count == page_size:
                    hyper_index['next_index'] = int(k)
                    break
        except KeyError:
            pass

        hyper_index['index'] = index
        hyper_index['data'] = data
        hyper_index['page_size'] = page_size
        return hyper_index
