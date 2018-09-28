#8 kyu Exclamation marks series #6: Remove n exclamation marks in the sentence from left to 

def remove(s, n):
    return s.replace("!", '', n)


print(remove("Hi!",1), "R = Hi")
print(remove("Hi!",100), "Hi")
print(remove("Hi!!!",1), "Hi!!")
print(remove("Hi!!!",100), "Hi")
print(remove("!Hi",1), "Hi")
print(remove("!Hi!",100), "Hi")
print(remove("!!!Hi !!hi!!! !hi",100), "Hi hi hi")
print(remove("!!!Hi !!hi!!! !hi",4), "Hi !hi!!! !hi")
print ('  ')
print(remove("!Hi!",1), "R = Hi!")#, "Hi!"
print(remove("!!!Hi !!hi!!! !hi",1), "R = !Hi !!hi!!! !hi")# "!!Hi !!hi!!! !hi"
print(remove("!!!Hi !!hi!!! !hi",3), "R =!Hi !!hi!!! !hi")#, "!Hi !!hi!!! !hi
print(remove("!!!Hi !!hi!!! !hi",5), "R = Hi hi!!! !hi")#  "Hi hi!!! !hi"
