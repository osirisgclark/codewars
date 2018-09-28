#7 kyu Hit Count
def counter_effect(hit_count):
	l = list()
	m= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	for x in hit_count:
		l.append(m[:m.index(int(x))+1])
	return l


print(counter_effect("1250"), [[0,1],[0,1,2],[0,1,2,3,4,5],[0]])
print(counter_effect("0050"), [[0],[0],[0,1,2,3,4,5],[0]])
print(counter_effect("0000"), [[0],[0],[0],[0]])

