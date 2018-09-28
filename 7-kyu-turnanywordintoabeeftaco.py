#7 kyu Turn any word into a beef taco
def tacofy(word):
	n = ['shell']
	l = list()
	K = {'a':'beef','A':'beef', 'e':'beef','E':'beef', 'i':'beef', 'I':'beef', 'o':'beef','O':'beef', 'u':'beef', 'U':'beef', 't': 'tomato','T': 'tomato', 'l': 'lettuce', 'L': 'lettuce', 'c': 'cheese', 'C': 'cheese', 'g': 'guacamole', 's': 'salsa', 'G': 'guacamole', 'S': 'salsa'}
	for x in word:
		if x in K:
			l.append(K[x])
	return n + l + n



print(tacofy(""),['shell', 'shell'])
print(tacofy("aAl"), ['shell', 'beef', 'shell'])
print(tacofy("ggg"), ['shell', 'guacamole', 'guacamole', 'guacamole', 'shell'])
print(tacofy("ogl"),['shell', 'beef', 'guacamole', 'lettuce', 'shell'])
print(tacofy("ydjkpwqrzto"), ['shell', 'tomato', 'beef', 'shell'])