import random
file_array = "../sorted.txt"

i = 1
n = 1

with open(file_array, "w") as fout:

    while i <= 500000:
        fout.write(str(n) + "\n")
        n = n + random.randint(0, 5)
        i = i + 1

print("Elements:")
print(i-1)