#!/usr/bin/env python3
"""write a measure_runtime coroutine
that will execute async_comprehension
four times in parallel using asyncio.gather."""

import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime of running async_comprehension
    four times in parallel
    """
    start_time = time.time()

    tasks = [
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    ]

    await asyncio.gather(*tasks)

    end_time = time.time()

    return end_time - start_time
