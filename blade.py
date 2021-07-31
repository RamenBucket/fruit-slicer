from cmu_112_graphics import *
import time,random


def init(app):
    app.mousePress = False
    app.blade = list()
    
    #app.startpos = None
    app.bladeTime = 0
    app.minPoints = 4
    app.maxPoints = 100
    app.pointTime = 100

def insertBlade(app,index,coord):
    app.blade.insert(index,(coord, time.time())) # just for the blade here
        
def stepBlade(app):
    app.bladeTime += 1
    i = 0
    while i < len(app.blade):
        startTime = app.blade[i][1]
        if(time.time() - startTime)*1000 > app.pointTime:
            app.blade.pop(i)
        else:
            i += 1
        
def dist(x0,y0,x1,y1):
    dx = (x0-x1)**2
    dy = (y0-y1)**2
    return (dx+dy)**0.5

def rgbString(r, g, b):
    # Don't worry about the :02x part, but for the curious,
    # it says to use hex (base 16) with two digits.
    return f'#{r:02x}{g:02x}{b:02x}'


def drawBlade(app,canvas):
    for i in range(len(app.blade)-1):
        x,y = app.blade[i][0]
        x1,y1 = app.blade[i+1][0]
        s = (len(app.blade)-i)+3
        canvas.create_oval(x-s//2, y-s//2, x+s//2, y+s//2, fill = "black")
        canvas.create_line(x,y,x1,y1, width=s, fill = "black")
