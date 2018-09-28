#7 kyu Sum of Odd Cubed Numbers

import re
def cube_odd(n):
	l = list()
	for x in n:
		if re.match('[+-]?\d+', str(x)):
			if x%2 != 0:
				l.append((x**3))
		else:
			return None
	return sum(l)


print(cube_odd([1, 2, 3, 4]), 28)
print(cube_odd([-3,-2,2,3]), 0)
print(cube_odd(["a",12,9,"z",42]), None)