import time

file_array = "../reverse.txt"

with open(file_array) as f:
    arr = []
    for line in f:
        numbers = int(line)
        arr.append(numbers)

start = time.time()


def heapify(A, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and A[i] < A[l]:
        largest = l

    if r < n and A[largest] < A[r]:
        largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]

        heapify(A, n, largest)


def heapSort(A):
    n = len(A)

    for i in range(n // 2 - 1, -1, -1):
        heapify(A, n, i)

    for i in range(n - 1, 0, -1):
        A[i], A[0] = A[0], A[i]
        heapify(A, i, 0)


# print(arr)
heapSort(arr)
n = len(arr)
# print ("Sorted table is: ")
# print(arr)
print("The time used to execute this is given below")
end = time.time()
print(end - start)
