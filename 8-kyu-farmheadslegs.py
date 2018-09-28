#8 kyu Heads and Legs

def animals(heads, legs):
    if (legs <= 0 or heads <= 0):
        return (0, 0) if (heads==0 and legs==0) else 'No solutions'
    else:
        y = (legs- 2*(heads))/2
        z = heads- y
        return (int(z),int(y)) if (y.is_integer()== True and z >=0 and y >=0) else 'No solutions'

print(hl(1513, -520))
print(hl(72, 200)) # Return (44, 28)
print(hl(116, 282)) # Return (91, 25)
print(hl(12, 24)) # Return (12, 0)
print(hl(6, 24)) # Return (0, 6)
print(hl(344, 872)) # Return (252, 92)
print(hl(158, 616)) # Return (8, 150)

print(hl(25, 555)) # Return => "No solutions"
print(hl(12, 25)) # Return => "No solutions"
print(hl(54, 956)) # Return => "No solutions"
print(hl(5455, 54956)) # Return => "No solutions"


print(hl(0, 0)) # Return => (0, 0)
print(hl(-1, -1)) # Return => "No solutions"
print(hl(500, 0)) # Return => "No solutions"
print(hl(0, 500)) # Return => "No solutions"
print(hl(-45, 5)) # Return => "No solutions"
print(hl(5, -55)) # Return => "No solutions"