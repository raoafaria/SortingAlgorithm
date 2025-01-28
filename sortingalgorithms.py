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


# Benchmark a specific sorting algorithm
def benchmark_algorithm(algorithm_name, sorting_function):
    input_sizes = [5, 10, 20, 50, 100, 500, 1000, 5000, 10000]
    times = []

    for size in input_sizes:
        test_array = [random.randint(1, 10000) for _ in range(size)]
        start_time = time.time()
        sorting_function(test_array)
        end_time = time.time()
        times.append(end_time - start_time)

    # Plot the result
    plt.figure(figsize=(10, 6))
    plt.plot(input_sizes, times, label=algorithm_name, marker='o')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Time (seconds)')
    plt.title(f'{algorithm_name} Runtime Performance')
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


# Main Menu
def main_menu():
    while True:
        print("Sorting Algorithms Benchmark")
        print("1. Benchmark Insertion Sort")
        print("2. Benchmark Selection Sort")
        print("3. Benchmark Bubble Sort")
        print("4. Display System Information")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nBenchmarking Insertion Sort...\n")
            benchmark_algorithm("Insertion Sort", insertion_sort)
        elif choice == "2":
            print("\nBenchmarking Selection Sort...\n")
            benchmark_algorithm("Selection Sort", selection_sort)
        elif choice == "3":
            print("\nBenchmarking Bubble Sort...\n")
            benchmark_algorithm("Bubble Sort", bubble_sort)
        elif choice == "4":
            print("\nDisplaying System Information...\n")
            display_system_info()
        elif choice == "5":
            print("\nExiting. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.\n")


if __name__ == "__main__":
    main_menu()
