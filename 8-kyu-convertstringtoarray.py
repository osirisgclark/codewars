# 8 kyu Convert a string to an array


def string_to_array(string):
    return string.split() if len(string)!=0 else [""]
    #Best:
    #return string.split(" ")
    #return string.split() or ['']


print(string_to_array(""), [""])
print(string_to_array("Robin Singh"), ["Robin", "Singh"])
print(string_to_array("I love arrays they are my favorite"), ["I", "love", "arrays", "they", "are", "my", "favorite"])
print(string_to_array("1 2 3"), ["1", "2", "3"])