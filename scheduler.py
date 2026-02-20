import heapq
import asyncio
from typing import List
from worker import Worker
from task import Task


class Scheduler:
    def __init__(self, workers: List[Worker]):
        self.workers = workers
        self.task_queue = []

    def add_task(self, task: Task):
        heapq.heappush(self.task_queue, task)

    def get_available_worker(self):
        for worker in self.workers:
            if worker.is_alive and worker.current_task is None:
                return worker
        return None

    async def run(self):
        while True:
            if self.task_queue:
                worker = self.get_available_worker()
                if worker:
                    task = heapq.heappop(self.task_queue)
                    asyncio.create_task(worker.process(task))

            await asyncio.sleep(0.1)
