

#8 kyu Sum without highest and lowest number

def sum_array(arr):
	if not isinstance(arr, (list, tuple)):
		arr = [arr]
        return 0
      
    else:
    	return sum(arr)- (max(arr)+min(arr)) if len(arr)>2 else 0 


print(sum_array(None)) #, 0))
print(sum_array([])) #, 0))
print(sum_array(3)) #, 0))
print(sum_array(-3)) #, 0))
print(sum_array([3, 5])) #, 0))
print(sum_array([-3, -5])) #, 0))


print(sum_array([6, 2, 1, 8, 10])) #, 16))
print(sum_array([6, 0, 1, 10, 10])) #, 17))
print(sum_array([-6, -20, -1, -10, -12])) #, -28))
print(sum_array([-6, 20, -1, 10, -12])) #, 3))




# from collections import Counter
# a = [ -6, 20, -1, 10, -12]
# b = Counter(sorted(a))  #Counter({1: 2, 11: 1, 2: 1, 3: 1})
# print(b)
# w = sorted(a)



