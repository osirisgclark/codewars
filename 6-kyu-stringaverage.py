#6 kyu String average
def average_string(s):
	l = list()
	m = s.split(" ")
	k = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
	q = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
	for x in m:
		if x in k:
			l.append(k[x])
		else:
			return "n/a"
	return q[int(sum(l)/len(l))]



print(average_string("zero nine five two"), "#four")
print(average_string("four six two three"), "three")
print(average_string("one two three four five"), "three")
print(average_string("five four"), "four")
print(average_string("zero zero zero zero zero"), "zero")
print(average_string("one one eight one"), "two")
print(average_string("one"), "one")
print(average_string(""), "n/a")
print(average_string("ten"), "n/a")
print(average_string("pippi"), "n/a")