from priority_queue import PriorityQueue
from task import Task

if __name__ == "__main__":
    pq = PriorityQueue()
    pq.insert(Task('A', 3))
    pq.insert(Task('B', 2))
    pq.insert(Task('C', 5))

    print("Extracted:", pq.extract_min())  # Should be Task B
    pq.decrease_key('C', 1)
    print("Extracted:", pq.extract_min())  # Should be Task C
    print("Is empty?", pq.is_empty())      # False
    print("Extracted:", pq.extract_min())  # Should be Task A
    print("Is empty?", pq.is_empty())      # True
