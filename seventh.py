class Shape():
    def __init__(self):
        super().__init__()
class Circle(Shape):
    def circle(self, radius):
        sq = int(3.14*(radius)**2)
        return f"The area of a circle is {sq}"
class Square(Shape):
    def square(self, side):
        sq = side**2
        return f"The area of a square is {sq}"
q = Square()
w = Circle()
ci = int(input("Input the radius of a circle:\n")) 
sq = int(input("Input the side square:\n"))   
print(w.circle(ci))
print(q.square(sq))
    