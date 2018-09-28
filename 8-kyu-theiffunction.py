#8 kyu The 'if' function
def _if(bool, func1=True, func2 =False):
	if bool == True: 
		return func1()
	else:
		return func2()

# era una mierda este ejemplo
# Best:
# def _if(bool, func1, func2):
#   if bool:
#       func1()
#   else:
#       func2()
#or return func1() if b else func2()

test.describe("The if function")

test.it("Should work for the examples:")
test.assert_equals(True, "True")
test.assert_equals(_if(False), "False")
test.assert_equals(_if(True), "True")
test.assert_equals(_if(False), "False")