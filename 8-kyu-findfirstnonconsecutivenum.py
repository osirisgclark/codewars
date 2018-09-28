#8 kyu Find the first non-consecutive number
def data(n): 
	for x in n:
		if x == n[0]+int(n.index(x)):
			continue
		else:
			return x



print(data([1,2,3,4,6,7,8]), 12)