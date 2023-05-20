import logging
import argparse
from lru_cache import LRUCache


def init_logger(name):
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", '--stdout', action="store_true")
    parser.add_argument("-f", '--filter', action="store_true")
    args = parser.parse_args()

    class CustomClass(logging.Filter):
        def filter(self, record):
            return len(record.msg) > 5

    format_sentry = logging.Formatter(
        "%(asctime)s - %(levelno)s - %(levelname)s - %(message)s - %(lineno)d "
    )
    format_file = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(lineno)d - [file] - %(message)s"
    )

    sh = logging.StreamHandler()
    sh.setLevel(logging.DEBUG)
    sh.setFormatter(format_sentry)

    fh = logging.FileHandler("file.log")
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(format_file)
    if args.filter:
        fh.addFilter(CustomClass())

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    if args.stdout:
        logger.addHandler(sh)
    logger.addHandler(fh)


init_logger("name")
info_logger = logging.getLogger("name")
error_logger = logging.getLogger("name")

cache = LRUCache(2)
cache.set("key1", "val1")
cache.set("key2", "val2")


def get_key(key):
    if cache.get(key) is None:
        raise Exception
    return cache.get(key)


def set_key(key, value):
    return cache.set(key, value)


def main():
    try:
        get_key('key4')
        info_logger.debug('working')
    except Exception:
        error_logger.error('NO SUCH KEY')
    try:
        get_key('key1')
        info_logger.debug('working')
    except Exception:
        info_logger.error('NO SUCH KEY')
    try:
        set_key("key3", "val3")
        info_logger.debug('working')
    except Exception as err:
        info_logger.error(err)


if __name__ == "__main__":
    main()
