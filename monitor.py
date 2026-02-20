import asyncio
from config import HEALTH_CHECK_INTERVAL
class Monitor:
    def __init__(self, workers):
        self.workers = workers
    async def monitor_workers(self):
        while True:
            for worker in self.workers:
                if not worker.is_alive:
                    print(f"[Monitor] Worker {worker.id} is down. Reviving...")
                    worker.revive()
            await asyncio.sleep(HEALTH_CHECK_INTERVAL)
