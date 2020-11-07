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

        #Shift new center of masses
        newX, newY = centroid.find_centroid(points)
        (xShift, yShift) = 

        #shift new center of mass
        (x,y) = pos
        pos = (x+newX, y+newY) 

        #Shift points to new centers of masses
        f1 = Fruit(self.points,self.pos,self.vel,self.fruitType,self.uncut)
        f2 = Fruit(self.points,self.pos,self.vel,self.fruitType,self.uncut)
        return (f1, f2)

    def move(grav): #grav = pixels/frame, pre-calculated
        (dx, dy) = vel
        (x,y) = pos
        pos = (x+dx, y+dy) #change position based on velocity
        vel = (dx, dy+grav) #gravitational acceleration

fruits = set()

p = [(0,0),(1,0),(0,1),(1,1)]
f = Fruit(p, (0,0), (5,6), "orange", True)
