"""
You will be given an array (a) and a value (x). All you need to do is check whether the provided array contains the value.

Array can contain numbers or strings. X can be either. Return true if the array contains the value, false if not.

"""


def check(seq, elem):
    return True if elem in seq else False


print(check([1, 2, 3, 4], 4))
print(check([1, 2, 3, 4], 5))


"""
Best way:
"""
# def check(seq, elem):
#     return elem in seq

