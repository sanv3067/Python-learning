tuples = [(1, 2), (3, 4, 5), (6, 7, 8, 9), (10,)]
largest = tuples[0]
for t in tuples:
    if len(t) > len(largest):
        largest = t
print("Tuple with more elements:", largest)
print("Number of elements:", len(largest))