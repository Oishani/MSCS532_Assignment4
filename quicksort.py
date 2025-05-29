import random

def quicksort(arr):
    """
    In-place Quicksort with random pivot.
    """
    def _quicksort(a, low, high):
        if low < high:
            pivot_index = random.randint(low, high)
            a[high], a[pivot_index] = a[pivot_index], a[high]
            pivot = a[high]
            i = low
            for j in range(low, high):
                if a[j] < pivot:
                    a[i], a[j] = a[j], a[i]
                    i += 1
            a[i], a[high] = a[high], a[i]
            _quicksort(a, low, i - 1)
            _quicksort(a, i + 1, high)
    _quicksort(arr, 0, len(arr) - 1)
