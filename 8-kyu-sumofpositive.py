#8 kyu Sum of positive
def positive_sum(arr):
	return sum(x for x in arr if x > 0)
	#return sum(filter(lambda x: x > 0,arr))
    # l = list()
    # for x in arr:
    #     if x>0:
    #         l.append(x)
    # return sum(l)
print(positive_sum([1,2,3,4,5]),15)
print(positive_sum([1,-2,3,4,5]),13)
print(positive_sum([-1,2,3,4,-5]),9)