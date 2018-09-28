#8 kyu Parse nice int from char problem
def get_age(age):
	return int(age[0])

print(get_age("0 years old"), 0)
print(get_age("2 years old"), 2)
print(get_age("4 years old"), 4)
print(get_age("5 years old"), 5)
print(get_age("7 years old"), 7)