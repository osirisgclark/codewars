#7 kyu Mumbling

# Description:
# This time no story, no theory. The examples below show you how to write function accum:

# Examples:
# accum("abcd")    # "A-Bb-Ccc-Dddd"
# accum("RqaEzty") # "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt")    # "C-Ww-Aaa-Tttt"
# The parameter of accum is a string which includes only letters from a..z and A..Z.


def accum(string):
	l = list()
	count= 0
	for x in string:
		count +=1
		w = x*count
		l.append(w.title()) 
		#print(count)
		#print(w)
		#print(l)
	return( "-".join(l))

#print(accum("abcd"))
#print(accum("RqaEzty"))
#print(accum("cwAt"))
print(accum("ZpglnRxqenU"))