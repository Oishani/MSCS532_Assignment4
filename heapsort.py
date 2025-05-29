def heapsort(arr):
    """
    Sorts an array in ascending order using the Heapsort algorithm.
    The function first builds a max-heap, then repeatedly extracts the maximum element
    to sort the array in-place.

    Args:
        arr (list): List of comparable elements to be sorted.

    Returns:
        None: The input list is sorted in-place.
    """
    def heapify(arr, n, i):
        """
        Ensures the subtree rooted at index i is a max-heap, assuming subtrees are already max-heaps.

        Args:
            arr (list): List representation of the heap.
            n (int): Size of the heap.
            i (int): Root index of the subtree.
        """
        largest = i        # Initialize largest as root
        left = 2 * i + 1   # left = 2*i + 1
        right = 2 * i + 2  # right = 2*i + 2

        # Check if left child exists and is greater than root
        if left < n and arr[left] > arr[largest]:
            largest = left

        # Check if right child exists and is greater than current largest
        if right < n and arr[right] > arr[largest]:
            largest = right

        # If largest is not root, swap and continue heapifying
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)

    # Build a max-heap (rearrange array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one from heap
    for i in range(n - 1, 0, -1):
        # Swap the root (max value) with the last item
        arr[i], arr[0] = arr[0], arr[i]
        # Call heapify on the reduced heap
        heapify(arr, i, 0)

# Example usage:
if __name__ == "__main__":
    test_cases = [
        [],                         # Empty array
        [42],                      # Single element
        [3, 2, 1, 4, 5, 6, 7],     # Unsorted array
        [7, 7, 7, 7],              # Duplicate elements
        [1, 2, 3, 4, 5],           # Already sorted
        [5, 4, 3, 2, 1],           # Reverse sorted
    ]
    for arr in test_cases:
        arr_copy = arr.copy()
        heapsort(arr_copy)
        print(f"Original: {arr} -> Sorted: {arr_copy}")
