#8 kyu Invert values
def invert(lst):
    l= list()
    for x in lst:
        l.append(-x)
    return l



print(invert([1,2,3,4,5]),'R  == [-1,-2,-3,-4,-5]')
print(invert([1,-2,3,-4,5]),'R  == [-1,2,-3,4,-5]')

print(invert([]),'R  == []')



Best:
def invert(lst):
    return [-x for x in lst]