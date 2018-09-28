#7 kyu The Hidden Word
def word(n):
	l = list()
	a = {'0':"o", '1':"b", '2':"l", '3':"i", '4':"e", '5':"t", '6':"a", '7':"d", '8':"n", '9':"m"}
	# a = {0:"o", 1:"b", 2:"l", 3:"i", 4:"e", 5:"t", 6:"a", 7:"d", 8:"n", 9:"m"}
	for letter in list(str(n)):
		if letter in a:
			l.append(a[letter])
	return ''.join(l)
	#return ''.join( trans[char] for char in str(num) )

    



print(word(100), [2, 3, 5, 7])
print(word(999), [2, 3, 5, 7, 11, 13, 17, 19, 23])
print(word(28), [2, 3, 5, 7, 11, 13, 17, 19, 23])
print(word(-1), [])



# return {("o":0), ("b":1), ("l":2), ("i":3), ("e": 4), ("t":5), ("a": 6), ("d":7), ("n":8), ("m":9)}  