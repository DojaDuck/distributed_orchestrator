
'''Central configuration file for the Distributed Task Orchestration System.
All tunable runtime parameters live here.'''

# Worker configuration
MAX_WORKERS = 4
WORKER_RETRY_LIMIT = 3
WORKER_TIMEOUT_SECONDS = 5

# Scheduler configuration
TASK_QUEUE_MAX_SIZE = 100
PRIORITY_LEVELS = 5

# Monitoring configuration
HEALTH_CHECK_INTERVAL = 2  # seconds
FAILURE_THRESHOLD = 3      # consecutive failures before restart

# Metrics configuration
ENABLE_METRICS = True
METRICS_REPORT_INTERVAL = 5  # seconds

# Simulation parameters
SIMULATED_TASK_DURATION_RANGE = (1, 3)
SIMULATED_FAILURE_RATE = 0.1  # 10% failure probability
