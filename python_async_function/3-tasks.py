#!/usr/bin/env python3
"""
This module defines a regular function that wraps the wait_random
coroutine in an asyncio Task.
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio Task that runs wait_random with the given max_delay.

    Args:
        max_delay: The maximum number of seconds the coroutine can wait.

    Returns:
        An asyncio.Task object wrapping the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
