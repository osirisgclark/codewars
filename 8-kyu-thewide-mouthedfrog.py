#8 kyu The Wide-Mouthed frog!

def mouth_size(animal):
    return "small" if animal.lower() == "alligator" else "wide"


test.assert_equals(mouth_size("toucan"),"wide")
test.assert_equals(mouth_size("ant bear"),"wide")
test.assert_equals(mouth_size("alligator"),"small")