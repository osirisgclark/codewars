#8 kyu Convert number to reversed array of digits
def digitize(n):
    return list(map(int,str(n)))[::-1]
    #return [int(x) for x in str(n)][::-1]
    #return map(int, str(n)[::-1])



print(v(348597), [7,9,5,8,4,3])
print(v(35231), [1,3,2,5,3])