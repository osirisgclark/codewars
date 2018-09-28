#8 kyu validate code with simple regex
import re
def validate_code(code):
	s = str(code)
	return True if re.findall('^[0-3]', s) else False


print(validate_code(123),'R == True')
print(validate_code(248),'R == True')
print(validate_code(8),'R == False')
print(validate_code(321),'R == True')
print(validate_code(9453),'R == False')




# Best:

# return True if re.match('^1|2|3', str(code)) else False

# .*             anything
# [^0-9]*        an optional character that is not a number
# [1][2][3][4]   "1234" done this way because it will be taken as a repeat count unless escaped
