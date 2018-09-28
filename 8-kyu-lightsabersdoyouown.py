#8 kyu How many lightsabers do you own?

	#fn = input(' Enter a name ')
	return 18 if fn in ['Zach','zach','ZACH'] else 0





# TODO: Replace examples and use TDD development by writing your own tests
# These are some of the methods available:
#   test.expect(boolean, [optional] message)
#   test.assert_equals(actual, expected, [optional] message)
#   test.assert_not_equals(actual, expected, [optional] message)

# You can use Test.describe and Test.it to write BDD style test groupings

Test.describe("Basic tests")
Test.assert_equals(howManyLightsabersDoYouOwn('Osiris'), 0)
Test.assert_equals(howManyLightsabersDoYouOwn('Zach'), 18)
Test.assert_equals(howManyLightsabersDoYouOwn('Sach'), 0)
Test.assert_equals(howManyLightsabersDoYouOwn('zach'), 18)
Test.assert_equals(howManyLightsabersDoYouOwn('Ben'), 0)
Test.assert_equals(howManyLightsabersDoYouOwn('ZACH'), 18)
Test.assert_equals(howManyLightsabersDoYouOwn('Zach'), 18)
Test.assert_equals(howManyLightsabersDoYouOwn(), 0)