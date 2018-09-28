#8 kyu Parse float
def parse_float(string):
    try:
    	return float(string)
    except:
    	return None
print(parse_float("1.0"), 1.0)
print(parse_float("234.0234"), 234.0234)
print(parse_float("a"), None)



# import re
# def parse_float(string):
#     return None if re.search("A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z", string) else float(string)

#     return float(string) if re.search("1|2|3|4|5|6|7|8|9|0", string) else None

