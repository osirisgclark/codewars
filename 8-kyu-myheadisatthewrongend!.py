def fix_the_meerkat(arr):
	arr[0], arr[2]= arr[2], arr[0]
	return arr
	# or return arr[::-1]
 # or     arr.reverse()
 #    return arr

print(fix_the_meerkat(["tail", "body", "head"]), ["head", "body", "tail"])
print(fix_the_meerkat(["tails", "body", "heads"]), ["heads", "body", "tails"])
print(fix_the_meerkat(["bottom", "middle", "top"]), ["top", "middle", "bottom"])
print(fix_the_meerkat(["lower legs", "torso", "upper legs"]), ["upper legs", "torso", "lower legs"])
print(fix_the_meerkat(["ground", "rainbow", "sky"]), ["sky", "rainbow", "ground"])