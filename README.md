# pypagination
simple pagination class for python

# usage
## getting offset for SQL statement
```
p1 = Pagination(total=100, per_page=10, current=1)
p1.get_offset()  # 0

p2 = Pagination(total=100, per_page=10, current=2)
p2.get_offset()  # 10
```

## getting max page
```
p1 = Pagination(total=100, per_page=10, current=1)
p1.get_max_page_num()  # 10

p2 = Pagination(total=101, per_page=10, current=1)
p2.get_max_page_num()  # 11
```

## getting pagination data
```
p = Pagination(total=100, per_page=10, current=5)
p.get_pagination_links(num=5)
"""
[
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
"""

```
