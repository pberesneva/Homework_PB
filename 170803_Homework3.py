# Easy Tasks
#1.1 Error raise
def user_number():
	try:
	    number=int(input('Enter any integral number:  '))
	    if number%2 == 0:
	        raise ValueError('The number is even and divided by two!')
	    elif number<0:
	        raise TypeError('The number is less than zero!')
	    elif number>10:
	        raise IndexError('The number is more than ten!')
	except Exception as e:
	    print(e)

user_number()

#1.2 Error raise
import random
random_list = random.sample(range(1, 1000), 23)
print(random_list)

def get_item_by_index():
	user_index =int(input("Please enter the index: "))
	try:
	    print('The item from our list is:', random_list[user_index])           
	except ValueError as e:
	    print('ValueError', e)
	except TypeError as e:
	    print('TypeError', e)
	except IndexError as e:
	    print('IndexError', e)

get_item_by_index()


#2.1 Functions
def function1(x, y):
    if x > 0 and y > 0:
        return x + y
    elif x < 0 and y < 0:
        return x - y
    else:
        return 0
# test
function1(2, 9)
function1(-1, -23)
function1(-123, 9)

#2.2 Function
def function2(a, b, c):
    list2 = [a, b, c]
    list2.sort(reverse = True)
    print('The first 2 max numbers from the list are {}'.format(list2[0:2]))
# test
function2(2, 9, 0)

#2.3 Functions
def function3(flag,*args):
    odd_list = []
    even_list = []

    for arg in args:
        if arg % 2 == 0:
            even_list.append(arg)
        else:
            odd_list.append(arg)

    if flag:
        return odd_list
    else:
        return even_list

print(function3(True, *[1,2,3,4,5,6,7,8,9,10,11,0]))
print(function3(False, *[1,2,3,4,5,6,7,8,9,10,11,0]))

#2.3 Alternative v
def function3b(b, random_list):
    if b:
        return filter(lambda x: x % 2 != 0, random_list)
    else:
        return filter(lambda x: x % 2 == 0, random_list)

print(function3b(True, [1,2,3,4,5,6,7,8,9,10,11,0]))
print(function3b(False, [1,2,3,4,5,6,7,8,9,10,11,0]))

#3.1 Variables
def function_min_max(*args):
	list1 = [arg for arg in args]
	list1.sort()
	print('Max value is {}'.format(list1[0]), 'Min value is {}'.format(list1[-1]))
function_min_max(123, 122, 3, 6,7 ,9,0, -2, 645)

def function_min_max2(*args):
    print(max(args),min(args))
some_numbers(1,2,3,4,5,6,7,8,9,0,-12,-1)

#3.2 Variabels

def function_case(any_string, case = True):
	if case:
		return any_string.upper()
	else:
		return any_string.lower()
print(function_case('Life, freedom and pursuit of happiness'))

#3.3 Variables

def function_glue(*kwargs, glue= ':'):
	for kwarg in kwargs:
		if len(kwarg) > 3:
			+=kwarg + glue
print(function_glue('the', 'test', 'is', 'fake'))



def function_glue(*kwargs, glue = ':'):
	for kwarg in kwargs:
		if len(kwarg) > 3:
			+=kwarg + glue
print(function_glue('the', 'test', 'is', 'fake'))
