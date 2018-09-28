#7 kyu Spot the Differences
def spot_diff(s1, s2):
	l = list()
	for x in range(len(s1)):
		if s1[x] != s2[x]:
			l.append(x)
	return l

print(spot_diff("abcdefg", "abcqetg"))
print(spot_diff('Hello World!', 'hello world.'))
print(spot_diff('FixedGrey', 'FixedGrey'))
print(spot_diff('aaasnntt', 'aapnataa'))