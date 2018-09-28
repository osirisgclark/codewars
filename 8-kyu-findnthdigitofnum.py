#8 kyu Find n'th Digit of a Number
def findDigit(n,nth):
	if nth >0:
		return int(list(str(num))[-nth]) if len(list(str(num)))>=nth and list(str(num))[-nth] != '-' else 0
	else:
		return -1


print(findDigit(5673, 4), 5)
print(findDigit(129, 2), 2)
print(findDigit(-2825, 3) , 8)
print(findDigit(-456, 4), 0)
print(findDigit(0, 20), 0)
print(findDigit(65, 0), -1)
print(findDigit(24, -8), -1)