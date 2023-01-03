from collections import deque


class Calculator:
    @staticmethod
    def add(*args):
        result = sum(args)
        return result

    @staticmethod
    def multiply(*args):
        result = 1
        for _ in args:
            result *= _
        return result

    @staticmethod
    def divide(*args):
        this_queue = deque(args)
        first_num = this_queue.popleft()
        this_list = list(this_queue)
        result = first_num
        for _ in this_list:
            result /= _
        return result

    @staticmethod
    def subtract(*args):
        this_queue = deque(args)
        first_num = this_queue.popleft()
        this_list = list(this_queue)
        result = first_num
        for _ in this_list:
            result -= _
        return result
