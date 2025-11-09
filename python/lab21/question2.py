class Quadrilateral:#parent class
    def __init__(self, side1, side2, side3, side4):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.side4 = side4

    def isSquare(self):
        return self.side1 == self.side2 == self.side3 == self.side4

    def isRectangle(self):
        return (self.side1 == self.side3) and (self.side2 == self.side4) and not self.isSquare()

class Rectangle(Quadrilateral): #child class 1
    def __init__(self, length, breadth): #call the parent constructor: when opp sides are eq
        super().__init__(length, breadth, length, breadth)

    def getArea(self):
        return self.side1 * self.side2

class Square(Quadrilateral): #child class 2
    def __init__(self, side): #call parent constructor when all sides equal
        super().__init__(side, side, side, side)

    def getArea(self):
        return self.side1 ** 2

# for creating a rectangle
rect = Rectangle(6, 4)
print("Rectangle:")
print("Is rectangle?", rect.isRectangle())
print("Area of rectangle =", rect.getArea())
print()

# for creating a square
sq = Square(5)
print("Square:")
print("Is square?", sq.isSquare())
print("Area of square =", sq.getArea())
