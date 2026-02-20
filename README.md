# Distributed Task Orchestrator

A fault-tolerant task orchestration engine written in Python.
Designed to simulate core principles of distributed systems including priority scheduling, retry policies, health monitoring, and performance metrics collection.

This project models real-world orchestration challenges such as:

* Asynchronous worker execution
* Load-aware scheduling
* Failure recovery with retry logic
* Task lifecycle state management
* Operational metrics and observability
* Separation of concerns across system components

## Architecture Overview

The system is modular and designed around clear responsibility boundaries (should be :/):

```
.
├── main.py        
├── task.py        
├── scheduler.py   
├── worker.py      
├── monitor.py     
├── metrics.py     
├── config.py     
└── README.md
```

### Core Design Principles

* **Separation of concerns**
* **Fault tolerance via retry policies**
* **Priority-based scheduling**
* **State-driven task lifecycle**
* **Operational observability**

## Task Lifecycle

Each task progresses through defined states:

```
PENDING → RUNNING → SUCCESS
                   ↘
                    RETRYING → FAILED
```

Retry behaviour is configurable via `max_retries`.


## Features

* Priority queue scheduling
* UUID-based task tracking
* Retry logic with bounded attempts
* Execution timestamps (created, started, completed)
* Metrics collection for throughput & failure rate
* Modular architecture for extensibility

## Installation


git clone https://github.com/yourusername/distributed-task-orchestrator.git
cd distributed-task-orchestrator
python3 main.py

No external dependencies required (standard library only).

## Example Usage

Example task definition:

```python
def sample_job(x):
    return x * 2
```

Task submission:

```python
from task import Task

task = Task(priority=1, function=sample_job, args=(5,))
scheduler.add_task(task)
```

## Observability

The `metrics.py` module tracks:

* Total tasks processed
* Success rate
* Failure rate
* Average execution time

Designed to simulate production-style monitoring hooks.

## Why This Project Exists

This project was built to explore:

* Distributed system design fundamentals
* Execution flow orchestration
* Resilient task handling patterns
* Clean modular Python architecture

It demonstrates applied systems thinking rather than simple script automation.


## Potential Extensions

* Persistent task storage (Redis / PostgreSQL)
* Horizontal worker scaling
* REST API interface (FastAPI)
* Docker containerisation
* Distributed queue backend
* Prometheus-compatible metrics endpoint

## Technologies Used

* Python 3.10+
* asyncio
* dataclasses
* priority queues
* enum-based state modelling

## Author

Built as an exploration of distributed system concepts and orchestration design patterns.
