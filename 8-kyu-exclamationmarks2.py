#8 kyu Exclamation marks series #2: Remove all exclamation marks from the end of sentence
import re

def remove(s):
	return s.rstrip("!") #re.sub(r'!+$', '', s)
	#return re.sub(r'/!+$/gm', '', s)
	# return re.sub(r'/(?!^)!/', '', s)
	# return re.sub(r'/!+$/', '', s)

print(remove("Hi!"), "R = Hi")
print(remove("Hi!!!"), "R = Hi")
print(remove("!Hi"), "R = !Hi")
print(remove("!Hi!"), "R = !Hi")
print(remove("Hi! Hi!"), " R = Hi! Hi")
print(remove("Hi"), "R = Hi")


# Best:
# def remove(s):
#     return s.rstrip("!")

# def remove(s):
#     while s and s[-1] == "!":
#         s = s[:-1]
#     return s

# def remove(s):
#     while s.endswith("!"):
#         s = s[0:-1] # o puede ser s = s[:-1]
#     return s

# import re
# def remove(s):
#     return re.match(r"(.*[^!]+)\!*", s).group(1)

# import re
# def remove(s):
#     return(re.match("^(.*?)!*$", s).groups()[0])

# import re
# result = re.sub(pattern, replacement, subject)
# result = re.sub(pattern, replacement, subject, limit)
# preg_replace — Perform a regular expression search and replace

# Description
# mixed preg_replace ( mixed $pattern , mixed $replacement , mixed $subject [, int $limit= -1 [, int &$count ]] )