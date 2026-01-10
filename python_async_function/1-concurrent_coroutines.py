#!/usr/bin/env python3
"""Function for concurrent coroutines"""


import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times and returns the list of delays
    in ascending order without using sort().
    """
    delays = []
    tasks = []

    # Create n tasks
    for i in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    # Get results as tasks finish
    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)

    return delays
