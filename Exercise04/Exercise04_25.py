x1, y1, x2, y2, x3, y3, x4, y4 = eval(input("Enter x1, y1, x2, y2, x3, y3, x4, y4: "))

a = (y1 - y2)
b = -(x1 - x2)
c = (y3 - y4)
d = -(x3 - x4)
e = (y1 - y2) * x1 - (x1 -x2) * y1
f = (y3 - y4) * x3 - (x3 -x4) * y3

detA = a * d - b * c
    
if detA == 0:
    print("The two lines are parallel")
else:
    x = (e * d - b * f) / detA
    y = (a * f - e * c) / detA
    print("The intersecting point is at (" + str(x) + ", " +  str(y) + ")")
