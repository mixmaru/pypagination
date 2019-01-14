class Pagination():
    def __init__(self, total, per_page, current):
        self.__check_init_params(total, per_page, current)
        self.__total = total
        self.__per_page = per_page
        self.__current = current

    def __check_init_params(self, total, per_page, current):
        if total < 0 or per_page < 0 or current < 0:
            raise ValueError(1, "引数が適正ではありません。total:{0} per_page:{1} current:{2}".format(total, per_page, current))

        first_of_current_page = (current - 1) * per_page
        if not (0 <= first_of_current_page < total):
            raise ValueError(2, "currentが適正な範囲ではありません。total:{0} per_page:{1} current:{2}".format(total, per_page, current))

    def get_offset(self):
        return self.__per_page * (self.__current - 1)

    def get_max_page_num(self):
        if self.__total % self.__per_page == 0:
            return self.__total // self.__per_page
        else:
            return self.__total // self.__per_page + 1

    def get_pagination_links(self, num):
        ret_data = []
        for page_num in self.get_pagination_page_nums(num):
            ret_data.append(self.__create_pagination_data(page_num))

        return ret_data

    def get_pagination_page_nums(self, num):
        if num % 2 == 0:
            start = self.__current - ((num // 2) - 1)
        else:
            start = self.__current - (num // 2)

        end = start + num - 1
        start, end = self.__adjust_start_end(start, end)

        return list(range(start, end + 1))

    def __create_pagination_data(self, page_num):
        return {
            "page": page_num,
            "is_current": page_num == self.__current,
        }

    # startが0以下になっていたり、endが存在するページ数を超えた値になっていたらそれぞれ範囲内になるように調整する
    def __adjust_start_end(self, start, end):
        ret_start = start
        ret_end = end

        if start <= 0:
            # startが0以下なら1にして、その分endを正方向にズラす
            ret_start = 1
            ret_end = end + abs(start - 1)
        if ret_end > self.get_max_page_num():
            # endが最大ページ数より大きければ、endを最大ページ数にし、減らした分startを負方向にズラす
            ret_start = ret_start - (ret_end - self.get_max_page_num())
            ret_end = self.get_max_page_num()
            if ret_start < 1:
                ret_start = 1

        return ret_start, ret_end
