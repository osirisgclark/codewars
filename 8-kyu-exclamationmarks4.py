#8 kyu Exclamation marks series #4: Remove all exclamation marks from sentence but ensure a exclamation mark at the end of string

def remove(s):
    return s.replace("!", "")+"!"


print(remove("Hi!"))#, , "Hi!"

print(remove("Hi!!!"))# "Hi!"

print(remove("!Hi" ))#, "Hi!"
print(remove("!Hi!"))#, "Hi!"
print(remove("!Hi!"))#, "Hi!"
print(remove("Hi! Hi!"))# "Hi Hi!"
rint(remove("Hi"))# "Hi!"




#     tests = [
#     ["Hi!" , "Hi!"],
#     ["Hi!!!" ,"Hi!"],
#     ["!Hi" , "Hi!"],
#     ["!Hi!" , "Hi!"],
#     ["Hi! Hi!" , "Hi Hi!"],
#     ["Hi" , "Hi!"],
# ]

# for inp, exp in tests:
#     test.assert_equals(remove(inp), exp)