#8 kyu Convert boolean values to strings 'Yes' or 'No'.

def rps(k,y):
	if k==y:
		return "Draw!"

	else:
		if k == 'scissors':
			if y == 'paper':
				return "Player 1 won!"
			if y == 'rock':
				return "Player 2 won!"
		if k== 'paper':
			if y == 'rock':
				return "Player 1 won!"
			if y == 'scissors':
				return "Player 2 won!"	
		if k== 'rock':
			if y == 'scissors':
				return "Player 1 won!"
			if y == 'paper':
				return "Player 2 won!"		
	#string = preg_replace('/!+$/', '', k);


print(rps('scissors','scissors'))
print(rps('scissors','paper'))
print(rps('scissors','rock'))
print(rps('paper','paper'))
print(rps('paper', 'rock'))
print(rps('paper', 'scissors'))
print(rps('rock', 'rock'))
print(rps('rock', 'scissors'))
print(rps('rock', 'paper'))
