from priority_queue import PriorityQueue
from task import Task

def scheduler_simulation(logfile='simulation_results.txt'):
    # Open the results file for writing
    with open(logfile, 'w') as f:
        def log(msg):
            print(msg)
            f.write(msg + '\n')

        # Simulated list of arriving tasks (task_id, priority, arrival_time, deadline)
        task_list = [
            Task('T1', 3, arrival_time=0, deadline=10, description='System Update'),
            Task('T2', 2, arrival_time=1, deadline=8, description='User Report'),
            Task('T3', 1, arrival_time=2, deadline=5, description='Urgent Bug Fix'),
            Task('T4', 5, arrival_time=3, deadline=12, description='Background Backup'),
            Task('T5', 4, arrival_time=4, deadline=9, description='Security Patch'),
        ]
        
        pq = PriorityQueue()
        current_time = 0
        tasks_to_arrive = list(task_list)
        executed_tasks = []

        while tasks_to_arrive or not pq.is_empty():
            # Insert tasks that arrive at this time
            for task in list(tasks_to_arrive):
                if task.arrival_time == current_time:
                    log(f"[Time {current_time}] Task Arrived: {task}")
                    pq.insert(task)
                    tasks_to_arrive.remove(task)

            # Dynamic example: lower the priority of T4 if it waits too long
            if current_time == 5:
                try:
                    pq.decrease_key('T4', 0)  # Make T4 urgent
                    log(f"[Time {current_time}] Priority of Task T4 decreased to 0")
                except Exception:
                    pass

            # Execute one task if available
            if not pq.is_empty():
                next_task = pq.extract_min()
                log(f"[Time {current_time}] Executing: {next_task}")
                executed_tasks.append((current_time, next_task))
            else:
                log(f"[Time {current_time}] Idle: No tasks to execute")

            current_time += 1

        log("\nExecution order:")
        for exec_time, task in executed_tasks:
            log(f"Time {exec_time}: Executed {task}")

if __name__ == "__main__":
    scheduler_simulation()
