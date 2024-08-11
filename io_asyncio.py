#!/usr/bin/env  python3


import asyncio
import time
import aiohttp


async def download_site(session, url):
    async with session.get(url) as response:
        print("Read {0} from {1}".format(response.content_length, url))


async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    asyncio.get_event_loop().run_until_complete(download_all_sites(sites))
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} sites in {duration} seconds")


# My Notes:

# Unlike threading, which uses multiple threads, asyncio uses a single thread with an event loop that handles multiple tasks concurrently.

# aiohttp is a popular third-party library for making asynchronous HTTP requests in Python. 
# It works well with asyncio to handle HTTP requests in an asynchronous manner.

# ClientSession: A class in aiohttp that represents a session for making requests. 
# It manages and reuses connections, which is more efficient than creating a new connection for each request.


# The output of this script was Downloaded 160 sites in 1.3641283512115479 seconds very fast :)