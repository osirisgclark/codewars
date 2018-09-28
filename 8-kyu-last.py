#8 kyu Last

def last(*args):
	if len(args)==1:
		try:
			return args[0][-1]
		except:
			return args[0]
	else:
		return args[-1]
	
print(last([1,2,3,4,5]), 5)
print(last("abcde"), "e")
print(last(1, "b", 3, "d", 5), 5)
print(last(1))