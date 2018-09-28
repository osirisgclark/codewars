#7 kyu Simple Fun #246: Array Center
from statistics import mean
def array_center(arr):
	l=list()
	for x in arr:
		if abs(x-mean(arr)) < min(arr):
			l.append(x)
	return l

print(array_center([8, 3, 4, 5, 2, 8]), [4, 5])

print(array_center([1, 3, 2, 1]), [1, 2, 1])



# Best:
 # - return [i for i in lst if abs(i - sum(lst)*1.0/len(lst)) < min(lst)]
 
 # - return [i for i in arr if abs(i - avg) < min(arr)]
# def average(values):
# return float(sum(arr)) / len(arr)