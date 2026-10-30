#!/usr/bin/env python3
"""Module with a coroutine that collects values using async comprehension."""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect ten random numbers using an async comprehension."""
    return [i async for i in async_generator()]
