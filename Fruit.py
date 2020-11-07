import centroid
import math

def getVelVectors(slope):
        vel = 2 #magnitude of velocity imparted
        angle = math.atan(slope)
        print("angle:", angle)
        vx1, vy1 = math.cos(angle)*vel,math.sin(angle)*vel
        #vx2, vy2 = math.cos(angle+math.pi)*vel,math.sin(angle+math.pi)*vel
        return (vx1,vy1)#,(vx2,vy2) #first coordinate is always on the right

def testVelVectors():
        slope = 9999
        print(getVelVectors(slope))

testVelVectors()

class Fruit(object):
    def __init__(self, points, pos, vel, fruitType, uncut):
        self.points = points
        self.pos = pos
        self.vel = vel
        self.fruitType = fruitType
        self.uncut = uncut
    
    def slice(p0, p1):
        
        #CONVERT TO GLOBAL
        #slice array into two new arrays
        #CONVERT BACK TO RELATIVE to proceed
        (cutX0, cutY0), (cutX1, cutY1) = p0, p1
        
        points1 = self.points
        points2 = self.points

        #shift new center of mass
        (xShift1, yShift1) = centroid.find_centroid(points1)
        (xShift2, yShift2) = centroid.find_centroid(points2)

        (x,y) = pos
        pos1 = (x+xShift1, y+yShift1) 
        pos2 = (x+xShift2, y+yShift2)
        
        #Shift points to new centers of masses
        for i in range(len(points1)):
            (pX, pY) = points1[i]
            points1[i] = (pX - xShift1, pY - yShift1)

        for i in range(len(points2)):
            (pX, pY) = points2[i]
            points2[i] = (pX - xShift2, pY - yShift2)

        #Compute new velocities
        cutSlope = (cutY1-cutY0)/(cutX1-cutX0)
        velSlope = -1/cutSlope #perpendicular
        #change velocities
        (dvx,dvy) = getVelVectors(velSlope) #change in velocity ,(dvx2,dvy2))
        (vx, vy) = self.vel #original velocity
        vel1, vel2 = self.vel, self.vel #initialize vars

        (x1,y1), (x2,y2) = pos1, pos2 #original positions
        if(x1>x2): #poly1 is moving to the right
            vel1 = (vx+dvx, vy+dvy) 
            vel2 = (vx-dvx, vy-dvy)
        else: #poly2 is moving right
            vel1 = (vx-dvx, vy-dvy) 
            vel2 = (vx+dvx, vy+dvy)

        f1 = Fruit(points1,pos1,vel1,self.fruitType,self.uncut)
        f2 = Fruit(points1,pos1,vel2,self.fruitType,self.uncut)
        return (f1, f2)

    def move(grav): #grav = pixels/frame, pre-calculated
        (dx, dy) = vel
        (x,y) = pos
        pos = (x+dx, y+dy) #change position based on velocity
        vel = (dx, dy+grav) #gravitational acceleration



#global to center of mass - each coordiinate is defined relative to the centroid
# ex) centroid is (122,122) -- coordinates aree  (+1,-2),(-5,+7)

fruits = set()

p = [(0,0),(1,0),(0,1),(1,1)]
f = Fruit(p, (0,0), (5,6), "orange", True)
