import unittest
from pagination import Pagination


class TestPagination(unittest.TestCase):
    def test_pagination_init(self):
        pagination = Pagination(total=100, per_page=10, current=1)
        self.assertIsNotNone(pagination)