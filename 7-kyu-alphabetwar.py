def AlphabetWar(n):
	l = list()
	Left={'w':4, 'p':3, 'b':2, 's':1}
	r = list()
	Right={'m':4, 'q':3, 'd':2, 'z':1}
	for x in n:
		if x in Left:
			l.append(Left[x])
		elif x in Right:
			r.append(Right[x])
		else:
			continue
	return 'Left side wins!' if sum(l) >sum(r) else 'Right side wins!' if sum(r)>sum(l) else "Let's fight again!"


print(AlphabetWar("zdqmwpbs"))