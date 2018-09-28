#6 kyu Srot the inner ctonnet in dsnnieedcg oredr


def adj_arr(arr):
    new_arr = []
    i = 0
    while i < len(arr):
        j = 0
        str_i = list(str(arr[i]))
        while j < len(str_i):
            if str_i[j] == '7':
                str_i[j] = '3'
            elif str_i[j] == '3':
                str_i[j] = '7'
            j += 1
        new_arr.append(int(''.join(str_i)))
        i += 1
    return new_arr


def sort_twisted37(arr):
    return adj_arr(sorted(adj_arr(arr)))




# print(sort_twisted37([1,2,3,4, 5,6,7,8,9]), [1,2,7,4,5,6,3,8,9])
# print(sort_twisted37([12,13,14]), [12,14,13])
# print(sort_twisted37([9,2,4,7,3]), [2,7,4,3,9])


	# m = sorted(arr)
	# l = list()
	# import re
	# for x in arr:
	# 	if x==3:
	# 		l.append(7)
	# 	elif x==7:
	# 		l.append(3)
	# 	else:
	# 		l.append(x)

	# return l


	# 	m = sorted(arr)
	# l = list()
	# import re
	# for x in m:
	# 	y = str(x)
	# 	if re.findall(r'[\d]+3+|3|3+[\d]', y):
	# 		j = y.replace('3', '7')
	# 		l.append(int(j))
	# 	elif re.findall(r'[\d]+7+|7|7+[\d]', y):
	# 		k = y.replace('7', '3')
	# 		l.append(int(k))
	# 	else:
	# 		l.append(x)
	# return l
