def leftOfheLiNE(x0, y0, x1, y1, x2, y2):
    if (x1 - x0) * (y2 - y0) - (x2- x0) * (y1 - y0) > 0:
        return True
    else:
        return False

def onTheSameLine(x0, y0, x1, y1, x2, y2):
    if (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0) == 0:
        return True
    else:
        return False

def rightOfTheLine(x0, y0, x1,y1, x2, y2):
    if (x1- x0) * (y2 - y0) - (x2 - x0) * (y1 - y0) < 0:
        return True
    else:
        return False

def main():
    x0, y0, x1, y1, x2, y2 = eval(input("Enter coodinates for the three points p0, p1 and p2: "))
    

    if leftOfheLiNE(x0, y0, x1, y1, x2, y2):
        print("p2 is on the left side of the line from p0 to p1.")
    
    elif onTheSameLine(x0, y0, x1, y1, x2, y2):
        print("p2 is on the same line from p0 to p1.")
    
    elif rightOfTheLine(x0,y0, x1, y1, x2, y2):
        print("p2 is on the right side of the line from p0 to p1.")

main()
