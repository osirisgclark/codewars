def total_bill(s):
	l = list()
	for x in s:
		if x == 'r':
			l.append(x)
	n = len(l)//5
	return 0 if len(l) == 0 else len(l)*2-2*n



print (total_bill('rr' ), 4)
print (total_bill('rr rrr'), 8)
print (total_bill('rrrrr rrrrr'), 16)
print (total_bill(' ' ), 0)
print(total_bill('rrrrrrrrrrrrrrrrrr   rr r'), 34)

Best:
# def total_bill(s):
#     return 2*(s.count("r") - s.count("r")//5)