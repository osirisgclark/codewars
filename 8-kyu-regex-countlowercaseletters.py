#8 kyu Regex count lowercase letters
import re
def lowercaseCount(s):
	return len(''.join(re.findall('[a-z]+', s)))


from collections import Counter
def lowercaseCount(s):
	l= list()
	for x in 'abcdefghijklmnopqrstuvwxyz':
		if x in s:
			l.append(x)
	return len(l)

8 kyu
Count of positives / sum of negatives



print(lowercaseCount("abc"), 3)
print(lowercaseCount("abcABC123"), 3)
print(lowercaseCount("abcABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~"), 3)
print(lowercaseCount(""), 0)
print(lowercaseCount("ABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~"), 0)
print(lowercaseCount("abcdefghijklmnopqrstuvwxyz"), 26)


Best:
#return len(re.findall('[a-z]',string))