import math

def quadratic(a,b,c):
    if not (isinstance(a, (int,float)) or isinstance(b, (int,float)) or isinstance(c, (int,float))):
        raise TypeError('bad operand type');
    deta = math.sqrt(b**2 - 4*a*c);
    x1 = (deta - b)/(2*a);
    x2 = (-deta - b)/(2*a);
    return x1,x2
