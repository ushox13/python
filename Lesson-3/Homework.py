fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits[2]) 


list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
print(concatenated_list) 


numbers = [10, 20, 30, 40, 50]
first_element = numbers[0]
middle_element = numbers[len(numbers) // 2]
last_element = numbers[-1]
extracted_elements = [first_element, middle_element, last_element]
print(extracted_elements) 


movies_list = ["Inception", "The Matrix", "Interstellar", "The Shawshank Redemption", "Pulp Fiction"]
movies_tuple = tuple(movies_list)
print(movies_tuple) 


cities = ["New York", "London", "Paris", "Tokyo", "Berlin"]
is_paris_in_list = "Paris" in cities
print(is_paris_in_list) 


numbers = [1, 2, 3, 4, 5]
duplicated_numbers = numbers * 2
print(duplicated_numbers) 


numbers = [1, 2, 3, 4, 5]
numbers[0], numbers[-1] = numbers[-1], numbers[0]
print(numbers)


numbers_tuple = tuple(range(1, 11))
sliced_tuple = numbers_tuple[3:8]
print(sliced_tuple) 


colors = ["red", "blue", "green", "blue", "yellow"]
blue_count = colors.count("blue")
print(blue_count) 


animals_tuple = ("cat", "dog", "lion", "tiger", "bear")
lion_index = animals_tuple.index("lion")
print(lion_index)  


tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
merged_tuple = tuple1 + tuple2
print(merged_tuple) 


list_example = [1, 2, 3, 4, 5]
tuple_example = (1, 2, 3, 4, 5)
list_length = len(list_example)
tuple_length = len(tuple_example)
print(f"Length of the list: {list_length}")  
print(f"Length of the tuple: {tuple_length}")  


numbers_tuple = (10, 20, 30, 40, 50)
numbers_list = list(numbers_tuple)
print(numbers_list)


numbers_tuple = (5, 10, 15, 20, 25)
max_value = max(numbers_tuple)
min_value = min(numbers_tuple)
print(f"Maximum value: {max_value}")  
print(f"Minimum value: {min_value}")  


words_tuple = ("apple", "banana", "cherry", "date", "elderberry")
reversed_tuple = words_tuple[::-1]
print(reversed_tuple) 
