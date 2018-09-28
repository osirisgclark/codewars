#7 kyu Disemvowel Trolls


#Description:

# Trolls are attacking your comment section!
# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
# Your task is to write a function that takes a string and return a new string with all vowels removed.
# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

def comment_section(comments):
	lista = list()
	k = list(comments)
	vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
	for letter in k:
		if letter not in vowels:
			lista.append(letter)
	return "".join(lista)

print(comment_section("Espiga, espigada, tan elegante y estirada, esperas sin temor ser cortada"))
print(comment_section("This website is for losers LOL!")) # "Ths wbst s fr lsrs LL!"
print(comment_section("No offense but, \nYour writing is among the worst I've ever read")) # "N ffns bt, \nYr wrtng s mng th wrst 'v vr rd"
print(comment_section("What are you, a communist?")) #"Wht r y,  cmmnst?"


# best:
# def disemvowel(s):
#     return s.translate(None, "aeiouAEIOU")


# Ejemplos de .translate(,)
# m = "Espiga, espigada, tan elegante y estirada, esperas sin temor ser cortada"
# k = m.maketrans('aeiouAEIOU', "          ")
# l = m.translate(k)
# print("".join(l))
