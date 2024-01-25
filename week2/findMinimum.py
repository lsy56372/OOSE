import numpy as np
from main_max_min_test import getMin
from Algorithm_running_comparison import selection_sort
import time

if __name__ == '__main__':
    # Generate random data
    data = np.random.random(10000)

    # Copy data for later sorting
    data_copy_selection = data.copy()

    # Use selection sort and record the time
    start_time = time.time()
    selection_sort(data_copy_selection)
    end_time = time.time()

    # Find the minimum value using getMin function
    min_value = getMin(data_copy_selection)

    print("Selection sort time:", end_time - start_time, "seconds")
    print("The minimum value is:", min_value)
