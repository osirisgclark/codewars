#6 kyu Your order, please

import re
def order(sentence):
	return ' '.join(sorted(sentence.split(), key=lambda x: int(''.join(filter(str.isdigit, x)))))
print(order("is2 Thi1s T4est 3a"))



def order(sentence):
    def sort_key(s):
        return next(c for c in s if c.isdigit())
    return ' '.join(sorted(sentence.split(), key=sort_key))