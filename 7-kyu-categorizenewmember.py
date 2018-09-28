7 kyu Categorize New Member


def openOrSenior(data):
	# l=list()
	# for x in data:
	# 	if x[0]>=55 and x[1]>7:
	# 		l.append('Senior') 
	# 	else:
	# 		l.append('Open')
	# return l

	
	return ['Senior'  if (x[0]>=55 and x[1]>7) else 'Open' for x in data  ]



print(inpu([[18, 20],[45, 2],[61, 12],[37, 6],[21, 21],[78, 9]]), ["Open", "Open", "Senior", "Open", "Open", "Senior"]
)


