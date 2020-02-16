import pygame as py
import sys
import random as rand
import Boundary as bond
import Particle as part


py.init()
size = (800, 600)
window = py.display.set_mode(size)
py.display.set_caption("Raycasting2D")

walls = []
for i in range(5):
    x1 = rand.randint(0, size[0])
    y1 = rand.randint(0, size[1])
    x2 = rand.randint(0, size[0])
    y2 = rand.randint(0, size[1])
    walls.append(bond.Boundary(x1, y1, x2, y2))

walls.append(bond.Boundary(0, 0, 0, size[1]))
walls.append(bond.Boundary(0, 0, size[0], 0))
walls.append(bond.Boundary(0, size[1] - 1, size[0], size[1] - 1))
walls.append(bond.Boundary(size[0] - 1, 0, size[0] - 1, size[1]))

particle = part.Particle(int(size[0] / 2), int(size[1] / 2))

while True:
    window.fill((0, 0, 0))

    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()

    pos = py.mouse.get_pos()
    particle.update(pos)

    particle.show(window)
    for w in walls:
        w.show(window)

    particle.look(walls, window)
    py.display.update()
