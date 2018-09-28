#8 kyu Switch it Up!

# Description:
# When provided with a number between 0-9, return it in words.
# Input :: 1
# Output :: "One".
# Try using "Switch" statements.
# This kata is meant for beginners. Rank and upvote to bring it out of beta

def switch_it_up(number):
	lista = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	numlet = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
	k = lista.index(number)
	l = numlet[k]
	return l

print(switch_it_up('0'))

def switch_it_up(number):
    #your code here
  lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  numlet = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
  k = lista.index(number)
  l = numlet[k]
  return l

print(switch_it_up(0))
# Test.describe('Example tests')
# Test.assert_equals(switch_it_up(0), "Zero")
# Test.assert_equals(switch_it_up(9), "Nine")

# Best:
# def switch_it_up(number):
#     return 'Zero One Two Three Four Five Six Seven Eight Nine'.split()[number]

# def switch_it_up(number):
#     word = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
#     return word[number]

# def switch_it_up(n):
#     return ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine'][n]