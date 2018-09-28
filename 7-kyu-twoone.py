# #7 kyu Two to One

# Description:
# Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible, containing distinct letters, - each taken only once - coming from s1 or s2.

# Examples:
# a = "xyaabbbccccdefww"
# b = "xxxxyyyyabklmopq"
# longest(a, b) -> "abcdefklmopqwxy"

# a = "abcdefghijklmnopqrstuvwxyz"
# longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"


def longest(s1, s2):
    # your code
    k = list(s1 +s2)
    lista = list()
    for letter in k:
        if letter not in lista:
            lista.append(letter)
            lista.sort()
    return "".join(lista)

print(longest("xyaabbbccccdefww","xxxxyyyyabklmopq"))

    # Best:
    # def longest(s1, s2):
    # return "".join(sorted(set(s1+s2)))

    # def longest(s1, s2):
    # set1 = set(s1)
    # set2 = set(s2)
    # return "".join(sorted(set1 | set2))