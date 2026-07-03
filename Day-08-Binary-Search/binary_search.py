import time

# ---------------------------------------------------------
# APPROACH 1: Linear Search O(N)
# ---------------------------------------------------------
def linear_search(arr, target):
    # Checks every single element one by one
    steps = 0
    for i in range(len(arr)):
        steps += 1
        if arr[i] == target:
            return i, steps
    return -1, steps

# ---------------------------------------------------------
# APPROACH 2: Binary Search O(log N)
# ---------------------------------------------------------
def binary_search(arr, target):
    # Divides the search area in half each time
    steps = 0
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        steps += 1
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid, steps
        elif arr[mid] < target:
            left = mid + 1 # Target is in the right half
        else:
            right = mid - 1 # Target is in the left half
            
    return -1, steps

if __name__ == "__main__":
    print("Generating a massive dataset of 10 MILLION sorted records...")
    # Creating a sorted array from 1 to 10,000,000
    dataset = list(range(1, 10000001))
    
    # We deliberately pick a target at the very end to force the worst-case scenario
    target_value = 9999999 

    print("\n========================================================")
    print(" ALGORITHM BENCHMARK: Searching 10,000,000 Records")
    print("========================================================")

    # 1. Test Linear Search
    print("Starting Linear Search O(N)... (Please wait)")
    start_time = time.time()
    index_linear, steps_linear = linear_search(dataset, target_value)
    end_time = time.time()
    linear_duration = end_time - start_time
    print(f"Target found at index: {index_linear}")
    print(f"Total Steps Taken:     {steps_linear:,}")
    print(f"Time taken:            {linear_duration:.5f} seconds")
    print("--------------------------------------------------------")

    # 2. Test Binary Search
    print("Starting Binary Search O(log N)...")
    start_time = time.time()
    index_binary, steps_binary = binary_search(dataset, target_value)
    end_time = time.time()
    binary_duration = end_time - start_time
    print(f"Target found at index: {index_binary}")
    print(f"Total Steps Taken:     {steps_binary:,}")
    print(f"Time taken:            {binary_duration:.5f} seconds")
    print("========================================================")
    
    # 3. Output Efficiency
    if binary_duration > 0:
        speedup = linear_duration / binary_duration
        print(f"🚀 Optimization Result: Binary Search was {speedup:,.0f}x faster!")
        print(f"🧠 Efficiency: It only took {steps_binary} steps vs {steps_linear:,} steps!")