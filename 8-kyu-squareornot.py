#8 kyu To square(root) or not to square(root)

from math import sqrt
def square_or_square_root(arr):
	l=list()
	for x in arr:
		p= sqrt(x)
		if p.is_integer()== True:
			l.append(int(p))
		else:
			l.append(x**2)
	return l

print(square_or_square_root([4,3,9,7,2,1]))#== [2, 9, 3, 49, 4, 1]
print(square_or_square_root([100, 101, 5, 5, 1, 1]))#== [10, 10201, 25, 25, 1, 1]
print(square_or_square_root([1, 2, 3, 4, 5, 6]))#== [1, 4, 9, 2, 25, 36]