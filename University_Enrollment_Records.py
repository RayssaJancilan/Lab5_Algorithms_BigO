def generate_datasets():
    """
    Requirement 1: Generate the two sorted enrollment datasets.
    Replace the logic below with your specific variables (SEED_DIGIT, ID_SUM, etc.)
    """
    dataset_a = [8, 23, 26, 35]
    dataset_b = [8, 10, 15, 25, 31]   
    return dataset_a, dataset_b

def consolidate_records(list_a, list_b):
    """
    Consolidate collections and count comparisons.
    """
    consolidated = []
    ptr_a, ptr_b = 0, 0
    comparison_count = 0
    
    while ptr_a < len(list_a) and ptr_b < len(list_b):
        comparison_count += 1
        if list_a[ptr_a] <= list_b[ptr_b]:
            consolidated.append(list_a[ptr_a])
            ptr_a += 1
        else:
            consolidated.append(list_b[ptr_b])
            ptr_b += 1
            
    while ptr_a < len(list_a):
        consolidated.append(list_a[ptr_a])
        ptr_a += 1
        
    while ptr_b < len(list_b):
        consolidated.append(list_b[ptr_b])
        ptr_b += 1
        
    return consolidated, comparison_count

def verify_results(list_a, list_b, consolidated):
    """
    Requirement 4: Verify the final order and number of records.
    """
    expected_count = len(list_a) + len(list_b)
    actual_count = len(consolidated)
    count_valid = (expected_count == actual_count)
    
    is_sorted = all(consolidated[i] <= consolidated[i+1] for i in range(len(consolidated)-1))
    
    return count_valid, is_sorted, expected_count, actual_count

dataset_A, dataset_B = generate_datasets()
final_list, total_comparisons = consolidate_records(dataset_A, dataset_B)
count_ok, order_ok, exp_cnt, act_cnt = verify_results(dataset_A, dataset_B, final_list)

print("===== ASSESSMENT DATA =====")
print(f"Department A dataset: {dataset_A}")
print(f"Department B dataset: {dataset_B}")
print(f"Consolidated dataset: {final_list}")
print(f"Number of records: Before = {len(dataset_A) + len(dataset_B)} | After = {act_cnt}")
print(f"Comparison count:     {total_comparisons}")
print(f"Ordering verification: {'PASSED' if (count_ok and order_ok) else 'FAILED'}")

