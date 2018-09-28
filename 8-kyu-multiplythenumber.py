#8 kyu Multiply the number
def multiply(n):
	l=len(str(n))
	return n*5**(len(str(n))) if n>=0 else 1*n*5**(len(str(n))-1)


print(multiply(-2)) 
print(multiply(10))
print(multiply(200))
print(multiply(0))
print(multiply(-3))