#7 kyu Simple Fun #177: Rank Of Element
def arr(n,i):
	l = list()
	ll=list()
	for x in n[:i]:
		if x <=n[i]:
			l.append(x)
	for x in n[i+1:]:
		if x <n[i]:
			ll.append(x)
	return len(l)+len(ll)


print(arr([2,1,2,1,2], 2), 3)

# n = 