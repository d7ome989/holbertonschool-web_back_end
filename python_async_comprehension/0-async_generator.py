#!/usr/bin/env python3
"""Module that defines an asynchronous generator yielding random numbers."""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Asynchronously yield a random number between 0 and 10, ten times."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
