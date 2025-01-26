import random
import time

def quicksort(arr, pivot_strategy):
    if len(arr) <= 1:
        return arr
    if pivot_strategy == 'first':
        pivot = arr[0]
    elif pivot_strategy == 'last':
        pivot = arr[-1]
    elif pivot_strategy == 'middle':
        pivot = arr[len(arr) // 2]
    else:
        raise ValueError("Invalid pivot strategy")
    
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left, pivot_strategy) + middle + quicksort(right, pivot_strategy)

def generate_data(size, data_type):
    if data_type == 'random':
        return [random.randint(0, 100000) for _ in range(size)]
    elif data_type == 'sorted':
        return list(range(size))
    elif data_type == 'reverse_sorted':
        return list(range(size, 0, -1))

size = 10000
data_type = 'random'
pivot_strategy = 'first'

data = generate_data(size, data_type)
start_time = time.time()
sorted_data = quicksort(data, pivot_strategy)
end_time = time.time()
print(f"Execution time: {end_time - start_time} seconds")