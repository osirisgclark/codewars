#8 kyu I love you, a little , a lot, passionately ... not at all

# def  how_much_i_love_you(nb_petals):
# 	n = nb_petals- 6*(nb_petals//6)
# 	p = {0: 'not at all', 1: 'I love you', 2: 'a little', 3:'a lot', 4: 'passionately', 5: 'madly', 6: 'not at all'}
# 	return p[nb_petals] if nb_petals in p else p[n]

#Best
def how_much_i_love_you(nb_petals):

    words = {1: 'I love you', 2: 'a little', 3: 'a lot', 4: 'passionately',
            5: 'madly', 0: 'not at all'}
    print(nb_petals%6)
    return words[nb_petals%6]




print(how_much_i_love_you(1), 'I love you')
print(how_much_i_love_you(2), 'a little')
print(how_much_i_love_you(3), 'a lot')
print(how_much_i_love_you(4), 'passionately')
print(how_much_i_love_you(5), 'madly')
print( )
print(how_much_i_love_you(7), 'I love you')
print( )
print(how_much_i_love_you(14), 'a little')
print(how_much_i_love_you(16), 'passionately')
print(how_much_i_love_you(17), 'madly')
print( )
print(how_much_i_love_you(21), 'a lot')
print(how_much_i_love_you(24), 'not at all')
print( )
print(how_much_i_love_you(25), 'todavia')
print(how_much_i_love_you(600), 'not at all')



