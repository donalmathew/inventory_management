import itertools

def min_sum_permutation(arr1, arr2):
    min_sum = float('inf')  # Initialize to infinity
    best_permutation = None
    
    # Generate all permutations of arr2
    for perm in itertools.permutations(arr2):
        # Calculate the sum of products
        current_sum = sum(a * b for a, b in zip(arr1, perm))
        print(perm)
        # Update minimum sum and best permutation if needed
        if current_sum < min_sum:
            min_sum = current_sum
            best_permutation = perm
            
    return min_sum, list(best_permutation)

# Example usage
arr1 = [1, 2, 3]
arr2 = [6,5,4,4,2,2]

min_sum, best_perm = min_sum_permutation(arr1, arr2)
print("Minimum Sum:", arr2)
print("Best Permutation of arr2:", best_perm)
