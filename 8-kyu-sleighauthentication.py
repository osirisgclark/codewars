#8 kyu Sleigh Authentication


class Sleigh(object):
    def authenticate(self, name, password):
        if name== 'Santa Claus' and password == 'Ho Ho Ho!':
            return True
        return False


print(sleigh('Santa Claus', 'Ho Ho!'))
print(sleigh('jhoffner', 'CodeWars'))
print(sleigh('Santa Claus', 'Ho Ho Ho!') )