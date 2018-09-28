#8 kyu Simple Fun #261: Whose Move
def whoseMove(lastPlayer, win):
	return 'white' if (lastPlayer=='black' and win==False) or (lastPlayer=='white' and win==True) else 'black'




print(whoseMove('black', False),'white')
print(whoseMove('white', False),'black')
print(whoseMove('black', True),'black')
print(whoseMove('white', True),'white')