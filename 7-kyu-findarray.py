#7 kyuFind array

def find_array(arr1, arr2)::
	return [arr1[x] for x in arr2 if x<= len(arr1)]



print(find_array(['a', 'a', 'a', 'a', 'a'], [2, 4])) # find_array returns ['a', 'a']

print(find_array([0, 1, 5, 2, 1, 8, 9, 1, 5], [1, 4, 7]))# find_array returns [1, 1, 1]

print(find_array([0, 3, 4], [2, 6])) #find_array returns [4]

print(find_array(["a","b","c","d"] , [2,2,2])) #, find_array returns ["c","c","c"]

print(find_array(["a","b","c","d"], [3,0,2])) # find_array returns ["d","a","c"]