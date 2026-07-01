import time

# ---------------------------------------------------------
# APPROACH 1: The Naive Method (Nested Loops) - O(N^2)
# ---------------------------------------------------------
def naive_target_sum(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return (arr[i], arr[j])
    return None

# ---------------------------------------------------------
# APPROACH 2: The Two-Pointer Method - O(N)
# ---------------------------------------------------------
def optimized_target_sum(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return (arr[left], arr[right])
        elif current_sum < target:
            left += 1  # We need a bigger sum, move left pointer right
        else:
            right -= 1 # We need a smaller sum, move right pointer left
            
    return None

if __name__ == "__main__":
    print("Generating a massive dataset of 20,000 numbers...")
    # Creating a sorted array from 1 to 20,000
    dataset = list(range(1, 20001))
    target_value = 39999 # This forces the algorithms to search the very end

    print("\n========================================================")
    print(" ALGORITHM BENCHMARK: Two-Sum Problem")
    print("========================================================")

    # 1. Test Naive Approach
    print("Starting Naive Approach O(N^2)... (This might take a moment)")
    start_time = time.time()
    result_naive = naive_target_sum(dataset, target_value)
    end_time = time.time()
    naive_duration = end_time - start_time
    print(f"Result: {result_naive}")
    print(f"Time taken: {naive_duration:.5f} seconds")
    print("--------------------------------------------------------")

    # 2. Test Optimized Approach
    print("Starting Two-Pointer Approach O(N)...")
    start_time = time.time()
    result_optimized = optimized_target_sum(dataset, target_value)
    end_time = time.time()
    optimized_duration = end_time - start_time
    print(f"Result: {result_optimized}")
    print(f"Time taken: {optimized_duration:.5f} seconds")
    print("========================================================")
    
    # 3. Calculate Performance Increase
    if optimized_duration > 0:
        speedup = naive_duration / optimized_duration
        print(f"🚀 Optimization Result: The Two-Pointer method was {speedup:,.0f}x faster!")