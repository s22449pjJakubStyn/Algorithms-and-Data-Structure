import random
file_array = "../reverse.txt"

i = 1

with open(file_array, "w") as fout:

    while i <= 500000:
        fout.write(str(random.randint(1, 1000)) + "\n")
        i = i + 1

print("Elements:")
print(i-1)