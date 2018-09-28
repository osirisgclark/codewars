#8 kyu Regexp Basics - is it a digit?
import re

def is_digit(n):
    return True if re.match('^[0-9]\Z', n) else False
	#return True if re.findall('^/\d+((.|,)\d+)?/', n) else False
	#return.isdigit() #n.isnumerci()
	#return True if re.findall('(^\d|^)\d(^\d|$)', n) else False
	#return True if re.findall('([^\d]|^)\d([^\d]|$)', n) else False
	#return True if len(n) == 10 and n.isdigit() else False
	#return True if re.findall('^([0-9]+)$', n) else False
	#return re.findall('\d*\.?\d+', n) 
	#return re.findall('[-+\d]+', n) #For negative numbers
	#return re.findall(r'(\d+)',  n) 
	#return re.findall('\\b\\d+\\b',  n) #r'\b\d+\b' == '\\b\\d+\\b')
	#return re.findall(r'\b\d+\b', '', n) #If you only want numbers delimited by word boundaries (space, period, comma)
	#return [int(x) for x in re.findall(r'\b\d+\b', n)] #To end up with a list of numbers instead of a list of strings
	#return [int(x) for x in re.findall('\\d+', n)] #To end up with a list of numbers instead of a list of strings
# \d+ o (\d+) o /(\d+)/
#  /\d+((.|,)\d+)?/
# .*             anything
# [^0-9]*        an optional character that is not a number
# [1][2][3][4]   "1234" done this way because it will be taken as a repeat count unless escaped



print(remove(""),' True')
print(remove(" "),' True')
print(remove("7"),' True')
print(remove("a"),' False')
print(remove("$"), ' False')
print(remove("1\n0"), ' False')
print(remove("1\n"), ' False')



Test.describe("Full tests")
Test.assert_equals(is_digit(""), False)
Test.assert_equals(is_digit("7"), True)
Test.assert_equals(is_digit(" "), False)
Test.assert_equals(is_digit("a"), False)
Test.assert_equals(is_digit("a5"), False)
Test.assert_equals(is_digit("14"), False)
Test.assert_equals(is_digit(" "), False)
Test.assert_equals(is_digit("!"), False)
Test.assert_equals(is_digit("\""), False)
Test.assert_equals(is_digit("#"), False)
Test.assert_equals(is_digit("$"), False)
Test.assert_equals(is_digit("%"), False)
Test.assert_equals(is_digit("&"), False)
Test.assert_equals(is_digit("'"), False)
Test.assert_equals(is_digit("("), False)
Test.assert_equals(is_digit(")"), False)
Test.assert_equals(is_digit("*"), False)
Test.assert_equals(is_digit("+"), False)
Test.assert_equals(is_digit(","), False)
Test.assert_equals(is_digit("-"), False)
Test.assert_equals(is_digit("."), False)
Test.assert_equals(is_digit("/"), False)
Test.assert_equals(is_digit("0"), True)
Test.assert_equals(is_digit("1"), True)
Test.assert_equals(is_digit("2"), True)
Test.assert_equals(is_digit("3"), True)
Test.assert_equals(is_digit("4"), True)
Test.assert_equals(is_digit("5"), True)
Test.assert_equals(is_digit("6"), True)
Test.assert_equals(is_digit("7"), True)
Test.assert_equals(is_digit("8"), True)
Test.assert_equals(is_digit("9"), True)
Test.assert_equals(is_digit(":"), False)
Test.assert_equals(is_digit(";"), False)
Test.assert_equals(is_digit("<"), False)
Test.assert_equals(is_digit("="), False)
Test.assert_equals(is_digit(">"), False)
Test.assert_equals(is_digit("?"), False)
Test.assert_equals(is_digit("@"), False)
Test.assert_equals(is_digit("A"), False)
Test.assert_equals(is_digit("B"), False)
Test.assert_equals(is_digit("C"), False)
Test.assert_equals(is_digit("D"), False)
Test.assert_equals(is_digit("E"), False)
Test.assert_equals(is_digit("F"), False)
Test.assert_equals(is_digit("G"), False)
Test.assert_equals(is_digit("H"), False)
Test.assert_equals(is_digit("I"), False)
Test.assert_equals(is_digit("J"), False)
Test.assert_equals(is_digit("K"), False)
Test.assert_equals(is_digit("L"), False)
Test.assert_equals(is_digit("M"), False)
Test.assert_equals(is_digit("N"), False)
Test.assert_equals(is_digit("O"), False)
Test.assert_equals(is_digit("P"), False)
Test.assert_equals(is_digit("Q"), False)
Test.assert_equals(is_digit("R"), False)
Test.assert_equals(is_digit("S"), False)
Test.assert_equals(is_digit("T"), False)
Test.assert_equals(is_digit("U"), False)
Test.assert_equals(is_digit("V"), False)
Test.assert_equals(is_digit("W"), False)
Test.assert_equals(is_digit("X"), False)
Test.assert_equals(is_digit("Y"), False)
Test.assert_equals(is_digit("Z"), False)
Test.assert_equals(is_digit("["), False)
Test.assert_equals(is_digit("\\"), False)
Test.assert_equals(is_digit("]"), False)
Test.assert_equals(is_digit("^"), False)
Test.assert_equals(is_digit("_"), False)
Test.assert_equals(is_digit("`"), False)
Test.assert_equals(is_digit("a"), False)
Test.assert_equals(is_digit("b"), False)
Test.assert_equals(is_digit("c"), False)
Test.assert_equals(is_digit("d"), False)
Test.assert_equals(is_digit("e"), False)
Test.assert_equals(is_digit("f"), False)
Test.assert_equals(is_digit("g"), False)
Test.assert_equals(is_digit("h"), False)
Test.assert_equals(is_digit("i"), False)
Test.assert_equals(is_digit("j"), False)
Test.assert_equals(is_digit("k"), False)
Test.assert_equals(is_digit("l"), False)
Test.assert_equals(is_digit("m"), False)
Test.assert_equals(is_digit("n"), False)
Test.assert_equals(is_digit("o"), False)
Test.assert_equals(is_digit("p"), False)
Test.assert_equals(is_digit("q"), False)
Test.assert_equals(is_digit("r"), False)
Test.assert_equals(is_digit("s"), False)
Test.assert_equals(is_digit("t"), False)
Test.assert_equals(is_digit("u"), False)
Test.assert_equals(is_digit("v"), False)
Test.assert_equals(is_digit("w"), False)
Test.assert_equals(is_digit("x"), False)
Test.assert_equals(is_digit("y"), False)
Test.assert_equals(is_digit("z"), False)
Test.assert_equals(is_digit("{"), False)
Test.assert_equals(is_digit("|"), False)
Test.assert_equals(is_digit("}"), False)
Test.assert_equals(is_digit("~"), False)
Test.assert_equals(is_digit("1\n0"), False)
Test.assert_equals(is_digit("1\n"), False)
Test.assert_equals(is_digit("1 "), False)
Test.assert_equals(is_digit(" 1"), False)




# Best:

# import re
# def is_digit(n):
#     return bool(re.match("\d\Z", n))

# def is_digit(n):
#     return n.isdigit() and len(n)==1


#GLENN HIZO ME GUSTO:

# import re
# tnum = 0
# def is_digit(n):
#     global tnum
#     tnum += 1
#     res = re.match(r'^[0-9]$', n ) and len(n)==1
    
#     if tnum == 103:
#         print( tnum, n, res )
#         print( n )
#         print( "class:", str(type(n)) )
#         print( "len:", len(n))
#         print("char0:", n[0] )
#         print("char1:", ord(n[1] ))
#         from pprint import pprint
#         pprint( dir( n ))
#         return False
#     return True if res else False



# import re
# tnum = 0
# def is_digit(n):
#     global tnum
#     tnum += 1
#     res = re.match(r'^[0-9]$', n, flags=re.M)
    
#     if tnum == 103:
#         print( tnum, n, res )
#         print( n )
#         print( "class:", str(type(n)) )
#         print( "len:", len(n))
#         print("char0:", n[0] )
#         print("char1:", ord(n[1] ))
#         from pprint import pprint
#         pprint( dir( n ))
#         return False
#     return True if res else False


# import re
# tnum = 0
# def is_digit(n):
#     global tnum
#     tnum += 1
#     res = re.match(r'^[0-9]$', n)
    
#     if tnum == 103:
#         print( tnum, n, res )
#         print( n )
#         print( "class:", str(n.__class__) )
#         print( "len:", len(n))
#         return False
#     return True if res else False



# import re
# tnum = 0
# def is_digit(n):
#     global tnum
#     tnum += 1
#     res = re.match(r'^[0-9]$', n)
    
#     if tnum == 103:
#         print( tnum, n, res )
#        print( n )
#        print( n.__class__ )
       
#        return False
#     return True if res else False
