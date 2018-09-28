#8 kyu They say that only the name is long enough to attract attention. They also said that only a simple Kata will have someone to solve it. This is a sadly story #1: Are they opposite?

def is_opposite(s1,s2):
	l = list()
	for x in n:
		if x.islower():
			l.append(x.upper())
		else:
			l.append(x.lower())
	return ''.join(l)==m and m!="" and n!=""

# Best
# def is_opposite(s1,s2):
#     return s1!="" and s1.swapcase() == s2
    
#      return False if not(s1 or s2) else s1.swapcase() == s2


print(isOpposite("ab","AB"),True)
print(isOpposite("aB","Ab"),True)
print(isOpposite("aBcd","AbCD"),True)
print(isOpposite("AB","Ab"), False)
print(isOpposite("",""), False)


