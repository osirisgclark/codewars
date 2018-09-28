# 8 kyu N-th Power


import math
def index(m, n):
	try:
		return int(math.pow(m[n], n))
	except:
		return -1

print(index( [1, 2, 3, 4], 2), 9)
print (index( [1, 2, 3], 3), -1)
print(index([1, 3, 10, 100],3),1000000)
