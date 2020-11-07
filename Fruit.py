import centroid

class Fruit(object):
    def __init__(self, points, pos, vel, fruitType, uncut):
        self.points = points
        self.pos = pos
        self.vel = vel
        self.fruitType = fruitType
        self.uncut = uncut

    def slice(p0, p1):
        #slice array into two new arrays
        #Compute new velocities
        points1 = self.points # arbitrary
        points2 = self.points

        (xShift1, yShift1) = centroid.find_centroid(points1)
        (xShift2, yShift2) = centroid.find_centroid(points2)

        #shift new center of mass
        (x,y) = pos
        pos1 = (x+xShift1, y+yShift1) 
        pos2 = (x+xShift2, y+yShift2)
        
        #Shift points to new centers of masses
        for i in range(len(points1)):
            (pX, pY) = points1[i]
            points1[i] = (pX - xShift, pY - yShift)

        for i in range(len(points2)):
            (pX, pY) = points2[i]
            points2[i] = (pX - xShift, pY - yShift)

        f1 = Fruit(self.points,self.pos,self.vel,self.fruitType,self.uncut)
        f2 = Fruit(self.points,self.pos,self.vel,self.fruitType,self.uncut)
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
