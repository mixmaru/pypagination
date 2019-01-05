class Pagination():
    def __init__(self, total, per_page, current):
        self._check_init_params(total, per_page, current)
        self._total = total
        self._per_page = per_page
        self._current = current

    def get_offset(self):
        return self._per_page * (self._current - 1)

    def get_limit(self):
        return (self._per_page * self._current) - 1

    def _check_init_params(self, total, per_page, current):
        if total < 0 or per_page < 0 or current < 0:
            raise self.InitException("totalが適正ではありません。total:{0} per_page:{1} current:{2}".format(total, per_page, current))

        if per_page > total:
            raise self.InitException("per_pageが適正ではありません。total:{0} per_page:{1} current:{2}".format(total, per_page, current))

        first_of_current_page = (current - 1) * per_page
        if not (0 <= first_of_current_page < total):
            raise self.InitException("currentが適正ではありません。total:{0} per_page:{1} current:{2}".format(total, per_page, current))

    class InitException(Exception):
        pass
