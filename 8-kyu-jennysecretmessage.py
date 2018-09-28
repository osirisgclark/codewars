#8 kyu Jenny's secret message


def greet(name):
    return "Hello, my love!" if name == "Johnny" else "Hello, {name}!".format(name=name)
    


Test.describe("Jenny's greeting function")
Test.it("should greet some people normally")
Test.assert_equals(greet("James"), "Hello, James!")
Test.assert_equals(greet("Jane"), "Hello, Jane!")
Test.assert_equals(greet("Jim"), "Hello, Jim!")

Test.it("should greet Johnny a little bit more special")
Test.assert_equals(greet("Johnny"), "Hello, my love!")