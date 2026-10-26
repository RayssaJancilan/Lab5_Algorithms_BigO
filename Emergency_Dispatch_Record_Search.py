def calculate_artist_sum(artist_name):
    return sum(ord(char) - 64 for char in artist_name.upper() if 'A' <= char <= 'Z')

def generate_dataset(student_id, last_name, favorite_artist):
    seed_digit = int(str(student_id)[-1])
    id_sum = sum(int(digit) for digit in str(student_id) if digit.isdigit())
    name_length = len(last_name.replace(" ", ""))
    artist_length = len(favorite_artist.replace(" ", ""))
    artist_sum = calculate_artist_sum(favorite_artist)
    
    base = id_sum + name_length
    step = (seed_digit if seed_digit > 1 else 3)
    size = 15  # Array size
    original_dataset = [base + i * step for i in range(size)]
    
    rotation_point = seed_digit % size if seed_digit > 0 else 4
    rotated_dataset = original_dataset[rotation_point:] + original_dataset[:rotation_point]
    
    target_incident = original_dataset[(id_sum + artist_sum) % size]
    
    return original_dataset, rotated_dataset, target_incident

def linear_search(arr, target):
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons
    return -1, comparisons

def rotated_binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    comparisons = 0
    
    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        
        if arr[mid] == target:
            return mid, comparisons
            
        if arr[low] <= arr[mid]:
            comparisons += 1
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            comparisons += 1
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
                
    return -1, comparisons



STUDENT_ID = "TUPM-26-3228"    
LAST_NAME = "Jancilan"
FAVORITE_ARTIST = "Rico Blanco"

orig, rotated, target = generate_dataset(STUDENT_ID, LAST_NAME, FAVORITE_ARTIST)
lin_pos, lin_comp = linear_search(rotated, target)
bin_pos, bin_comp = rotated_binary_search(rotated, target)

print("=== ASSESSMENT DATA ===")
print(f"Original Dataset:  {orig}")
print(f"Rotated Dataset:   {rotated}")
print(f"Target Incident:   {target}\n")

print("=== SEARCH RESULTS ===")
if bin_pos != -1:
    print(f"Target found at index: {bin_pos} (Rotated Dataset)")
else:
    print("Target not found in the dataset.")

print("\n=== COMPARISON COUNTS ===")
print(f"Linear Search Comparisons: {lin_comp}")
print(f"Modified Binary Search Comparisons: {bin_comp}")
