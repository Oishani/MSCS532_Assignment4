# Increase recursion limit for large input sizes in recursive sorts
import sys
sys.setrecursionlimit(10000)

import random
import time

from heapsort import heapsort
from mergesort import mergesort
from quicksort import quicksort

def generate_input(size, distribution):
    if distribution == 'random':
        return [random.randint(0, size) for _ in range(size)]
    elif distribution == 'sorted':
        return list(range(size))
    elif distribution == 'reverse':
        return list(range(size, 0, -1))
    elif distribution == 'repeated':
        base = [random.choice(range(10)) for _ in range(size // 10)]
        return [random.choice(base) for _ in range(size)]
    else:
        raise ValueError(f"Unknown distribution: {distribution}")

def benchmark(sort_fn, arr):
    arr_copy = arr.copy()
    start = time.perf_counter()
    sort_fn(arr_copy)
    end = time.perf_counter()
    assert arr_copy == sorted(arr), "Sort failed!"
    return end - start

def main():
    sizes = [1000, 5000, 10000, 50000]
    distributions = ['random', 'sorted', 'reverse', 'repeated']
    algorithms = [
        ('Heapsort', heapsort),
        ('Quicksort', quicksort),
        ('Merge Sort', mergesort),
    ]
    results = []

    for alg_name, alg_fn in algorithms:
        for dist in distributions:
            for size in sizes:
                arr = generate_input(size, dist)
                timings = []
                error = None
                for _ in range(3):
                    try:
                        t = benchmark(alg_fn, arr)
                        timings.append(t)
                    except RecursionError:
                        error = "RecursionError"
                        break
                    except AssertionError:
                        error = "SortFailed"
                        break
                    except Exception as e:
                        error = f"Error:{type(e).__name__}"
                        break
                if error:
                    avg_time = error
                else:
                    avg_time = sum(timings) / len(timings)
                results.append((alg_name, dist, size, avg_time))
                print(f"{alg_name:10} | {dist:8} | {size:6} | {avg_time}")

    print("\nSummary Table:\nAlgorithm\tDistribution\t1000\t5000\t10000\t50000")
    for alg_name, alg_fn in algorithms:
        for dist in distributions:
            row = [alg_name, dist]
            for size in sizes:
                entry = next((r for r in results if r[0] == alg_name and r[1] == dist and r[2] == size), None)
                val = entry[3]
                if isinstance(val, float):
                    row.append(f"{val:.5f}")
                else:
                    row.append(str(val))
            print('\t'.join(row))

if __name__ == "__main__":
    main()
