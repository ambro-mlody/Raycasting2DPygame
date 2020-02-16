import Ray
import pygame as py
import math as m


class Particle:
    def __init__(self, startx, starty):
        self.position = (startx, starty)
        self.rays = []
        for i in range(360):
            self.rays.append(Ray.Ray(self.position, i))

    def show(self, window):
        py.draw.circle(window, (255, 255, 255), self.position, 4, 1)
        for r in self.rays:
            r.show(window)

    def look(self, walls, window):
        result = ()
        for r in self.rays:
            closest = m.inf
            best_point = ()
            for w in walls:
                result = r.cast(w)
                if result and result[0]:
                    d = m.hypot(result[1][1] - self.position[1], result[1][0] - self.position[0])
                    if d < closest:
                        closest = d
                        best_point = result[1]

            if closest != m.inf:
                py.draw.line(window, (255, 255, 255, 100), self.position, best_point, 1)

    def update(self, pos):
        self.position = pos
        self.rays.clear()
        for i in range(360):
            self.rays.append(Ray.Ray(self.position, i))