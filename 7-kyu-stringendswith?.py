# 7 kyu String ends with?

def solution(string, ending):
	return True if string[len(ending)-1:len(string)]==ending else False


print(solution('abcde', 'cde'))
print(solution('abc', 'bc'))
print(solution('abc', 'd') )

print(solution('samurai', 'ai'))# to return True

print(solution('ninja', 'ja')) #to return True
print(solution('sensei', 'i')) # to return True

print(solution('abc', 'abc')) # to return True
print(solution('abcabc', 'bc')) # to return True
print(solution('fails', 'ails'))# to return True

# a = 'ninja'
# b = 'ja'
# m = len(a)
# l = len(b)
# p = a[m-l:m]

# print(m)
# print(l)
# print(p)