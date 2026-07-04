import time
import random

def setup_databases(size):
    print(f"Generating database of {size:,} employee records...")
    
    # We will store the data in two different structures to compare them
    list_database = []
    hash_map_database = {}
    
    for i in range(size):
        employee_id = f"EMP-{i}"
        employee_data = {"name": f"User_{i}", "department": "Engineering"}
        
        # 1. Appending to a standard list
        list_database.append((employee_id, employee_data))
        
        # 2. Assigning to a Hash Map (Dictionary)
        hash_map_database[employee_id] = employee_data
        
    return list_database, hash_map_database

def search_list(data_list, target_id):
    # O(N) Linear Search - Must check every item until found
    for emp_id, data in data_list:
        if emp_id == target_id:
            return data
    return None

def search_hash_map(data_map, target_id):
    # O(1) Constant Time - Instant mathematical lookup
    return data_map.get(target_id)

if __name__ == "__main__":
    # Create 5 Million Records
    db_size = 5000000
    list_db, dict_db = setup_databases(db_size)
    
    # Pick a target ID at the very end of the database
    target = f"EMP-{db_size - 1}"

    print("\n========================================================")
    print(" ALGORITHM BENCHMARK: List O(N) vs Hash Map O(1)")
    print("========================================================")

    # 1. Test Standard List Search
    print("Searching standard List O(N)... (Please wait)")
    start_time = time.time()
    result_list = search_list(list_db, target)
    end_time = time.time()
    list_duration = end_time - start_time
    print(f"Record found! Time taken: {list_duration:.5f} seconds")
    print("--------------------------------------------------------")

    # 2. Test Hash Map Lookup
    print("Searching Hash Map O(1)...")
    start_time = time.time()
    result_dict = search_hash_map(dict_db, target)
    end_time = time.time()
    dict_duration = end_time - start_time
    print(f"Record found! Time taken: {dict_duration:.5f} seconds")
    print("========================================================")
    
    # 3. Calculate Performance Increase
    if dict_duration > 0:
        speedup = list_duration / dict_duration
        print(f"🚀 Optimization Result: The Hash Map was {speedup:,.0f}x faster!")