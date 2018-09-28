#8 kyu Counting sheep...
def count_sheeps(arrayOfSheeps):
	l = list()
	for x in arrayOfSheeps:
		if x == True:
			l.append(x)
	return len(l)

print(present([True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]))