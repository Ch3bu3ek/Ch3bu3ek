import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

# Определение вершин и рёбер куба
vertices = [
    [1, 1, -1],
    [1, -1, -1],
    [-1, -1, -1],
    [-1, 1, -1],
    [1, 1, 1],
    [1, -1, 1],
    [-1, -1, 1],
    [-1, 1, 1]
]

edges = [
    [0, 1],
    [1, 2],
    [2, 3],
    [3, 0],
    [4, 5],
    [5, 6],
    [6, 7],
    [7, 4],
    [0, 4],
    [1, 5],
    [2, 6],
    [3, 7]
]

def draw_cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def draw_high_poly_cube():
    step = 0.2
    for x in range(-5, 6):
        for y in range(-5, 6):
            for z in range(-5, 6):
                glBegin(GL_QUADS)
                glVertex3f(x * step, y * step, z * step)
                glVertex3f(x * step + step, y * step, z * step)
                glVertex3f(x * step + step, y * step + step, z * step)
                glVertex3f(x * step, y * step + step, z * step)
                glEnd()

def draw_cubes(num_cubes):
    for i in range(num_cubes):
        glPushMatrix()
        glTranslatef(i % 5, (i // 5) % 5, -((i // 25) % 5) * 2)
        draw_high_poly_cube()
        glPopMatrix()


def setup_lighting():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, [1, 1, 1, 0])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1, 1, 1, 1])
    glLightfv(GL_LIGHT0, GL_SPECULAR, [1, 1, 1, 1])
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -20)

    clock = pygame.time.Clock()

    num_cubes = 50  # Увеличь количество кубов для большей нагрузки

    setup_lighting()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_cubes(num_cubes)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
