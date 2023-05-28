import asyncio
import aiohttp
import argparse
import aiofiles
import time
from sys import argv


count = 0


async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            global count
            count += 1
            assert resp.status == 200


async def run_worker(queue):
    while True:
        url = await queue.get()
        try:
            await fetch_url(url)
        finally:
            queue.task_done()


async def main(workers_amount, url_filename):
    urls = []
    async with aiofiles.open(
            url_filename, mode='r', encoding='utf-8'
    ) as url_f:
        line = await url_f.readline()
        while line:
            urls.append(line)
            line = await url_f.readline()
    queue = asyncio.Queue()
    workers = [
        asyncio.create_task(run_worker(queue))
        for _ in range(int(workers_amount))
    ]

    for url in urls:
        await queue.put(url)

    await queue.join()

    for work in workers:
        work.cancel()


if __name__ == '__main__':
    if len(argv) == 4:
        number_of_workers = int(argv[2])
        filename = argv[3]
    elif len(argv) == 3:
        number_of_workers = int(argv[1])
        filename = argv[2]
    # parser = argparse.ArgumentParser()
    # parser.add_argument('-c', type=int)
    # parser.add_argument('f', type=str)
    # args = parser.parse_args()
    # number_of_workers, filename = args.c, args.f
    t1 = time.time()
    asyncio.run(main(number_of_workers, filename))
    t2 = time.time()
    print(f"Script works. All {count} urls involved in.", "TIME is", t2 - t1)
