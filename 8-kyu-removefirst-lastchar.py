# 8 kyu Remove First and Last Character
def remove_char(a):
	return s[1:len(s)-1]
	#return s[1:-1]


print(remove_char('eloquent'), 'loquen')
print(remove_char('country'), 'ountr')
print(remove_char('person'), 'erso')
print(remove_char('place'), 'lac')
print(remove_char('ok'), '')