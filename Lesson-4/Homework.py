data = {'a': 1, 'b': 3, 'c': 2}
sorted_asc = dict(sorted(data.items(), key=lambda item: item[1]))
sorted_desc = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))
print("Ascending order:", sorted_asc)
print("Descending order:", sorted_desc)


sample_dict = {0: 10, 1: 20}
sample_dict[2] = 30  # Adding a new key-value pair
print("Updated Dictionary:", sample_dict)


dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
# Concatenating dictionaries
new_dict = {**dic1, **dic2, **dic3}
print("Concatenated Dictionary:", new_dict)


n = 5
squares_dict = {x: x * x for x in range(1, n + 1)}
print("Squares Dictionary:", squares_dict)


squares_dict_1_to_15 = {x: x * x for x in range(1, 16)}
print("Squares Dictionary (1 to 15):", squares_dict_1_to_15)


sample_set = {1, 2, 3, 4, 5}
print("Sample Set:", sample_set)


sample_set.add(6)  # Adding a single member
sample_set.update([7, 8])  # Adding multiple members
print("Updated Set:", sample_set)


sample_set.remove(1)  # Removing a single member
sample_set.discard(2)  # Discarding a member (no error if not found)
print("Set after removal:", sample_set)


if 3 in sample_set:
    sample_set.remove(3)  # Remove item if present
print("Set after conditional removal:", sample_set)
