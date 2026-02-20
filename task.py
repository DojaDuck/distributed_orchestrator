from enum import Enum
from dataclasses import dataclass, field
from typing import Callable, Any
import time
import uuid
class TaskStatus(Enum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    RETRYING = "RETRYING"

@dataclass(order=True)
class Task:
    priority: int
    function: Callable[..., Any] = field(compare=False)
    args: tuple = field(default=(), compare=False)
    kwargs: dict = field(default_factory=dict, compare=False)
    id: str = field(default_factory=lambda: str(uuid.uuid4()), compare=False)
    status: TaskStatus = field(default=TaskStatus.PENDING, compare=False)
    retries: int = field(default=0, compare=False)
    max_retries: int = field(default=3, compare=False)
    result: Any = field(default=None, compare=False)
    created_at: float = field(default_factory=time.time, compare=False)
    started_at: float = field(default=None, compare=False)
    completed_at: float = field(default=None, compare=False)

    def mark_running(self):
        self.status = TaskStatus.RUNNING
        self.started_at = time.time()

    def mark_success(self, result: Any):
        self.status = TaskStatus.SUCCESS
        self.result = result
        self.completed_at = time.time()

    def mark_failed(self):
        self.retries += 1
        if self.retries > self.max_retries:
            self.status = TaskStatus.FAILED
            self.completed_at = time.time()
        else:
            self.status = TaskStatus.RETRYING
