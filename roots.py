import math
def solve_quadratic_eqn(a:float,b:float, c:float):
    D = (b**2)-(4*a*c)
    x1=(-b + math.sqrt(abs(D)))/(2*a)
    x2=(-b - math.sqrt(abs(D)))/(2*a)
    if D>0:
        print("root 1 and root 2", x1 , x2 ,"Real and Unequal Roots")
    elif D==0:
        print("root 1", x1 ,"Real and Equal Roots :)")
    elif D<0:
        print("Complex Roots :(")
    return(x1,x2)

a=float(input("enter coefficient of x^2 of equation = "))
b=float(input("enter coefficient of x of equation = "))
c=float(input("enter constant term= "))
x=solve_quadratic_eqn(a,b,c)
print("two roots of given equation are ",x)
