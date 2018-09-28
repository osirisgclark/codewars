#8 kyu Even or Odd
def even_or_odd(number):	
    if number%2 == 0:
        return "Even"
    else:
        return "Odd"


print(even_or_odd(2)) #== "Even")
print(even_or_odd(1)) #== "Odd")
print(even_or_odd(0)) #== "Even")
print(even_or_odd(1545452)) #== "Even")
print(even_or_odd(7)) #== "Odd")
print(even_or_odd(78)) #== "Even")
print(even_or_odd(17)) #== "Odd")
print(even_or_odd(74156741)) #== "Odd")
print(even_or_odd(100000)) #== "Even")


# Best:
# def even_or_odd(number):
#   return 'Even' if number % 2 == 0 else 'Odd'