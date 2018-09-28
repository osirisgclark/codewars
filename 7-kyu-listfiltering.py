#7 kyu-List Filtering
def filter_list(s):
	l= list()
	for x in s:
		if x in range(100000):
			l.append(x)
	return l


print(filter_list([1,2,'a','b'])) # == [1,2])
print(filter_list([1,'a','b',0,15]))# == [1,0,15]
print(filter_list([1,2,'aasf','1','123',123])) # == [1,2,123]

# Best:

# 1. return [x for x in l if type(x) is not str]
# 2. return [x for x in l if type(x) is int]