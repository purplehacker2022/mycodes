
import cmath
import math
def equationroots( a, b, c): 
    D = b * b - 4 * a * c 
    asif=math.sqrt(abs(D))
    if D > 0: 
        print(" real and different roots ") 
        print((-b + asif)/(2 * a)) 
        print((-b - asif)/(2 * a)) 
    elif D == 0: 
        print(" real and same roots") 
        print(-b / (2 * a)) 
    else:
        print("Complex Roots") 
        
a=int(input("enter the number= "))
b=int(input("enter the number= "))
c=int(input("enter the number= "))
print(equationroots(a,b,c))
