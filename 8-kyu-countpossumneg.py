#8 kyu Count of positives / sum of negatives

def count_positives_sum_negatives(arr):
	l= list()
	m = list()
	return [] if len(arr)== 0 
	else:
		for x in arr: 
			if x >0:
				m.append(x)
			else:
				l.append(x)

		return [len(m),sum(l)]

print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]),[10,-65])
print(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]),[8,-50])
print(count_positives_sum_negatives([1]),[1,0])
print(count_positives_sum_negatives([-1]),[0,-1])
print(count_positives_sum_negatives([0,0,0,0,0,0,0,0,0]),[0,0])
print(count_positives_sum_negatives([]),[])



# Best:
# def count_positives_sum_negatives(arr):
#   output = []
#   if arr:
#     output.append(sum([1 for x in arr if x > 0]))
#     output.append(sum([x for x in arr if x < 0]))
#   return output

#   def count_positives_sum_negatives(arr):
#     return [len([x for x in arr if x > 0])] + [sum(y for y in arr if y < 0)] if arr else []