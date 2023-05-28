import cProfile
import pstats
import io
from functools import wraps


def profile_deco(func):
    profile = cProfile.Profile()

    @wraps(func)
    def deco(*args, **kwargs):
        profile.enable()
        res = func(*args, **kwargs)
        profile.disable()
        return res

    def print_stat():
        st = io.StringIO()
        sortby = "cumulative"
        ps = pstats.Stats(profile, stream=st).sort_stats(sortby)
        ps.print_stats()
        print(st.getvalue())
    deco.print_stat = print_stat
    return deco


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
    add.print_stat()

# add.print_stat()  # выводится результат профилирования суммарно по всем вызовам функции add (всего два вызова)
# sub.print_stat()  # выводится результат профилирования суммарно по всем вызовам функции sub (всего один вызов)
