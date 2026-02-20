import asyncio
import random
from scheduler import Scheduler
from worker import Worker
from task import Task
from monitor import Monitor
from metrics import Metrics
from config import MAX_WORKERS, MAX_TASKS


async def generate_tasks(scheduler):
    for _ in range(MAX_TASKS):
        task = Task(priority=random.randint(1, 5))
        scheduler.add_task(task)
        await asyncio.sleep(random.uniform(0.2, 1.0))


async def main():
    workers = [Worker(i) for i in range(MAX_WORKERS)]

    scheduler = Scheduler(workers)
    monitor = Monitor(workers)
    metrics = Metrics(workers)

    await asyncio.gather(
        scheduler.run(),
        monitor.monitor_workers(),
        metrics.report(),
        generate_tasks(scheduler),
    )


if __name__ == "__main__":
    asyncio.run(main())
