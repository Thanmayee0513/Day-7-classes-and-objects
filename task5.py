
class Time:
    """Time class with the following attributes"""
    hours=0
    minutes=0
    seconds=0

t=Time()#creating an instance of the class Time
t.hours=1
t.minutes=59
t.seconds=3

def print_time(t):
    """Prints time in the following format
    %2d takes atleast 2integers"""

    print('%.2d:%.2d:%.2d' % (t.hours, t.minutes, t.seconds))


print_time(t)

