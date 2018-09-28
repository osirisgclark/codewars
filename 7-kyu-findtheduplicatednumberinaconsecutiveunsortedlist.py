#7 kyu Find The Duplicated Number in a Consecutive Unsorted List
def find_dup(arr):
	for x in sorted(arr):
		if sorted(arr)[x]==sorted(arr)[x-1]:
			return sorted(arr)[x]
	

print(find_dup([3,2,5,1,3,4]))
print(find_dup([5,4,3,2,1,1]), 1)
print(find_dup([1,3,2,5,4,5,7,6]), 5)
print(find_dup( [3, 17, 28, 28, 6, 38, 29, 12, 41, 2, 8, 27, 11, 14, 21, 9, 22, 24, 35, 5, 30, 20, 19, 39, 26, 4, 10, 15, 7, 1, 40, 36, 37, 33, 13, 16, 18, 25, 32, 34, 31, 23]))


	# print(len(arr))
	# for x in range(1, len(arr)):
	# 	if len(re.findall(str(x), str(arr)))>1:
	# 		return x