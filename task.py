import uuid
from dataclasses import dataclass, field
from time import time


@dataclass(order=True)
class Task:
    priority: int
    created_at: float = field(init=False, compare=True)
    id: str = field(default_factory=lambda: str(uuid.uuid4()), compare=False)

    def __post_init__(self):
        self.created_at = time()

    def __repr__(self):
        return f"<Task id={self.id[:8]} priority={self.priority}>"
