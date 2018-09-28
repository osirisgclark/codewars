#  8 kyu Basic Mathematical Operations

def basic_op(a, b , c):
	if a == '+':
		return b+c
	elif a == '-':
		return b-c
	elif a== '*':
		return b*c
	else:
		return b/c


print(basic_op('+', 4, 7) , 11)
print(basic_op('-', 15, 18), -3)
print(basic_op('*', 5, 5) , 25)
print(basic_op('/', 49, 7) , 7)



# Best:
# def basic_op(o, a, b):
#     return {'+':a+b,'-':a-b,'*':a*b,'/':a/b}.get(o)