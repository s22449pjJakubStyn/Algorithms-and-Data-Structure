import time

file_array = "../reverse.txt"

with open(file_array) as f:
    arr = []
    for line in f:
        numbers = int(line)
        arr.append(numbers)


def merge_sort(A):
    if len(A) > 1:
        mid = len(A) // 2

        left = A[:mid]
        right = A[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            A[k] = right[j]
            j += 1
            k += 1


arr.sort(reverse=True)
# print(arr)
start = time.time()
merge_sort(arr)
# print("Sorted table is: ")
# print(arr)
print("The time used to execute this is given below")
end = time.time()
print(end - start)
