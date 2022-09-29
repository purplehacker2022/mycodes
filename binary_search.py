list=[1,2,3,4,5,6,7,8,9]

def binary_search(list,key):
    l=0
    h = len(list)-1
    while l <= h:
        m=int ((l+h)/2)
        if key == list[m]:
            return m
        elif key <list[m]:
            h=m-1
        else:
            l= m+1
    else:
        return ()
    
item = int(input("enter element = "))
b = binary_search(list,item)
if (b >= 0):
    print("Found =",b)
else:
    print("none")
