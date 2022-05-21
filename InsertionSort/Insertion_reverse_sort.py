import time

start = time.time()

file_array = "../reverse.txt"

with open(file_array) as f:
    arr = []
    for line in f:
        numbers = int(line)
        arr.append(numbers)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = 0

        while key > arr[j] and j < i:
            j = j + 1

        arr.insert(j, key)
        del arr[i + 1]


# print(arr)
insertion_sort(arr)
# print("Sorted table is: ")
# print(arr)
print("The time used to execute this is given below")
end = time.time()
print(end - start)
