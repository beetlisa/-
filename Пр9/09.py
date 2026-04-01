from abc import ABC, abstractmethod

class ShapePerimeter(ABC):
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(ShapePerimeter):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
        
rect = Rectangle(3, 4)
print(rect.perimeter())