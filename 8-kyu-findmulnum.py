

# 8 kyu Find Multiples of a Number
def find_difference(integer,limit):
	l = list()
	p = int(limit/integer)
	for x in range(1, p+1):
		l.append(x*integer)
	return l


print(find_difference(5, 25)) #==[5, 10, 15, 20, 25]
print(find_difference(1, 2)) #==[1, 2]

