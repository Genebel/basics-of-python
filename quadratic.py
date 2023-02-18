import math
a = int(input("enter first value: "))
b = int(input("enter second value: "))
c = int(input("enter third value: "))
d = math.sqrt(b*b-4*a*c)

if d>0:
    r1 = (-b+d)//2*a
    r2 = (-b-d)//2*a
    print("the roots are ", r1, r2)

elif d==0:
    r1=-b/(2*a)
    print(r1)

else:
    print("the roots are complex")





# r1 = (-b+math.sqrt(d))/2*a
# r2 = (-b-math.sqrt(d))/2*a
# if(d>0):
    # print("roots are real and distinct")
# else:
    # (d==0):
    # print("roots are real and equal")
# 