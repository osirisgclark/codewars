# 7 kyu Friend or Foe?
def inn(n):
	l = list()
	for x in n:
		if len(x)==4:
			l.append(x)

	return l


print(inn(["Ryan", "Kieran", "Jason", "Yous"]))#, Output = ["Ryan", "Yous"])