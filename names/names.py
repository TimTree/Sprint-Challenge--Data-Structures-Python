import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure
#print(names_1)


b = BinarySearchTree(names_1[0])
c = BinarySearchTree(names_2[0])

for i in range(1, len(names_1)):
    b.insert(names_1[i])

for i in range(1, len(names_2)):
    c.insert(names_2[i])

duplicates = [name_1 for name_1 in names_1 if b.contains(name_1) and c.contains(name_1)]


# Replace the nested for loops below with your improvements
#for name_1 in names_1:
#    for name_2 in names_2:
#        if name_1 == name_2:
#            duplicates.append(name_1)
#            continue
#duplicates = [name_1 for name_1 in names_1 for name_2 in names_2 if name_1 == name_2]

# Runtime complexity of old code is O(n^2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
