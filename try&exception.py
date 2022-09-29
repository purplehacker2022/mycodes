a =int(input("enter the value of a := "))
b=int(input("enter the value of b:= "))
c=int(input("enter the value of c:="))
try:
    d=a/(b-c)
    print("the value of the expression is:=", d)
except (ZeroDivisionError):
    print("Can't divide with zero.  ")
