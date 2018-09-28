#7 kyu Vowel Count

def getCount(inputStr):
    l= list()
    for x in list(inputStr):
        if x in ['a','e', 'i', 'o', 'u' ]:
            l.append(x)
    return len(l)
    return sum(1 for x in inputStr if x in "aeiouAEIOU")
	return sum(x in 'aeiou' for x in inputStr)
	return sum([x in list('euioa') for x in string])
	return sum(inputStr.count(x) for x in ['a', 'e', 'i', 'o', 'u'])


print(getCount("abracadabra"),  5)
