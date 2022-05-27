class Checker:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def is_triangle(self):
        if self.x + self.y > self.z and self.x + self.z > self.y and self.y + self.z > self.x:
            return msg_ok
        else:
            return msg_err


msg_ok = 'Треугольник построить можно!'
msg_err = 'Из этих чисел треугольник собрать не получится...'


triangle1 = Checker(3, 4, 5)
assert triangle1.is_triangle() == msg_ok
print(triangle1.is_triangle())

triangle2 = Checker(77, 3, 4)
assert triangle2.is_triangle() == msg_err
print(triangle2.is_triangle())

triangle3 = Checker(77, 3, 101)
assert triangle3.is_triangle() == msg_err
print(triangle3.is_triangle())
