#6 kyu Find the unique number
from collections import Counter


def find_uniq(arr):
    return [item for item, count in Counter(arr).items() if count == 1]


print(find_uniq([1, 1, 1, 2, 1, 1 ]))#, === 2)
print(find_uniq([0, 0, 0.55, 0, 0 ]))#, === 0.55)

# def find_uniq(arr):
# 	for n in arr:
# 		a= arr.count(n)
# 		if a==1:
# 			return n

# from itertools import groupby
# def find_uniq(n):
# 	m= sorted(list(set(sorted(n))))
# 	k=[len(list(group)) for key, group in groupby(sorted(n))]
# 	for x in k:
# 		if x ==1:
# 			print(k[x])
# 			return m[k[x]]




