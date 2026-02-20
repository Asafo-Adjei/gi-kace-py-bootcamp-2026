#Define the Rectangle Class

class Rectangle:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def getArea(self):
        return self.width * self.height
    
    def getPerimeter(self):
        return 2 * (self.width + self.height)
    

# Create Three Rectangle Objects and Print Their Areas

rect1 = Rectangle(4, 5)
rect2 = Rectangle(6, 3)
rect3 = Rectangle(10, 2)

print("Area of rect1:", rect1.getArea())
print("Area of rect2:", rect2.getArea())
print("Area of rect3:", rect3.getArea()) 



#What Happens If You Forget self?

# class Rectangle:
    
#     def __init__(self, width, height):
#         width = width
#         height = height

    
# rect = Rectangle(4, 5)
# print(rect.width)