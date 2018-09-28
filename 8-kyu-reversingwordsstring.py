#8 kyu Reversing Words in a String
def reverse(st):
    return ' '.join(reversed(st.split(' ')))



print(reverse('Hello World'),'e')
print(reverse('Hi There.'),'e')
print(reverse('quahaeppkeui'),'e')
print(reverse('dkfdhsosjolqq'),'e')