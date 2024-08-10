# Speeding Up an I/O-Bound Python Program

This repository explores methods for improving the performance of I/O-bound Python programs. By leveraging concurrency and parallelism, you can significantly reduce the time it takes to complete I/O-bound tasks.

## Methods Covered

The following methods are demonstrated:

- **Threading:** Utilizes multiple threads to handle I/O-bound tasks concurrently.
- **Asyncio:** Provides an asynchronous programming model, ideal for managing multiple I/O-bound operations without blocking.
- **Multiprocessing:** Employs multiple processes to parallelize tasks, taking full advantage of multiple CPU cores.

## Learn More

These examples are adapted from the [Real Python guide on concurrency](https://realpython.com/python-concurrency/). Visit the link for a more in-depth explanation of these techniques.
Also check out the second module of [Troubleshooting & Debugging Techniques on Coursera](https://www.coursera.org/learn/troubleshooting-debugging-techniques/home/module/2)