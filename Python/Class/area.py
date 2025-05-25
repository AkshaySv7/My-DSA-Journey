class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


# Example usage
rect = Rectangle(10, 5)
print("Area:", rect.area())           # Output: 50
print("Perimeter:", rect.perimeter()) # Output: 30
