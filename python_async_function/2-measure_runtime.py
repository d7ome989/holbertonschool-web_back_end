#!/usr/bin/env python3
"""
This module defines a function that measures the average execution time
per coroutine of the wait_n routine.
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time of wait_n and return the time per call.

    Args:
        n: The number of times wait_random is spawned.
        max_delay: The maximum number of seconds each coroutine can wait.

    Returns:
        The total elapsed time divided by n, as a float.
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start
    return total_time / n
