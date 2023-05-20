from math import pi

figure = str(input())

if figure == 'square':
    side_a = float(input())
    square_size = side_a * side_a
    print(f'{square_size:.3f}')
elif figure == 'rectangle':
    side_a = float(input())
    side_b = float(input())
    rectangle_size = side_a * side_b
    print(f'{rectangle_size:.3f}')
elif figure == 'circle':
    radius = float(input())
    circle_size = (radius ** 2) * pi
    print(f'{circle_size:.3f}')
elif figure == 'triangle':
    side_a = float(input())
    height_a = float(input())
    triangle_size = 1 / 2 * side_a * height_a
    print(f'{triangle_size:.3f}')
