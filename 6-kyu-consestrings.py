#m= ["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"]
def longest_consec(strarr, k):
	l= list()
	w = list()
	if k <= 0 or len(strarr)<k or len(strarr) == 0:
		return ""

	if k == 1:
		return max(strarr, key=len)

	p = max(strarr, key=len)
	w.append(p)
	if k == 2:
		for x in strarr:
			if x not in l and x !=p and k:
				l.append(x)
		w.append(max(l, key=len))

		return "".join(sorted(w,key=strarr.index))

	if k==3:
		longest = 0
		longest_i = None
		for i in range(len(strarr)):
			length = sum(len(item) for item in strarr[i:i + k])
			if length > longest:
				longest = length
				longest_i = i
		return ''.join(strarr[longest_i:longest_i + k])


print(longest_consec([], 3)) # ""
print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15))# "")
print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0))# "")
print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2))# "")

print(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1))# "oocccffuucccjjjkkkjyyyeehh")

print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2)) # "abigailtheta"
print(longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2)) #"wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck")
print(longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2)) # "wlwsasphmxxowiaxujylentrklctozmymu")

print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3))# "ixoyx3452zzzzzzzzzzzz")

# Best:
# def longest_consec(strarr, k):
#     if (len(strarr) == 0 or k <= 0) or len(strarr) < k:
#         return ""
#     lst = [''.join(strarr[i:i+k]) for i in xrange(len(strarr))]
#     return max(lst, key= lambda x: len(x))


# def longest_consec(strarr, k):
#     result = ""
    
#     if k > 0 and len(strarr) >= k:
#         for index in range(len(strarr) - k + 1):
#             s = ''.join(strarr[index:index+k])
#             if len(s) > len(result):
#                 result = s
            
#     return result

# def longest_consec(strarr, k):
#     max = ""
#     for i in range(len(strarr)-k+1):
#         stri = ""
#         for n in range(k):
#             stri += strarr[i+n]
#         if (len(stri)>len(max)):
#             max = stri
#     return max