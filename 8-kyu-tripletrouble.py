#8 kyu Triple Trouble

def triple_trouble(one, two, three):
    l = len(one)
    ret = ""
    for i in range(l):
        t += one[i] + two[i] +three[i]
    return t


print(triple_trouble("aaa","bbb","ccc"), "abcabcabc")
print(triple_trouble("aaaaaa","bbbbbb","cccccc"), "abcabcabcabcabcabc")
print(triple_trouble("burn", "reds", "roll"), "brrueordlnsl")
print(triple_trouble("Bm", "aa", "tn"), "Batman")
print(triple_trouble("LLh", "euo", "xtr"), "LexLuthor")

# return ''.join(''.join(a) for a in zip(one, two, three))