def area_calculator(n: int):
    def rectangle_area(a, b):
        a = int(input('Введите длину:'))
        b = int(input('Введите ширину:'))
        return a*b
    def circle_area(r):
        r = int(input('Введите радиус:'))
        return 3.14*r**2
    def square_area(a):
        a = int(input('Введите длину:'))
        return a**2
    def triangle_area(a, h):
        a = int(input('Введите основание:'))
        h = int(input('Введите высоту:'))
        return 0.5*a*h
    
    if shape == rectangle:
        return rectangle_area
    if shape == circle:
        return circle_area
    if shape == square:
        return square_area
    if shape == triangle:
        return triangle_area

result = choose_operation(2)
loh_function = choose_operation(4)

print(result(2), loh_function(3))
