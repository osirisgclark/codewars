#8 kyu repeatIt

def repeat_it(string,n):
    return string * n if isinstance(string,str) else 'Not a string'


repeat_it("*",3)
repeat_it("Hello",10)