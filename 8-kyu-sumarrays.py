# 8 kyu Sum Arrays

def sum_array(a):
	return 0 if a ==[] else sum(a)


print(sum_array([]), 0)
print(sum_array([1, 2, 3]), 6)
print(sum_array([1.1, 2.2, 3.3]), 6.6)
print(sum_array([4, 5, 6]), 15)
print(sum_array(range(101)), 5050)