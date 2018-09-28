# write-number-in-expanded-form
def expanded_form(num):
	p= str(num)
	j,*i=p.split('.')
	e=enumerate
	z='0'
	return ' + '.join([(x+len(j[y+1:])*z)for y,x in e(j)if x>z]+['.'+o*z+p for o,p in e(i)if p>z]or z)


# BEst:
# def expanded_form(num):
#     return " + ".join([str(int(d) * 10**p) for p, d in enumerate(str(num)[::-1]) if d != "0"][::-1])

# def expanded_form(num):
#     return ' + '.join([a+'0'*b for b, a in zip(reversed(range(len(str(num)))), str(num)) if a not in '0'])

# def expanded_form(n):
#     result = []
#     for a in range(len(str(n)) - 1, -1, -1):
#         current = 10 ** a
#         quo, n = divmod(n, current)
#         if quo:
#             result.append(str(quo * current))
#     return ' + '.join(result)


# def expanded_form(num):
#     num = str(num)
#     st = ''
#     for j, i in enumerate(num):
#         if i != '0':
#             st += ' + {}{}'.format(i, (len(num[j+1:])*'0'))
#     return st.strip(' +')


print (expanded_form(12), '10 + 2')
print(expanded_form(42),'40 + 2')
print(isOpposite(222), '200 + 20 + 2')
print(isOpposite(4561), '4000 + 500 + 61 +1')
print(expanded_form(70304, '70000 + 300 + 4')


