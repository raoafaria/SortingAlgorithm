import time
import matplotlib.pyplot as plt
import random
import psutil
import platform

# Insertion Sort Implementation
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Selection Sort Implementation
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Bubble Sort Implementation
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Function to benchmark sorting algorithms
def benchmark_sorting_algorithms():
    input_sizes = [5, 10, 20, 50, 100, 500, 1000, 5000, 10000]
    insertion_times = []
    selection_times = []
    bubble_times = []

    for size in input_sizes:
        test_array = [random.randint(1, 10000) for _ in range(size)]

        # Time Insertion Sort
        start_time = time.time()
        insertion_sort(test_array.copy())
        end_time = time.time()
        insertion_times.append(end_time - start_time)

        # Time Selection Sort
        start_time = time.time()
        selection_sort(test_array.copy())
        end_time = time.time()
        selection_times.append(end_time - start_time)

        # Time Bubble Sort
        start_time = time.time()
        bubble_sort(test_array.copy())
        end_time = time.time()
        bubble_times.append(end_time - start_time)

    # Plot results
    plt.figure(figsize=(10, 6))
    plt.plot(input_sizes, insertion_times, label='Insertion Sort', marker='o')
    plt.plot(input_sizes, selection_times, label='Selection Sort', marker='o')
    plt.plot(input_sizes, bubble_times, label='Bubble Sort', marker='o')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Time (seconds)')
    plt.title('Sorting Algorithm Runtime Comparison')
    plt.legend()
    plt.grid()
    plt.show()

# Function to display system information
def display_system_info():
    print("System Information:")
    print(f"Operating System: {platform.system()} {platform.release()}")
    print(f"Processor: {platform.processor()}")
    print(f"Number of Cores: {psutil.cpu_count(logical=False)}")
    print(f"Total Logical Processors: {psutil.cpu_count(logical=True)}")
    print(f"Total RAM: {round(psutil.virtual_memory().total / (1024 * 1024 * 1024), 2)} GB")
    print("\n")

if __name__ == "__main__":
    display_system_info()
    benchmark_sorting_algorithms()