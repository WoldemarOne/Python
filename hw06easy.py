# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math


class Tripod:
    def __init__(self, ax, ay, bx, by, cx, cy):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        self.cx = cx
        self.cy = cy

    def new_per(self):
        self.ab = math.sqrt(((self.bx - self.ax) ** 2) + ((self.by - self.ay) ** 2))
        self.bc = math.sqrt(((self.cx - self.bx) ** 2) + ((self.cy - self.by) ** 2))
        self.ca = math.sqrt(((self.ax - self.cx) ** 2) + ((self.ay - self.cy) ** 2))
        self.per = self.ab + self.bc + self.ca
        return self.per

    def new_height(self):
        self.height = 2 / self.ab * math.sqrt(self.per / 2 * (self.per / 2 - self.ab) *
                                              (self.per / 2 - self.bc) *
                                              (self.per / 2 - self.ca))
        return self.height

    def new_square(self):
        self.square = (self.ab * self.height) / 2
        return self.square


tri = Tripod(2, 2, 4, 4, 6, 2)
print(tri.new_per())
print(tri.new_height())
print(tri.new_square())

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Fourpod:
    def __init__(self, ax, ay, bx, by, cx, cy, dx, dy):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        self.cx = cx
        self.cy = cy
        self.dx = dx
        self.dy = dy

    def proverka(self):
        self.ac = math.sqrt(((self.cx - self.ax) ** 2) + ((self.cy - self.ay) ** 2))
        self.bd = math.sqrt(((self.dx - self.bx) ** 2) + ((self.dy - self.by) ** 2))
        if self.ac == self.bd:
            return 'Трапеция равнобедренная'
        else:
            return 'Трапеция не прошла проверку'

    def dliny(self):
        self.ab = math.sqrt(((self.bx - self.ax) ** 2) + ((self.by - self.ay) ** 2))
        self.bc = math.sqrt(((self.cx - self.bx) ** 2) + ((self.cy - self.by) ** 2))
        self.cd = math.sqrt(((self.dx - self.cx) ** 2) + ((self.dy - self.cy) ** 2))
        self.da = math.sqrt(((self.ax - self.dx) ** 2) + ((self.ay - self.dy) ** 2))
        return self.ab, self.bc, self.cd, self.da

    def four_per(self):
        self.per_four = self.ab + self.bc + self.cd + self.da
        return self.per_four

    def ploschad(self):
        h = math.sqrt((self.ab ** 2 - (((self.da - self.bc) ** 2 + self.ab ** 2 -
                                       self.cd ** 2) / (2 * (self.da - self.bc))) ** 2))
        self.sq = (self.bc + self.da) * h / 2
        return self.sq


four = Fourpod(2, 2, 4, 4, 8, 4, 10, 2)
print(four.proverka())
print(four.dliny())
print(four.four_per())
print(four.ploschad())
