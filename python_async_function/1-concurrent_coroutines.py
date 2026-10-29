#!/usr/bin/env python3
"""
This module defines an asynchronous routine that spawns the wait_random
coroutine multiple times concurrently and collects the delays.
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the given max_delay.

    Args:
        n: The number of times to spawn wait_random.
        max_delay: The maximum number of seconds each coroutine can wait.

    Returns:
        The list of all the delays in ascending order.
    """
    coroutines = [wait_random(max_delay) for _ in range(n)]
    delays: List[float] = []
    for completed in asyncio.as_completed(coroutines):
        delays.append(await completed)
    return delays
