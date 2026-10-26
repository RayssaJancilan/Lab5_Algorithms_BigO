import time
import random

class Order:
    def __init__(self, order_id, amount):
        self.order_id = order_id
        self.amount = amount  # Sorting metric: Total transaction value

    def __repr__(self):
        return f"Order({self.order_id}, ${self.amount})"



def bubble_sort(arr):
    n = len(arr)
    comparisons = 0
    movements = 0
    arr_copy = list(arr)  
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr_copy[j].amount > arr_copy[j+1].amount:
                arr_copy[j], arr_copy[j+1] = arr_copy[j+1], arr_copy[j]
                movements += 3
                swapped = True
        if not swapped: 
            break
            
    return arr_copy, comparisons, movements


def selection_sort(arr):
    n = len(arr)
    comparisons = 0
    movements = 0
    arr_copy = list(arr)
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr_copy[j].amount < arr_copy[min_idx].amount:
                min_idx = j
                
        if min_idx != i:
            arr_copy[i], arr_copy[min_idx] = arr_copy[min_idx], arr_copy[i]
            movements += 3
            
    return arr_copy, comparisons, movements


def insertion_sort(arr):
    n = len(arr)
    comparisons = 0
    movements = 0
    arr_copy = list(arr)
    
    for i in range(1, n):
        key = arr_copy[i]
        movements += 1  
        j = i - 1
        
        while j >= 0:
            comparisons += 1
            if arr_copy[j].amount > key.amount:
                arr_copy[j + 1] = arr_copy[j]
                movements += 1
                j -= 1
            else:
                break
        arr_copy[j + 1] = key
        movements += 1
        
    return arr_copy, comparisons, movements


num_orders = 500
random.seed(23)  
random_dataset = [Order(f"ORD{i:03d}", round(random.uniform(5.00, 1500.00), 2)) for i in range(num_orders)]

datasets = {
    "Sorted (Best Case)": sorted(random_dataset, key=lambda x: x.amount),
    "Reverse-Sorted (Worst Case)": sorted(random_dataset, key=lambda x: x.amount, reverse=True),
    "Random (Average Case)": random_dataset
}

algorithms = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort
}

print(f"| {'Dataset State':<30} | {'Algorithm':<15} | {'Comparisons':<12} | {'Movements':<12} | {'Time (ms)':<10} | {'Verified':<8} |")
print("|" + "-"*32 + "|" + "-"*17 + "|" + "-"*14 + "|" + "-"*14 + "|" + "-"*12 + "|" + "-"*10 + "|")

for dataset_name, test_data in datasets.items():
    for algo_name, algo_function in algorithms.items():
        start_time = time.perf_counter()
        sorted_output, total_comps, total_moves = algo_function(test_data)
        end_time = time.perf_counter()
        
        execution_time_ms = (end_time - start_time) * 1000
        
        is_valid = all(sorted_output[k].amount <= sorted_output[k+1].amount for k in range(len(sorted_output) - 1))
        
        print(f"| {dataset_name:<30} | {algo_name:<15} | {total_comps:<12} | {total_moves:<12} | {execution_time_ms:<10.3f} | {str(is_valid):<8} |")
