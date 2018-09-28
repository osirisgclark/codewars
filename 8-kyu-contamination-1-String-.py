#8 kyu Contamination #1 -String-
def contamination(text, char):
	l= list()
	if text == "" or char == "":
		return "Si"
	else:
		for x in range(len(text)):
			l.append(char)
		return ''.join(l)



	

 
print(contamination("abc","z"), "zzz")
print(contamination("","z"), "")
print(contamination("abc",""), "")
print(contamination("_3ebzgh4","&"), "&&&&&&&&")
print(contamination("//case"," "), "      ")