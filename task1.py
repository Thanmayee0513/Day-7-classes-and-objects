import math


class Point():
    x=0
    y=0



P1=Point()
P2=Point()
P1.x=5
P1.y=6
P2.x=6
P2.y=5

def distance_between_points(Point,P1,P2):
    distance=math.sqrt((P2.x-P1.x)**2+(P2.y-P1.y)**2)
    return distance


print(distance_between_points(Point,P1,P2))









