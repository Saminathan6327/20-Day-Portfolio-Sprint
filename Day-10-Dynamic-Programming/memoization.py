import time

# ---------------------------------------------------------
# APPROACH 1: Naive Recursion O(2^N)
# ---------------------------------------------------------
def fib_naive(n):
    if n <= 1:
        return n
    # Calculates the same branches over and over
    return fib_naive(n - 1) + fib_naive(n - 2)

# ---------------------------------------------------------
# APPROACH 2: Memoization O(N)
# ---------------------------------------------------------
def fib_memo(n, cache=None):
    if cache is None:
        cache = {}
        
    # 1. Check if we already did the work! (O(1) Hash Map Lookup)
    if n in cache:
        return cache[n]
        
    # 2. Base cases
    if n <= 1:
        return n
        
    # 3. Do the work ONCE and save it to the cache
    cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)
    return cache[n]

if __name__ == "__main__":
    target = 35 # High enough to make naive struggle, low enough not to crash your PC
    
    print("\n========================================================")
    print(f" ALGORITHM BENCHMARK: Fibonacci Sequence (N = {target})")
    print("========================================================")

    # 1. Test Memoized Approach First (So you don't have to wait!)
    print("Starting Memoized DP O(N)...")
    start_time = time.time()
    result_memo = fib_memo(target)
    end_time = time.time()
    memo_duration = end_time - start_time
    print(f"Result: {result_memo}")
    print(f"Time taken: {memo_duration:.6f} seconds")
    print("--------------------------------------------------------")

    # 2. Test Naive Approach
    print("Starting Naive Recursion O(2^N)... (This will take a few seconds)")
    start_time = time.time()
    result_naive = fib_naive(target)
    end_time = time.time()
    naive_duration = end_time - start_time
    print(f"Result: {result_naive}")
    print(f"Time taken: {naive_duration:.6f} seconds")
    print("========================================================")
    
    # 3. Calculate Performance Increase
    if memo_duration > 0:
        speedup = naive_duration / memo_duration
        print(f"🚀 DP Magic: Memoization was {speedup:,.0f}x faster!")