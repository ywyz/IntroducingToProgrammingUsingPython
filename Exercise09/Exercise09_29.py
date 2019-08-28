from tkinter import * # Import tkinter
from random import randint
import math

width = 300
height = 200
radius = 2
        
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # Is point (x, y) close to this point
    def isNearBy(self, x, y):
        return distance(self.x, self.y, x, y) < radius + 3
    
class MainGUI:
    def __init__(self):   
        window = Tk() # Create a window
        window.title("Intersecting points") # Set title
        
        self.canvas = Canvas(window, width = width, height = height)
        self.canvas.pack()
        
        self.p1 = Point(randint(0, width - 1), randint(0, height - 1))
        self.p2 = Point(randint(0, width - 1), randint(0, height - 1))
        self.p3 = Point(randint(0, width - 1), randint(0, height - 1))
        self.p4 = Point(randint(0, width - 1), randint(0, height - 1))
        self.drawLines()
        
        self.canvas.bind("<B1-Motion>", self.mouseMoved)     
        window.mainloop() # Create an event loop
           
    def mouseMoved(self, event):
        if self.closeToAPoint(event.x, event.y):
            self.canvas["cursor"] = "plus"
        else:
            self.canvas["cursor"] = "arrow"
        
        if self.p1.isNearBy(event.x, event.y):
            self.p1.x = event.x
            self.p1.y = event.y
        elif self.p2.isNearBy(event.x, event.y):
            self.p2.x = event.x
            self.p2.y = event.y
        elif self.p3.isNearBy(event.x, event.y):
            self.p3.x = event.x
            self.p3.y = event.y
        elif self.p4.isNearBy(event.x, event.y):
            self.p4.x = event.x
            self.p4.y = event.y
            
        self.drawLines()
        
    def closeToAPoint(self, x, y):
        return self.p1.isNearBy(x, y) or self.p2.isNearBy(x, y) or self.p3.isNearBy(x, y)
    
    def drawLines(self):
        self.canvas.delete("line")
        self.canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, tags = "line")
        self.canvas.create_line(self.p3.x, self.p3.y, self.p4.x, self.p4.y, tags = "line")   
        x, y = self.crossPoint()
        self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill = "red", tags = "line")

    def crossPoint(self):
        a = (self.p1.y - self.p2.y)
        b = -(self.p1.x - self.p2.x)
        c = (self.p3.y - self.p4.y)
        d = -(self.p3.x - self.p4.x)
        e = (self.p1.y - self.p2.y) * self.p1.x - (self.p1.x - self.p2.x) * self.p1.y
        f = (self.p3.y - self.p4.y) * self.p3.x - (self.p3.x - self.p4.x) * self.p3.y
        
        detA = a * d - b * c
            
        if detA == 0:
            return None
        else:
            x = (e * d - b * f) / detA
            y = (a * f - e * c) / detA
            return x, y
        
def distance(x1, y1, x2, y2):
    return ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5
       
MainGUI()
