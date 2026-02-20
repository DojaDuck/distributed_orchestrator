import asyncio
from config import METRICS_INTERVAL
class Metrics:
    def __init__(self, workers):
        self.workers = workers
    async def report(self):
        while True:
            total_processed = sum(w.total_processed for w in self.workers)
            alive_workers = sum(1 for w in self.workers if w.is_alive)

            print("\n[Metrics]")
            print(f"Total processed: {total_processed}")
            print(f"Active workers: {alive_workers}")
            print("-" * 30)
            await asyncio.sleep(METRICS_INTERVAL)
