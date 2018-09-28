#8 kyu BASIC: Making Six Toast.
def six_toast(num):
	return 6 -num if num < 6 else num-6
	#return abs(num-6)


print(six_toast(15), 9)
print(six_toast(6), 0)
print(six_toast(3), 3)
print(six_toast(0), 6)
print(six_toast(-10), 3)
