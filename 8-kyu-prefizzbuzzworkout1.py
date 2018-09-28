#  8 kyu Pre-FizzBuzz Workout #1
def fizzbuzz(n):
	l= list()
	for x in range(n):
		l.append(x+1)
	return l

print(fizzbuzz(1), [1])
print(fizzbuzz(2), [1,2])
print(fizzbuzz(3), [1,2,3])
print(fizzbuzz(4), [1,2,3,4])
print(fizzbuzz(5), [1,2,3,4,5])

# Best:
# return list(range(1, n+1))
