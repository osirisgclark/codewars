#6 kyu Srot the inner ctonnet in dsnnieedcg oredr
def sort_the_inner_content(words):
	l = list()
	p= words.split(' ')
	for x in p:
		if len(x)==1:
			l.append(''.join(x))
		else:
			l.append(''.join(list(x[0])+sorted(list(x[1:-1]), reverse=True)+list(x[-1])))
	return ' '.join(l)



# print(sort_the_inner_content("sort the inner content in descending order"),"srot the inner ctonnet in dsnnieedcg oredr")
# print(sort_the_inner_content("wait for me"), "wiat for me")
# print(sort_the_inner_content("this kata is easy" ), "tihs ktaa is esay")
print(sort_the_inner_content("a trully love is better that thousand of lovers"), "a turlly lvoe is btteer that tusonhad of lvroes")

