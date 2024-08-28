
def bubble_sort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(n-1-i):
            if array[j] > array[j+1]:
                # Swap array[j] and array[j+1]
                array[j], array[j+1] = array[j+1], array[j]

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)

print("Sorted array is:", arr)
