# 1. Make the list and sort it
my_list = [18, 4, 89, 100, 2, 6, 76]
my_list.sort()
print(my_list)

# 2. Make the dict and print it as key-value
my_dict = {1: 'banana', 2: 'apple', 3: 'mango', 4: 'lemon', 5: 'passion fruit'}
for key, value in my_dict.items():
	print(key, value)

#3. Make a tuple of non-integres and fin min and max
my_tuple = (1.779, 1.8985, 1.5464, 1.7689, 1.98797)
print('Max value is {}'.format(max(my_tuple)))
print('Min value is {}'.format(min(my_tuple)))

#4. make a list and convert it into a string
list_1 = ['Earth', 'Russia', 'Moscow']

string_1 = ' -> '.join(list_1)
print(string_1)

