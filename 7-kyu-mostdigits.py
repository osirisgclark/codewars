#7 kyu Most digits
def find_longest(arr):
	l = list()
	m= max(arr)
	le= len(str(m))
	for x in arr:
		if len(str(x))== le:
			l.append(x)
	return  l,  l[0]

print(find_longest([8000, 30, 400, 500, 20, 90000]), [4, 5])

# Best:
# max(arr, key=lambda x: len(str(x)))