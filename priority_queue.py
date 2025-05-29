import heapq

class PriorityQueue:
    """
    A min-heap priority queue for Task objects.
    Supports insertion, extraction, priority update, and empty-check operations.
    """
    def __init__(self):
        self.heap = []
        self.entry_finder = {}  # Map from task_id to [priority, count, task]
        self.counter = 0  # Unique sequence count to break ties

    def insert(self, task):
        """
        Inserts a new task into the heap. O(log n) time.
        """
        entry = [task.priority, self.counter, task]
        self.entry_finder[task.task_id] = entry
        heapq.heappush(self.heap, entry)
        self.counter += 1

    def extract_min(self):
        """
        Removes and returns the task with the lowest priority value. O(log n) time.
        Raises IndexError if the queue is empty.
        """
        while self.heap:
            priority, count, task = heapq.heappop(self.heap)
            if task.task_id in self.entry_finder:
                del self.entry_finder[task.task_id]
                return task
        raise IndexError("extract_min from empty priority queue")

    def decrease_key(self, task_id, new_priority):
        """
        Decreases the priority of an existing task and updates its position. O(log n) time.
        """
        if task_id in self.entry_finder:
            entry = self.entry_finder[task_id]
            task = entry[2]
            if new_priority < task.priority:
                # Mark the old entry as removed
                del self.entry_finder[task_id]
                # Insert new entry with updated priority
                task.priority = new_priority
                self.insert(task)

    def increase_key(self, task_id, new_priority):
        """
        Increases the priority of an existing task and updates its position. O(log n) time.
        """
        if task_id in self.entry_finder:
            entry = self.entry_finder[task_id]
            task = entry[2]
            if new_priority > task.priority:
                del self.entry_finder[task_id]
                task.priority = new_priority
                self.insert(task)

    def is_empty(self):
        """
        Checks if the priority queue is empty. O(1) time.
        """
        return not bool(self.entry_finder)

    def __len__(self):
        return len(self.entry_finder)
