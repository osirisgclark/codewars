#8 kyuExclamation marks series #1: Remove a exclamation mark from the end of string


def remove(s):
    if len(s) == 0:
        return s
    else:
        return s[:len(s)-1] if s[len(s)-1] == '!' else s

print(remove("Hi!"))#, "Hi"

print(remove("Hi!!!"))# "Hi!!"

print(remove("!Hi"))#, "!Hi"

print(remove("!Hi!"))#, "!Hi"

print(remove("Hi! Hi!"))#, "Hi! Hi"

print(remove("Hi"))#, "Hi"


# Best: aprendi
# return s[:-1] if s.endswith('!') else s
# return s[:-1] if s and s[-1] == '!' else s
