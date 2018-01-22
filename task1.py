import math


class Point():
    """This is an empty class"""

P1=Point()
P2=Point()
P1.x1=5
P1.y1=6
P2.x2=6
P2.y2=5

def distance_between_points(Point,P1,P2):
    distance=math.sqrt((P2.x2-P1.x1)**2+(P2.y2-P1.y1)**2)
    return distance


print(distance_between_points(Point,P1,P2))









