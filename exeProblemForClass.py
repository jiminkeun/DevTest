#6-1

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def get(self):
        return (self.x, self.y)

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

p = Point(10, 20)
(x, y) = p.get()
print("1.\nx = %s\ny = %s"% (x, y))

p.setX(15)
p.setY(25)
(x, y) = p.get()
print("2.\nx = %s\ny = %s"% (x, y))

p.move(2, 2)
(x, y) = p.get()
print("3.\nx = %s\ny = %s"% (x, y))

# 6.4
# kospi
# kospi
# kospi
# kosdaq
# nasdaq
# kospi
