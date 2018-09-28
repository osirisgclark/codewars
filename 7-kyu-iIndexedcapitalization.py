def capitalize(s,ind):
	l = list()
	for x in range(len(s)):
		if x in ind:
			l.append(s[x].upper())
		else:
			l.append(s[x])
	return ''.join(l)

print(capitalize("abcdef",[1, 2, 5, 100]), "aBCdeF")
print(capitalize("abcdef",[1, 3, 6, 100]), "aBCdeF")
print(capitalize("abcdef",[0, 2, 5,100]), "aBCdeF")

# a= "abcdef"
# print([x for x in range(len(a))])


