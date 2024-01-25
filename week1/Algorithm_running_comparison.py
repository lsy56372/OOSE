import numpy as np
import time

# Selection sort function
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Bubble sort function
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

if __name__ == '__main__':
    # Generate random data
    data = np.random.random((10000))

    # Copy data for later sorting
    data_copy_selection = data.copy()
    data_copy_bubble = data.copy()

    # Use NumPy's quicksort and record the time
    start_time = time.time()
    sorted_data_np = np.sort(data)
    end_time = time.time()
    print("NumPy quicksort time:", end_time - start_time, "seconds")

    # Use selection sort and record the time
    start_time = time.time()
    selection_sort(data_copy_selection)
    end_time = time.time()
    print("Selection sort time:", end_time - start_time, "seconds")

    # Use bubble sort and record the time
    start_time = time.time()
    bubble_sort(data_copy_bubble)
    end_time = time.time()
    print("Bubble sort time:", end_time - start_time, "seconds")
