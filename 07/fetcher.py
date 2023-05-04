import asyncio
import aiohttp
import time
from sys import argv

if len(argv) == 4:
    c = int(argv[2])
    filename = argv[3]
elif len(argv) == 3:
    c = int(argv[1])
    filename = argv[2]

count = 0
list_of_urls = []


with open(filename, "r") as f:
    for line in f:
        list_of_urls.append(line)
print(list_of_urls)


async def fetch_url(url, sem):
    async with aiohttp.ClientSession() as session:
        async with sem:
            async with session.get(url) as resp:
                global count
                count += 1
                # assert resp.status == 200


async def fetch_batch(urls, sem):
    tasks = [
        asyncio.create_task(fetch_url(url, sem))
        for url in urls
    ]
    await asyncio.gather(*tasks)


t1 = time.time()

sem = asyncio.Semaphore(c)
asyncio.run(fetch_batch(list_of_urls, sem))

t2 = time.time()
print(f"Script works. All {count} urls involved in.", "TIME is", t2 - t1)
