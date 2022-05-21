import time

file_array = "../sorted.txt"

with open(file_array) as f:
    arr = []
    for line in f:
        numbers = int(line)
        arr.append(numbers)

start = time.time()


def partition(A, p, r):
    x = A[r]

    i = p - 1
    for j in range(p, r):
        if A[j] < x:
            i += 1
            change = A[i]
            A[i] = A[j]
            A[j] = change
    change = A[i + 1]
    A[i + 1] = A[r]
    A[r] = change
    return i + 1


def _quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        _quicksort(A, p, q - 1)
        _quicksort(A, q + 1, r)
    return A


def quicksort(A):
    return _quicksort(A, 0, len(A) - 1)


# print(arr)
quicksort(arr)
n = len(arr)
# print ("Sorted table is: ")
# print(arr)
print("The time used to execute this is given below")
end = time.time()
print(end - start)
