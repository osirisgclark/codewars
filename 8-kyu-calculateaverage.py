#8 kyu Calculate average
#import statistics as s
def find_average(array):
	return float(sum(array)) / max(len(array), 1)
	#return s.mean(array) if len(array) >1 else array

print(find_average([ 1, 2, 3 ]))
print(find_average([]))
print(find_average([486.4945501986162]))