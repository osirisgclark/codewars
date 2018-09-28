# 6 kyu-Are they the "same"?
def comp(a, b):
	from math import sqrt
	if a== None or b== None:
		return False
	elif a == [] and b ==[]:
		return True
	elif len(a)!= len(b):
		return False
	else:
		for x in a:
			if x**2 in b:
				continue
			else:
				return False
		for x in b:
			if sqrt(x) in a:
				continue
			else:
				return False
		return True



print(comp([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 361, 25921, 361, 20736, 361]))
print(comp([121, 144, 19, 161, 19, 144, 19, 11],[132, 14641, 20736, 361, 25921, 361, 20736, 361]))
print(comp([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
))
print(comp([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 36100, 25921, 361, 20736, 361]))
print(comp([], []))
print(comp([], [1]))
print(comp(None, None))