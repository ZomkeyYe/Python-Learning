import turtle
def drawTriangle(points, color, my_angle):
    my_angle.fillcolor(color)
    my_angle.up()
    my_angle.goto(points[0][0], points[0][1])
    my_angle.down()
    my_angle.begin_fill()
    my_angle.goto(points[1][0], points[1][1])
    my_angle.goto(points[2][0], points[2][1])
    my_angle.goto(points[0][0], points[0][1])
    my_angle.end_fill()

def getMid(p1, p2):
    return ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)
def sierpinski(points,degree,myTurtle):
    colormap = ['blue','red','green','white','yellow', 'violet','orange']
    drawTriangle(points,colormap[degree],myTurtle)
    if degree > 0:
        sierpinski([points[0], getMid(points[0], points[1]), getMid(points[0], points[2])], degree-1, myTurtle)
        sierpinski([points[1], getMid(points[0], points[1]), getMid(points[1], points[2])], degree-1, myTurtle)
        sierpinski([points[2], getMid(points[2], points[1]), getMid(points[0], points[2])], degree-1, myTurtle)
def main():
    myTurtle = turtle.Turtle()
    myWin = turtle.Screen()
    myPoints = [[-100,-50],[0,100],[100,-50]]
    sierpinski(myPoints,3,myTurtle)
    myWin.exitonclick()
main()