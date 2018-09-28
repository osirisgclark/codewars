#	6 kyu-Pizza pieces
def max_pizza( cut ):	
	if cut< 0:
	   return(-1)
	else:
	   sum = 1
	   for x in range (cut+1):
	   		sum += x
	   return sum
print (max_pizza(-100000), -1)
print (max_pizza(-5), -1)
print ("Aqui")
print (max_pizza(0), 1)
print("oooo")
print (max_pizza(1), 2)
print (max_pizza(2), 4)

print (max_pizza(3), 7)
print (max_pizza(4), 11)
print (max_pizza(5), 16)
print (max_pizza(6), 22)
print (max_pizza(7), 29)
print (max_pizza(8), 37)
print (max_pizza(9), 46)
print (max_pizza(10), 56)
print (max_pizza(11), 67)
print (max_pizza(12), 79)
print (max_pizza(15), 121)
print (max_pizza(20), 211)
print (max_pizza(100), 5051)
print (max_pizza(250), 31376)
print (max_pizza(45000), 1012522501)




#second way with a while :
# def max_pizza( cut ):	
# 	if cut< 0:
# 	   return(-1)
# 	else:
# 		while(cut > 0):
# 			sum += cut
# 			cut -= 1
# 	   return sum