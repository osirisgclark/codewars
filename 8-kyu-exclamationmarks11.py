#8 kyu Exclamation marks series #11: Replace all vowel to exclamation mark in the sentence

def replace(s):
	vowels = 'aeiouAEIOU'
	for vowel in vowels:
		s = s.replace(vowel, '!')
	return s 

	#return s.translate(str.maketrans('aeiouAEIOU', '!' * 10))

	#return s.translate(s.maketrans('aeiouAEIOU', '!!!!!!!!!!'))



print(replace("Hi!"))#, "H!!"
print(replace("ABCDE"))# "!BCD!"
print(replace("!Hi! Hi!"))# "!H!! H!!"
print(replace("aeiou"))#, "!!!!!"



# Best:
# import re
# def replace_exclamation(s):
#     return re.sub('[aeiouAEIOU]', '!', s)
# def replace_exclamation(s):
#    vowels = set('aeiouAEIOU')
#     return ''.join('!' if a in vowels else a for a in s)