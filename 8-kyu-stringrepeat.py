#8 kyu String repeat
def repeat_str(repeat, string):
    return str(repeat*string)


print(repeat_str(6, "I"), "IIIIII")
print(repeat_str(5, "Hello"), "HelloHelloHelloHelloHello")
print(repeat_str(2, 'abc'), 'abcabc')