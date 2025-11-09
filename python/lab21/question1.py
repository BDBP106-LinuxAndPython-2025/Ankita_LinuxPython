class Quadrilateral:
    def __init__(self, side1, side2, side3, side4):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.side4 = side4

    def isSquare(self):
        return self.side1 == self.side2 == self.side3 == self.side4

    def isRectangle(self):
        return (self.side1 == self.side3) and (self.side2 == self.side4) and not self.isSquare()

# (a) All sides different
q1 = Quadrilateral(4, 3, 6, 5)
print("Case (a):")
print("Square:", q1.isSquare())
print("Rectangle:", q1.isRectangle())
print()

# check if opp sides are same: square or rectangle?
q2 = Quadrilateral(4, 6, 4, 6)
print("Case (b):")
print("Square:", q2.isSquare())
print("Rectangle:", q2.isRectangle())
print()

# if all sides are same: square or rectangle?
q3 = Quadrilateral(7, 7, 7, 7)
print("Case (c):")
print("Square:", q3.isSquare())
print("Rectangle:", q3.isRectangle())
