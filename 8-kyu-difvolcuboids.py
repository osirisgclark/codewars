#8 kyu Difference of Volumes of Cuboids
def find_difference(a, b):
	l = list()
	for x in a,b:
		l.append(x[0]*x[1]*x[2])
	return abs(l[0]-l[1])


print(find_difference([2, 2, 3], [5, 4, 1])) #==8
print(find_difference([3, 2, 5], [1, 4, 4]))#==14
print(find_difference([9, 7, 2], [5, 2, 2])) #==106
print(find_difference([11, 2, 5], [1, 10, 8]))#==30
print(find_difference([4, 4, 7], [3, 9, 3]))#==31
print(find_difference([15, 20, 25], [10, 30, 25])) #==0

