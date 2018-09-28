#8 kyu Dollars and Cents

#8 kyu Even or Odd
def find_difference(amount):
	return '${:.2f}'.format(amount)



print(find_difference(2)) #==8
print(find_difference(428.4)) #==14
print(find_difference(789)) #==106
print(find_difference(5.15))#==30
print(find_difference(1088.23))#==31
print(find_difference(1142.7)) #==0

