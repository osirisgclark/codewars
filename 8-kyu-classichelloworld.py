#8 kyu Classic Hello World

class Solution():
    @staticmethod
    def main(*args):
        print('Hello World!')



Test.describe("Basic tests")
Test.it("Testing with no extra parameter")
print(Solution.main,result="Hello World!")
Test.it("Testing with 'Hello World!' as extra parameter")
print(Solution.main,"Hello World!",result="Hello World!")
Test.it("Testing with 'Hello World' as extra parameter")
print(Solution.main,"Hello World",result="Hello World!")
Test.it("Testing with 'hello world!' as extra parameter")
print(Solution.main,"hello world!",result="Hello World!")
Test.it("Testing with 'Greetings from Javatlacati' as extra parameter")
print(Solution.main,"Greetings from Javatlacati",result="Hello World!")
Test.it("Testing with 'several parameters' as extra parameter")
print(Solution.main,["Greetings from Javatlacati","Hello Wo"],result="Hello World!")