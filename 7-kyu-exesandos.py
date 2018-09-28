#7 kyu Exes and Ohs
def XO(n):
	l = list()
	m= list()
	for an in n:
		if an== 'o' or an== 'O' :
			l.append(an)
		elif an == 'x' or an== 'X':
			m.append(an)
		else:
			continue
	return True if len(l)==len(m) else False

# Best:
# return s.lower().count('x') == s.lower().count('o')

print(XO("ooxx"), True)
print(XO("xooxx"), False)
print(XO("ooxXm"), False)
print(XO("zpzpzpp"), True)
print(XO("zzoo"), False)