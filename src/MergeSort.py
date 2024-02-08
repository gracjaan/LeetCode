def merge_sort(arr):
    if len(arr) <= 1:
        return

    # Split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort each half
    merge_sort(left_half)
    merge_sort(right_half)

    # Merge the sorted halves
    merge(arr, left_half, right_half)

def merge(arr, left, right):
    result = []
    left_index, right_index, arr_index = 0, 0, 0

    # Compare elements from the left and right arrays and merge them in sorted order
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            arr[arr_index] = left[left_index]
            left_index += 1
        else:
            arr[arr_index] = right[right_index]
            right_index += 1
        arr_index += 1

    # Append any remaining elements from the left and right arrays
    while left_index < len(left):
        arr[arr_index] = left[left_index]
        left_index += 1
        arr_index += 1

    while right_index < len(right):
        arr[arr_index] = right[right_index]
        right_index += 1
        arr_index += 1

# Example usage:
my_list = [38, 27, 43, 3, 9, 82, 10]
print("Original List:", my_list)
merge_sort(my_list)
print("Sorted List:", my_list)
