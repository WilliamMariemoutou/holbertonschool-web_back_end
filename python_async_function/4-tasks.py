#!/usr/bin/env python3
"""ake the code from wait_n and
alter it into a new function task_wait_n.
The code is nearly identical to wait_n except
task_wait_random is being called."""


import asyncio


async def task_wait_n(n: int, max_delay: int) -> list[float]:
    """
    Run task_wait_random n times and return the results
    in ascending order of completion
    """
    delays = []
    tasks = []

    # Create n tasks
    for _ in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)

    # Collect results as tasks finish
    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)

    return delays
