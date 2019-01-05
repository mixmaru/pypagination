class Pagination():
    def __init__(self, total, per_page, current):
        self._total = total
        self._per_page = per_page
        self._current = current
