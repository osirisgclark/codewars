# 8 kyu Find the position!

def position(alphabet):
	if alphabet in "abcdefghijklmnopqrstuvwxyz":
		i= "abcdefghijklmnopqrstuvwxyz".index(alphabet)+1
		return  'Position of alphabet: %d' %(i)

	return "Position of alphabet: %s" % ("abcdefghijklmnopqrstuvwxyz".find(alphabet) + 1)
	return "Position of alphabet: %d" % (ord(letter) - 96)


print(position('a'), 1)
print(position('z'), 26)
print(position('e'), 5)