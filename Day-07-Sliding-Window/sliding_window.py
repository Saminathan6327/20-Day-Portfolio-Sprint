import time
import random

# ---------------------------------------------------------
# APPROACH 1: Brute Force O(N * K)
# ---------------------------------------------------------
def brute_force_max_sub_array(arr, k):
    max_sum = float('-inf')
    n = len(arr)
    
    # Check every possible subarray of size k
    for i in range(n - k + 1):
        current_sum = 0
        for j in range(i, i + k):
            current_sum += arr[j]
        max_sum = max(max_sum, current_sum)
        
    return max_sum

# ---------------------------------------------------------
# APPROACH 2: Optimized Sliding Window O(N)
# ---------------------------------------------------------
def sliding_window_max_sub_array(arr, k):
    n = len(arr)
    if n < k:
        return 0
        
    # Compute the sum of the very first window
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide the window across the remaining elements
    for i in range(n - k):
        # Subtract the element leaving on the left, add the element entering on the right
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)
        
    return max_sum

if __name__ == "__main__":
    print("Generating a massive synthetic data array of 50,000 values...")
    random.seed(42) # Ensure reproducible results
    dataset = [random.randint(1, 100) for _ in range(50000)]
    window_size = 5000 # Large window size to emphasize computational overhead

    print("\n========================================================")
    print(" ALGORITHM BENCHMARK: Maximum Subarray Sum (K = 5,000)")
    print("========================================================")

    # 1. Test Brute Force
    print("Running Brute Force O(N * K)...")
    start_time = time.time()
    result_brute = brute_force_max_sub_array(dataset, window_size)
    end_time = time.time()
    brute_duration = end_time - start_time
    print(f"Max Sum Found: {result_brute}")
    print(f"Time taken:    {brute_duration:.5f} seconds")
    print("--------------------------------------------------------")

    # 2. Test Sliding Window
    print("Running Sliding Window O(N)...")
    start_time = time.time()
    result_window = sliding_window_max_sub_array(dataset, window_size)
    end_time = time.time()
    window_duration = end_time - start_time
    print(f"Max Sum Found: {result_window}")
    print(f"Time taken:    {window_duration:.5f} seconds")
    print("========================================================")
    
    # 3. Efficiency Gain Output
    if window_duration > 0:
        speedup = brute_duration / window_duration
        print(f"🚀 Optimization Result: The Sliding Window was {speedup:,.1f}x faster!")