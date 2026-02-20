# distributed_orchestrator
Distributed Task Orchestrator

A fault-tolerant, load-aware task scheduling system built in Python.
This project simulates core concepts used in distributed systems, including dynamic load balancing, worker health monitoring, and priority-based task allocation.

**Overview**

This system models a simplified distributed task execution environment where:
Tasks are dynamically assigned to workers
Workers report health and performance metrics
The scheduler reallocates tasks based on load and availability
Failures are detected and handled automatically
The goal of this project is to explore real-world distributed system behaviours such as resilience, scalability, and performance optimisation.

**Architecture**

The system consists of:
Scheduler – Central orchestrator responsible for task allocation
Workers – Asynchronous task processors with simulated load
Priority Queue – Handles task importance and execution order
Health Monitor – Detects worker failures and reassigns tasks
Metrics Engine – Tracks performance and system state
The implementation uses Python’s asyncio framework to simulate concurrent execution.

**Key Features**

Asynchronous task execution
Priority-based scheduling
Dynamic load-aware allocation
Worker health checks
Automatic failure recovery
Performance monitoring and metrics reporting

**Technologies Used**

Python 3.10+ asyncio
heapq (priority queue)
logging
dataclasses

**Installation**

1. Clone the repository:

git clone https://github.com/yourusername/distributed-task-orchestrator.git
cd distributed-task-orchestrator

2. Create a virtual environment:

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

3. Install dependencies (if any):

pip install -r requirements.txt

Running the Project
python main.py

**You will see:**

Task scheduling logs
Worker allocation updates
Load distribution metrics
Failure simulation handling

**Example Output**
[Scheduler] Assigned Task 12 to Worker 2
[Worker 2] Processing task with priority 1
[Monitor] Worker 3 unresponsive  reallocating tasks
[Metrics] Average load: 63%

**Future Improvements**

Horizontal scaling simulation
Persistent state storage
REST API interface
Docker containerisation
Integration with message brokers (e.g. RabbitMQ)

**Why This Project?**

This project was built to deepen understanding of:
Distributed system design principles
Asynchronous programming patterns
Load balancing strategies
Fault tolerance mechanisms
