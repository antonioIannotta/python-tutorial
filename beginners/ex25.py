class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5


point1 = Point()
point2 = Point(3, 4)

print(point1.x)
print(point1.y)
print(point2.x)
print(point2.y)
print(point2.distance_from_origin())
