import os

size = {}

for root, _, files in os.walk('.'):
    for file in files:
        correct_file = os.path.join(root, file)
        memory = 10 ** (len(str(os.stat(correct_file).st_size)))
        size[memory] = size.get(memory, 0) + 1
sorted_tuple = sorted(size.items(), key=lambda x: x[0])
final_dict = dict(sorted_tuple)
print(final_dict)