#7 kyu Find the lucky numbers

def filter_lucky(lst):
	l = list()
	import re
	for x in lst:
		y = str(x)
		if re.findall(r'[\d]+7+|7|7+[\d]', y):
			l.append(x)
	return l
	 
print (filterlucky([1,2,3,4,5,6,7,68,69,70,15,17]), [7,70,17])