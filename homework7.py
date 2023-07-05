# Write a lambda function called add that takes two numbers as arguments and returns their sum.


add = lambda a,b: a+b
a = 15
b = 39
result = add(a,b)
print(f"Sum of {a} and {b} is {result}.")



# Implement zip function



num = [1,2,3]
letter = ['a','b','c']
zipped = zip(num,letter)
print(type(zipped))
zipped_list = list(zipped)
print(zipped_list)



# Implement filter function


def check_odd(num):
	return num % 2 != 0
num = [15,64,23,74,6,19,26]
odd_num_iterator = filter(check_odd,num)
odd_num = list(odd_num_iterator)
print(odd_num)


# Implement enumerate function


cake = ['egg','sugar','flour']
enumerate_prime = enumerate(cake)
print(list(enumerate_prime))



# Implement map function


num1 = [1,2,3]
num2 = [4,5,6]
result = map(lambda x, y: x + y,num1,num2)
print(list(result))



# Write a function called counter that returns a closure. The closure should keep track of the number of times it has been called and return that count.



def counter():
	count = 0
	def decrement():
		nonlocal count
		count = count + 1
		return count
	return decrement
decrement = counter()
print(decrement())
print(decrement())
print(decrement())




