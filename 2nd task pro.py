class Point():
    def __init__(self, xcor, ycor):
        self.xcor = xcor
        self.ycor = ycor
    def distance_to_zero(self):
        return int(((self.xcor)**2 + (self.ycor)**2)**0.5)
fi = int(input("Input the x coordinate: \n"))
se = int(input("Input the y coordinate: \n"))
dist = Point(fi, se)
print(dist.distance_to_zero())