#8 kyu Geometry Basics: Distance between points in 2D
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance_between_points(a, b):
    return math.hypot(a.x- b.x, a.y-b.y)

    
print(distance_between_points(Point(1, 6),Point(4, 2)), 5)
print(distance_between_points((3, 3),(3, 3)), 0)
print(distance_between_points((1, 6),(4, 2)), 5)
print(round(distance_between_points((-10.2, 12.5), (0.3, 14.7)), 6), 10.728001)



# Best:
# 	def distance(self, x, y):
# 		return math.hypot(self.x-x, self.y-y)
		return ((b.x - a.x) ** 2 + (b.y - a.y) ** 2) ** 0.5

# import math
# class Point:
# 	def __init__(self, x, y):
# 		self.x = x
# 		self.y = y
	
# 	def __repr__(self):
# 		return 'Point({!r:}, {!r:})'.format(self.x, self.y)

# 	def distance_between_points(self, target):
# 		# self.a = Point(x1,y1)
# 		# self.b = Point(x2,y2)
# 		#return ((self.x ** 2) + (self.y ** 2)) ** 0.5
# 		return math.hypot(self.x- target.x, self.y-target.y)
