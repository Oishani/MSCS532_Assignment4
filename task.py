class Task:
    """
    Represents a single task in the priority queue.
    Stores information such as task ID, priority, arrival time, deadline, and optional description.
    Comparison is based on priority for use in a min-heap.
    """
    def __init__(self, task_id, priority, arrival_time=None, deadline=None, description=None):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline
        self.description = description

    def __lt__(self, other):
        # For min-heap: lower value means higher priority
        return self.priority < other.priority

    def __eq__(self, other):
        return (self.task_id == other.task_id)

    def __repr__(self):
        return (f"Task(id={self.task_id}, priority={self.priority}, "
                f"arrival={self.arrival_time}, deadline={self.deadline})")
