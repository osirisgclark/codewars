#7 kyu-Unique string characters
def solve(a, b):
	l1 = list(a)
	l2 = list(b)
	l = list()
	p = [l.append(x) for x in l1 if x not in l2 ]
	q = [l.append(x) for x in l2 if x not in l1 ]
	return ''.join(l)

print((solve("xxx","xzca"),"zca"))