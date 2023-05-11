import cProfile, pstats, io
import functools


def profile_deco(func):
    def wrapper(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        res = func(*args, **kwargs)
        pr.disable()
        # print(s.getvalue())
        # func_name = func.__name__
        return pr.print_stats()

    return wrapper


# def profile_deco(print_stats):
#     def print_stats(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             pr = cProfile.Profile()
#             pr.enable()
#             res = func(*args, **kwargs)
#             pr.disable()
#             return pr.print_stats()
#         func.print_stats = print_stats
#         return wrapper
#
#     return print_stats


@profile_deco
def add(a, b):
    return a + b


@profile_deco
def sub(a, b):
    return a - b


if __name__ == "__main__":
    add(1, 2)
    add(4, 5)
    sub(4, 5)
    add.print_stats()

# add.print_stat()  # выводится результат профилирования суммарно по всем вызовам функции add (всего два вызова)
# sub.print_stat()  # выводится результат профилирования суммарно по всем вызовам функции sub (всего один вызов)
