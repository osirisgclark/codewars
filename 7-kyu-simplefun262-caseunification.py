#7 kyu Simple Fun #262: Case Unification
from string import ascii_uppercase
import re
def s(n):
	# a = len([letter for letter in n if letter in ascii_uppercase])
	# b= len(re.findall(r'[a-z]',n))
	# b= len(re.findall(r'[A-Z]',n))
	return n.upper() if len(re.findall(r'[A-Z]',n))>len(re.findall(r'[a-z]',n)) else n.lower()


print(s("HaHa"), 3)
