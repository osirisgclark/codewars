#8 kyu Fix the Bugs (Syntax) - My First Kata

def my_first_kata(a,b):
	try:
		retval =  a % b + b % a
		if isinstance(a, bool) or isinstance(b, bool):
			return False
		return retval
	except:
		return False



print(my_first_kata(3,5),(3 % 5 + 5 % 3))
print(my_first_kata("hello",3),False)
print(my_first_kata(67,"bye"),False)
print(my_first_kata(True,True),False)
print(my_first_kata(314,107),(107 % 314 + 314 % 107))
print(my_first_kata(1,32),(1 % 32 + 32 % 1))
print(my_first_kata(-1,-1),(-1 % -1 + -1 % -1))
print(my_first_kata(19483,9),(9 % 19483 + 19483 % 9))
print(my_first_kata("hello",{}),False)
print(my_first_kata([],"pippi"),False)