#8 kyu Get Planet Name By ID
def get_planet_name(id):
    d = {1: "Mercury", 2: "Venus", 3: "Earth", 4: "Mars", 5: "Jupiter", 6: "Saturn", 7: "Uranus", 8: "Neptune"}
    return d[id]


print(get_planet_name(1), "Mercury" )