class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, new_width):
        self.width = new_width
        print(f'width has been updated to {self.width}!')

    def set_height(self, new_height):
        self.height = new_height
        print(f'height has been updated to {self.height}!')

    def get_area(self):
        self.area = self.height*self.width
        return f"The area is {self.width}x{self.height}={self.area}"
    
    def get_perimeter(self):
        self.perim = 2*self.height + 2*self.width
        return f"The perimeter is 2*{self.width}+2*{self.height}={self.perim}"
    
    def get_diagonal(self):
        self.diag = (self.height**2 + self.width**2)**0.5
        return f"The diagonal is sqrt({self.width}^2x{self.height}^2)={self.diag:.2f}" 

    def get_picture(self):
        picture = ''
        if self.width > 50 or self.height > 50:
            return 'Too big for the picture'
        for i in range(self.height):
            for j in range(self.width):
                picture += '*'
            picture += f'\n'
        return picture
    
    def get_amount_inside(self, other_shape): #other shape is rectangle or square
#it returns the number of times or how many times the other_shape fits inside the current shape
        other_shape.get_area()
        self.get_area()
        fitting = self.area//other_shape.area #// is will round down every number 1.2=>1 3.8=>3
        return f"({self.height}x{self.width}/{other_shape.width}x{other_shape.height})={fitting}\n{self.area}/{other_shape.area}"

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    def __init__(self, length):
        #super().__init__(length, length)
        self.width = length
        self.height = length
    
    def set_width(self, new_length):
        self.height = new_length
        self.width = new_length
        print(f'side length has been updated to {new_length}!')

    def set_height(self, new_length):
        self.height = new_length
        self.width = new_length
        print(f'side length has been updated to {new_length}!')

    def set_side(self, side_length):
        self.height = side_length
        self.width = side_length
        print(f'side length has been updated to {side_length}!')

    def __str__(self):
        return f"Square(side={self.height})"
    
rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
