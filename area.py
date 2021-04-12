from math import sqrt

def area(a:float,b:float,c:float,d:float,q:float):
    """
    q is qotr
    """
    p1=(a+b+q)/2
    p2=(c+d+q)/2
    s1=sqrt(p1*(p1-a)*(p1-b)*(p1-q))
    s2=sqrt(p2*(p2-c)*(p2-d)*(p2-q))
    return s1+s2

print(area(3,4,2,4,5))
