#7 kyu Kooka-Counter
def kooka_counter(laughing):
	l=list()
	c=0
	if laughing== '':
		return 0
	else:
		for x in laughing:
			if x!= 'a':
				l.append(x)
		for i in range(1,len(l)):
			if l[i] != l[i-1]:
				c+=1
		return c+1


print(kooka_counter("HaHaHahahaHaHa"), 3)


