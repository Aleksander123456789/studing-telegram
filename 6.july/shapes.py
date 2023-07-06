class Square():
    def __init__(self, side: int)
        if size < 0:
            raise ValueError('Размер стороны меньше 0!')
        self.side = side
    
    def calculate_square_area(self):
        return self.side * self.side
    
    def calculate_square_perimeter(self):
        return self.side * 4
    
class Rectangle(Square):
    def __init__(self, side: int, second_side):
        self.second_side = second.side

    def calculate_rectangle_area(self):
        return self.second_side * side
    
    def calculate_rectangle_perimeter(self):
        return (self.second_side + self.side) * 2

class Circle(Square):
    def __init__(self, side: int,  lenght: int):
        self.lenght = lenght
    
    def calculate_circle_area(self):
        return (self.lenght * (self.side**0.5))/2
    
    def calculate_circle_perimeter(self):
        return 2 * pi * (self.side/2)



