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

    def test_get_limit(self):
        p1 = Pagination(total=100, per_page=10, current=1)
        self.assertEqual(9, p1.get_limit())

        p2 = Pagination(total=100, per_page=10, current=2)
        self.assertEqual(19, p2.get_limit())

    def test_get_pagination_links(self):
        p1 = Pagination(total=100, per_page=10, current=1)
        expect1 = [
            {
                "page": 1,
                "is_current": True
            },
            {
                "page": 2,
                "is_current": False
            },
            {
                "page": 3,
                "is_current": False
            },
            {
                "page": 4,
                "is_current": False
            },
            {
                "page": 5,
                "is_current": False
            },
        ]
        self.assertEqual(expect1, p1.get_pagination_links(num=5))

        p2 = Pagination(total=100, per_page=10, current=1)
        expect2 = [
            {
                "page": 1,
                "is_current": True
            },
            {
                "page": 2,
                "is_current": False
            },
        ]
        self.assertEqual(expect2, p2.get_pagination_links(num=2))

        p3 = Pagination(total=100, per_page=10, current=10)
        expect3 = [
            {
                "page": 6,
                "is_current": False
            },
            {
                "page": 7,
                "is_current": False
            },
            {
                "page": 8,
                "is_current": False
            },
            {
                "page": 9,
                "is_current": False
            },
            {
                "page": 10,
                "is_current": True
            },
        ]
        self.assertEqual(expect3, p3.get_pagination_links(num=5))

        p4 = Pagination(total=100, per_page=10, current=5)
        expect4 = [
            {
                "page": 3,
                "is_current": False
            },
            {
                "page": 4,
                "is_current": False
            },
            {
                "page": 5,
                "is_current": True
            },
            {
                "page": 6,
                "is_current": False
            },
            {
                "page": 7,
                "is_current": False
            },
        ]
        self.assertEqual(expect4, p4.get_pagination_links(num=5))

        p4 = Pagination(total=100, per_page=10, current=2)
        expect4 = [
            {
                "page": 1,
                "is_current": False
            },
            {
                "page": 2,
                "is_current": True
            },
            {
                "page": 3,
                "is_current": False
            },
            {
                "page": 4,
                "is_current": False
            },
            {
                "page": 5,
                "is_current": False
            },
        ]
        self.assertEqual(expect4, p4.get_pagination_links(num=5))

        p5 = Pagination(total=100, per_page=10, current=9)
        expect5 = [
            {
                "page": 6,
                "is_current": False
            },
            {
                "page": 7,
                "is_current": False
            },
            {
                "page": 8,
                "is_current": False
            },
            {
                "page": 9,
                "is_current": True
            },
            {
                "page": 10,
                "is_current": False
            },
        ]
        self.assertEqual(expect5, p5.get_pagination_links(num=5))

        p6 = Pagination(total=100, per_page=10, current=5)
        expect6 = [
            {
                "page": 3,
                "is_current": False
            },
            {
                "page": 4,
                "is_current": False
            },
            {
                "page": 5,
                "is_current": True
            },
            {
                "page": 6,
                "is_current": False
            },
            {
                "page": 7,
                "is_current": False
            },
        ]
        self.assertEqual(expect6, p6.get_pagination_links(num=5))
