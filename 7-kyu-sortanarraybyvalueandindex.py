7 kyu Sort an array by value and index
def sort_by_value_and_index(arr):
	l = list()
	n = 1
	p = list()
	for x in arr:
		l.append(x*n)
		n+=1
	k = l[:len(arr)]
	return [x for (y,x) in sorted(zip(k, arr), key=lambda pair: pair[0])] 

print(sort_by_value_and_index([ 1, 2, 3, 4, 5 ]), [ 1, 2, 3, 4, 5 ])
print(sort_by_value_and_index([ 23, 2, 3, 4, 5 ]), [ 2, 3, 4, 23, 5 ])
print(sort_by_value_and_index([ 26, 2, 3, 4, 5 ]), [ 2, 3, 4, 5, 26 ])
print(sort_by_value_and_index([ 9, 5, 1, 4, 3 ]), [ 1, 9, 5, 3, 4 ])

 
# print(sort_by_value_and_index([23, 2, 3, 4, 5]), [ 2, 3, 4, 23, 5 ])
# Input: 23, 2, 3, 4, 5
# Product of value and index:
# 23 => 23 * 1 = 23  -> Output-Pos 4
#  2 =>  2 * 2 = 4   -> Output-Pos 1
#  3 =>  3 * 3 = 9   -> Output-Pos 2
#  4 =>  4 * 4 = 16  -> Output-Pos 3
#  5 =>  5 * 5 = 25  -> Output-Pos 5

# Output: 2, 3, 4, 23, 5