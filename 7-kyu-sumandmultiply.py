
# 7 kyu Sum and Multiply
def sum_and_multiply(sum, multiply):
	l=list()
	for x in range(1001):
		for y in range(1001):
			if x+y==sum and x*y==multiply:
				l.append(x)
				l.append(y)
				return l
	# return [l.append((x, y)) for x, y in range(0,1000) if (x+y==n and x*y==m) ]
	# return [(x, y for x in range(0, 1000) for y in range(0, 1000) if (x+y==n and x*y==m) ]


print(sum_and_multiply(12, 32), '[4,8]')
print(sum_and_multiply(0, 0), '[0, 0]')
print(sum_and_multiply(2, 1), '[1, 1]')
print(sum_and_multiply(200, 8458), None)