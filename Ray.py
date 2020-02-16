import math as m
import pygame as py


class Ray:
    def __init__(self, pos, angle):
        self.position = pos
        self.direction = (m.cos(m.radians(angle)), m.sin(m.radians(angle)))
        # dir = (m.cos(m.radians(angle)), m.sin(m.radians(angle)))
        # d = m.dist(dir[0], dir[1])
        # self.direction = (dir[0] / d, dir[1] / d)

    def show(self, window):
        x2 = self.position[0] + self.direction[0] * 4
        y2 = self.position[1] + self.direction[1] * 4
        py.draw.line(window, (255, 255, 255, 100), self.position, (x2, y2), 1)

    def cast(self, wall):
        x1 = wall.a[0]
        y1 = wall.a[1]
        x2 = wall.b[0]
        y2 = wall.b[1]

        x3 = self.position[0]
        y3 = self.position[1]
        x4 = self.position[0] + self.direction[0]
        y4 = self.position[1] + self.direction[1]

        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if den == 0:
            return False

        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den

        if 0 < t < 1 and u > 0:
            point = (x1 + t * (x2 - x1), y1 + t * (y2 - y1))
            return True, point

        return

    def look_at(self, x, y):
        dir = (x, y)
        d = m.dist(self.position, dir)
        self.direction = ((x - self.position[0]) / d, (y - self.position[1]) / d)