# MSCS-532 Assignment 4: Heap Data Structures: Implementation, Analysis, and Applications

This repository contains Python implementations, empirical benchmarks, a scheduler simulation, and an in-depth report for key heap-based data structures and algorithms, including:

- **Heapsort (with benchmarking and analysis)**
- **Priority Queue (min-heap) implementation and simulation of scheduling applications**

All code, benchmarks, and the final report are included for clarity and reproducibility.

---

## Repository Structure

MSCS532_ASSIGNMENT3/
- `benchmark_results.txt`: Output/results from sorting benchmark
- `benchmark_sorting.py`: Heapsort, Quicksort, Mergesort benchmarking script
- `heapsort.py`: Heapsort implementation
- `mergesort.py`: Mergesort implementation
- `quicksort.py`: Quicksort implementation
- `priority_queue.py`: Min-heap-based priority queue implementation
- `task.py`: Task class for use with the priority queue
- `scheduler_simulation.py`: Task scheduling simulation using the priority queue
- `simulation_results.txt`: Output/results from the scheduler simulation
- `test_priority_queue.py`: Script to test priority queue operations
- `test_priority_queue_results.txt`: Output/results from priority queue tests
- `MSCS-532_ Assignment 4_ Heap Data Structures_ Implementation, Analysis, and Applications.pdf` # Final report
- `README.md`: This file

---

## Instructions: Running the Code

#### Setup
1. **Python Version**  
   Ensure you have Python 3.7 or higher installed. You can check your version with:
   ```bash
   python3 --version
   ```
2. **Dependencies**
All scripts use only Python standard library modules. No external installations are required.
3. **Clone the Repository**
   Clone this repository to your local machine:
   ```bash
   git clone https://github.com/Oishani/MSCS532_Assignment4.git
   cd MSCS532_Assignment4
   ```

### 1. Heapsort, Quicksort, and Mergesort Benchmarking

Run the benchmark script to compare Heapsort, Quicksort, and Mergesort across various input sizes and distributions:
```bash
python3 benchmark_sorting.py
```
Output will display the timing results for each algorithm on random, sorted, reverse-sorted, and repeated arrays.
A summary results table is also saved in `benchmark_results.txt`.

You can also test individual sorting algorithms directly:
```bash
python3 heapsort.py
python3 mergesort.py
python3 quicksort.py
```

### 2. Priority Queue and Scheduler Simulation

Test the Priority Queue implementation:
```bash
python3 test_priority_queue.py
```
Results will be saved in `test_priority_queue_results.txt`.

Run the Scheduler Simulation:
```bash
python3 scheduler_simulation.py
```
This simulates a dynamic scheduling environment where tasks with different priorities and arrival times are managed and executed. The results, including task arrivals, dynamic priority updates, execution order, and idle periods, will be saved to `simulation_results.txt`.

## Summary of Findings

### Part 1: Heapsort Implementation and Analysis

- **Heapsort** is implemented as an in-place, robust, and efficient algorithm suitable for all input types.
- Theoretical analysis confirms O(n log n) time for all cases (worst, average, and best) and O(1) auxiliary space.
- **Empirical benchmarks** show Quicksort is fastest for most random/ordered data, but Heapsort and Merge Sort are more robust for pathological cases (e.g., repeated elements), confirming their suitability for applications needing consistent performance.

### Part 2: Priority Queue Implementation and Applications

- A **min-heap-based priority queue** efficiently supports task scheduling with dynamic priority updates and robust edge case handling.
- All major operations (`insert`, `extract_min`, `increase`/`decrease_key`, `is_empty`) run in O(log n) time.
- The scheduler simulation models real-world task arrival, dynamic priority updates, and execution, showcasing the practical use of the queue in dynamic systems such as operating systems or job queues.

### Report
The full analysis, theoretical explanation, benchmarking tables, and discussion of the scheduler simulation are included in
`MSCS-532_ Assignment 4_ Heap Data Structures_ Implementation, Analysis, and Applications.pdf`.