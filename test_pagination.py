import unittest
from pagination import Pagination


class TestPagination(unittest.TestCase):
    def test_init(self):
        pagination = Pagination(total=100, per_page=10, current=1)
        self.assertIsNotNone(pagination)

        with self.assertRaises(Pagination.InitException):
            pagination = Pagination(total=-1, per_page=100, current=1)

        with self.assertRaises(Pagination.InitException):
            pagination = Pagination(total=100, per_page=101, current=1)

        with self.assertRaises(Pagination.InitException):
            pagination = Pagination(total=100, per_page=10, current=11)

        with self.assertRaises(Pagination.InitException):
            pagination = Pagination(total=100, per_page=-1, current=1)

        with self.assertRaises(Pagination.InitException):
            pagination = Pagination(total=100, per_page=10, current=-1)

    def test_get_offset(self):
        p1 = Pagination(total=100, per_page=10, current=1)
        self.assertEqual(0, p1.get_offset())

        p2 = Pagination(total=100, per_page=10, current=2)
        self.assertEqual(10, p2.get_offset())
