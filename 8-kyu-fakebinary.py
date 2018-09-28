#8 kyu Fake Binary
def fake_bin(x):
	l = list()
	for a in x:
		if a in ['0', '1', '2', '3', '4']:
			l.append('0')	
		else:
			l.append('1')
	return ''.join(l)


print(fake_bin("45385593107843568"))
print("01011110001100111")
print( )
print(fake_bin("509321967506747"))
print("101000111101101")
print( )
print(fake_bin("366058562030849490134388085"))
print("011011110000101010000011011")
print( )
print(fake_bin("15889923"))
print("01111100")
print( )
print(fake_bin("800857237867"))
print("100111001111")


# Best:
# def fake_bin(x):
#     return ''.join('0' if c < '5' else '1' for c in x)

# import string

# def fake_bin(s):
#     return s.translate(string.maketrans('0123456789', '0000011111'))