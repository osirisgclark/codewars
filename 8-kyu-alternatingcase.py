#8 kyu altERnaTIng cAsE <=> ALTerNAtiNG CaSe
def to_alternating_case(string):
    l = list()
    for x in string:
        if x.isupper():
            l.append(x.lower())
        elif x.islower():
            l.append(x.upper())
        else:
            l.append(x)
    return ''.join(l)



    # Best: 
    # return string.swapcase()