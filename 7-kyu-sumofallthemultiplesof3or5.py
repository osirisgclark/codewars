#7 kyu Sum of all the multiples of 3 or 5


def find(n):
	l = list()
	for x in range(1, n):
		for y in [3,5]:
			if x*y <=n:
				l.append(x*y)

	return sum(set(l))

	#return  sum([x for x in range(1,n+1) if not x%3 or not x%5])
	# return [sum(l.append(x*y)) for x in range(1, n) for y in [3,5] if x*y <=n ]


print(find(5))
print(find(10))
print(find(12))