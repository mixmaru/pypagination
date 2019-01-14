import unittest
from pagination import Pagination


class TestPagination(unittest.TestCase):
    def test_init(self):
        pagination = Pagination(total=100, per_page=10, current=1)
        self.assertIsNotNone(pagination)

        with self.assertRaises(ValueError):
            pagination = Pagination(total=-1, per_page=100, current=1)

        with self.assertRaises(ValueError):
            pagination = Pagination(total=100, per_page=-1, current=1)

        with self.assertRaises(ValueError):
            pagination = Pagination(total=100, per_page=10, current=-1)

        with self.assertRaises(ValueError):
            pagination = Pagination(total=100, per_page=10, current=11)

    def test_get_offset(self):
        p1 = Pagination(total=100, per_page=10, current=1)
        self.assertEqual(0, p1.get_offset())

        p2 = Pagination(total=100, per_page=10, current=2)
        self.assertEqual(10, p2.get_offset())

    def test_get_max_page_num(self):
        p1 = Pagination(total=100, per_page=10, current=1)
        self.assertEqual(10, p1.get_max_page_num())

        p1 = Pagination(total=101, per_page=10, current=1)
        self.assertEqual(11, p1.get_max_page_num())

    def test_get_pagination_page_nums(self):
        p4 = Pagination(total=100, per_page=10, current=5)
        self.assertEqual([3,4,5,6,7], p4.get_pagination_page_nums(5))

        p1 = Pagination(total=100, per_page=10, current=1)
        self.assertEqual([1,2,3,4,5], p1.get_pagination_page_nums(5))

        p2 = Pagination(total=100, per_page=10, current=1)
        self.assertEqual([1,2], p2.get_pagination_page_nums(2))

        p3 = Pagination(total=100, per_page=10, current=10)
        self.assertEqual([6,7,8,9,10], p3.get_pagination_page_nums(5))

        p5 = Pagination(total=100, per_page=10, current=2)
        self.assertEqual([1,2,3,4,5], p5.get_pagination_page_nums(5))

        p6 = Pagination(total=100, per_page=10, current=9)
        self.assertEqual([6,7,8,9,10], p6.get_pagination_page_nums(5))

        # ページネーションが正しくでなかったバグ対応
        p7 = Pagination(total=7, per_page=2, current=1)
        self.assertEqual([1,2,3,4], p7.get_pagination_page_nums(5))

    def test_get_pagination_links(self):
        p = Pagination(total=100, per_page=10, current=5)
        expect = [
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
        self.assertEqual(expect, p.get_pagination_links(num=5))
