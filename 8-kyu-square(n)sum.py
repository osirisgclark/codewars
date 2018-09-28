#8 kyu Square(n) Sum
def square_sum(n):
	l = list()
	for x in n:
		l.append(x**2)
	return sum(l)

print(square_sum([1, 2, 2]), 9)


#Best:
# def square_sum(numbers):
#     return sum(x ** 2 for x in numbers)