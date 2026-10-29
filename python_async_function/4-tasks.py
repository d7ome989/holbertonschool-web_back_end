#!/usr/bin/env python3
"""
This module defines an asynchronous routine that spawns the
task_wait_random function multiple times and collects the delays.
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times with the given max_delay.

    Args:
        n: The number of tasks to spawn.
        max_delay: The maximum number of seconds each task can wait.

    Returns:
        The list of all the delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays: List[float] = []
    for completed in asyncio.as_completed(tasks):
        delays.append(await completed)
    return delays
