class Pagination():
    def __init__(self, total, per_page, current):
        self._check_init_params(total, per_page, current)
        self._total = total
        self._per_page = per_page
        self._current = current

    def _check_init_params(self, total, per_page, current):
        if total < 0 or per_page < 0 or current < 0:
            raise ValueError(1, "引数が適正ではありません。total:{0} per_page:{1} current:{2}".format(total, per_page, current))

        first_of_current_page = (current - 1) * per_page
        if not (0 <= first_of_current_page < total):
            raise ValueError(2, "currentが適正な範囲ではありません。total:{0} per_page:{1} current:{2}".format(total, per_page, current))

    def get_offset(self):
        return self._per_page * (self._current - 1)

    def get_max_page_num(self):
        if self._total % self._per_page == 0:
            return self._total // self._per_page
        else:
            return self._total // self._per_page + 1

    def get_pagination_links(self, num):
        ret_data = []
        for page_num in self.get_pagination_page_nums(num):
            ret_data.append(self._create_pagination_data(page_num))

        return ret_data

    def get_pagination_page_nums(self, num):
        if num % 2 == 0:
            start = self._current - ((num // 2) - 1)
        else:
            start = self._current - (num // 2)

        end = start + num - 1
        start, end = self._adjust_start_end(start, end)

        return list(range(start, end + 1))

    def _create_pagination_data(self, page_num):
        return {
            "page": page_num,
            "is_current": page_num == self._current,
        }

    def _adjust_start_end(self, start, end):
        ret_start = start
        ret_end = end
        if start < 1:
            ret_start = 1
            ret_end = end + abs(start - 1)
        if end > self.get_max_page_num():
            ret_end = self.get_max_page_num()
            ret_start = ret_start - (end - self.get_max_page_num())
            if ret_start < 1:
                ret_start = 1

        return ret_start, ret_end
