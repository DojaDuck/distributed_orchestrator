import asyncio
import random
from config import TASK_PROCESSING_MIN, TASK_PROCESSING_MAX, WORKER_FAILURE_PROBABILITY


class Worker:
    def __init__(self, worker_id: int):
        self.id = worker_id
        self.current_task = None
        self.is_alive = True
        self.total_processed = 0

    async def process(self, task):
        if not self.is_alive:
            return

        self.current_task = task
        print(f"[Worker {self.id}] Processing {task}")

        await asyncio.sleep(random.uniform(TASK_PROCESSING_MIN, TASK_PROCESSING_MAX))

        # Simulate failure
        if random.random() < WORKER_FAILURE_PROBABILITY:
            self.is_alive = False
            print(f"[Worker {self.id}] FAILURE occurred")
            return

        self.total_processed += 1
        print(f"[Worker {self.id}] Completed {task}")
        self.current_task = None

    def revive(self):
        self.is_alive = True
        print(f"[Worker {self.id}] Revived")
