#8 kyu Name Shuffler

import re
def name_shuffler(arr):
	return ' '.join(re.split(" ", arr)[::-1])
	# return ' '.join(str.split(' ')[::-1])

print(name_shuffler('john McClane'), "McClane john")
