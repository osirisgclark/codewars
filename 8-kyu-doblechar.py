
# 8kyu-Double Char
def double_char(S):
	count =2
	l= list()
	for x in S:
		l.append(x*count)
	return "".join(l)

print (double_char("String"))# ==> "SSttrriinngg")
print(double_char("Hello World")) #==> "HHeelllloo  WWoorrlldd"

print(double_char("1234!_ ")) #==> "11223344!!__  "