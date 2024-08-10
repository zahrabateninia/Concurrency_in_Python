#!/usr/bin/env  python3

import concurrent.futures
import requests
import threading
import time

# store data unique to each thread. This prevents race conditions and ensures that each thread has its own separate data.
thread_local = threading.local()


def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


def download_site(url):
    session = get_session()
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


def download_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_site, sites)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")


# My Notes: 

# the Executor’s going to control how and when each of the threads in the pool will run. It will execute the request in the pool.
# Because the operating system is in control of when your task gets interrupted and another task starts, 
# any data that is shared between the threads needs to be protected, or thread-safe.
# Unfortunately requests.Session() is not thread-safe.

# There are several strategies for making data accesses thread-safe depending on what the data is and how you’re using it. 
# One of them is to use thread-safe data structures like Queue from Python’s queue module.

# These objects use low-level primitives like threading.Lock to ensure that only one thread can access a block of code or a bit of memory at the same time. 
# You are using this strategy indirectly by way of the ThreadPoolExecutor object.

# Another strategy to use here is thread local storage. threading.local() creates an object that looks like a global
# but is specific to each individual thread. In this example, this is done with thread_local and get_session()


# my output was Downloaded 160 in 6.36435341835022 seconds much faster than non concurrent approach