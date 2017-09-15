#smileyface.py
from math import *
from graphics import *
win =GraphWin("Click&Smile" , 500, 500)
win.setBackground('orange')
intro = Text(Point(250,480), "Click on window, Smileys are waiting :D")
intro.setFill('green')
intro.draw(win)

def drawCircle(x,y, r):
    aCircle =Circle(Point(x,y), r)
    aCircle.setFill('Yellow')
    aCircle.draw(win)

    center =aCircle.getCenter()
    r =aCircle.getRadius()
    
def drawFilledEye(x,y,eyesize):
   Eye= Circle(Point(x,y), eyesize)
   Eye.setFill('black')
   Eye.draw(win)


def drawMouth(x,y,r):
   m = Oval(Point(x-r//3,y+r//7), Point(x+r//3,y+10+r//7))
   m.setFill('white')
   m.draw(win)

def makeface(center, r, win): # change name
    #circle
    drawCircle(p.x,p.y, r)
    #lefteye
    drawFilledEye(p.x-radhalf ,p.y - radhalf,eyesize)
    #righteye
    drawFilledEye(p.x+radhalf,p.y - radhalf, eyesize)
    #mouth
    drawMouth(p.x,p.y,r)
  
def calculateDistance(point1, point2):
    x1 = point1.x
    y1 = point1.y
    
    x2 = point2.x
    y2 = point2.y

    distance = sqrt((x1-x2)**2 + (y1-y2)**2)
    return distance

def isOverlapping(point1, rad1, point2, rad2):
    circleDistance =calculateDistance(point1, point2)
    radsum= rad1 + rad2
    if(radsum > circleDistance):
        return True
    return False
    
    

#increase size of faces on drawing   
size=20
radhalf = size/4
eyesize = size/12
centerArr =[]
sizeArr= []
for i in range(500):
    p= win.getMouse()
    center = Point(p.x, p.y)
    centerCoord = p.x, p.y
    x=p.x
    y=p.y
    #Before making face, verify overlapping.
    #Verify with all existing circles.
    makeface(center, size, win)
    result = False
    for j in range(len(sizeArr)):
        result = isOverlapping(centerArr[j], sizeArr[j], center, size)
        if(result==True):
            break
    if(result == True):
        break
    
    sizeArr += [size]
    centerArr += [center]
    size=size+5

message = Text(Point(250,30), "Game Over!")
message.setFill('red')
message.draw(win)
points ='Hurray! You made '+ str(len(sizeArr) + 1)+ ' smileys'
pointsMsg = Text(Point(250,50), points)
pointsMsg.draw(win)
        

    
    



