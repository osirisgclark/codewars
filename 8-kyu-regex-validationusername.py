#  8 kyu simple validation of a username with regex
import re
def validate_usr(username):
	if 4<=len(username)<= 16 :
		return True if  re.findall('^[a-z0-9_]+$', username) else False
	else:
		return False


print(validate_usr('asddsa'), True)
print(validate_usr('a'), False)
print(validate_usr('Hass'), False) #ayusculas
print(validate_usr('Hasd_12assssssasasasasasaasasasasas'), False)
print(validate_usr(''), False)
print(validate_usr('____'), True)
print(validate_usr('012'), False)
print(validate_usr('p1pp1'), True)
print(validate_usr('asd43 34'), False) #espacios
print(validate_usr('asd43_34'), True)



# BEst:
# import re
# def validate_usr(un):
#     return re.match('^[a-z0-9_]{4,16}$', un) != None

# import re
# def validate_usr(username):
#     if re.match(ur'^[a-z0-9_]{4,16}$', username):
#         return True
#     else:
#         return False