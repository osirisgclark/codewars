#7 kyu Highest and Lowest

def high_and_low(n):
	# l= list()
	L = sorted(n.split(' '), key=int)
	# l.append(p[0])	
	#l.append(p[-1])
	#return ' '.join(l)
	print(L)
	return ' '.join([sorted(n.split(' '), key=int)[index] for index in [-1,0] ])



print(high_and_low("1 2 3 4 5"),  "5 1")
print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"),  "542 -214")


# n = "1 2 3 4 5"
# p = set(n)
# k = list(n)
# print(k[0], k[-1])