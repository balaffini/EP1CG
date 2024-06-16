import math
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

fan_rotation_angle = 0

def draw_fan_blades(precision, radius):
    glBegin(GL_POLYGON)
    glVertex3f(0, 0, 0)
    glVertex3f(1, 0.5, 0)
    glVertex3f(1, -0.5, 0)
    for i in range(precision):
        angle = 0.25 * math.pi * i / precision
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        glVertex3f(x, y, 0)
    glEnd()

def draw_fan_arm():
    glColor3fv((0, 1, 0))
    glBegin(GL_POLYGON)
    glVertex3f(0, 0, 0)
    glVertex3f(-1, -3, 0)
    glVertex3f(1, -3, 0)
    glEnd()


def draw_fan_blades_spinning():
    precision = 35
    radius = 1.1
    fan_blades_count = 4
    for _ in range(fan_blades_count):
        draw_fan_blades(precision, radius)
        glRotatef(360/fan_blades_count, 0, 0, 1)
    glColor3fv((0, 1, 1))
    glutSwapBuffers()
    # glRotatef(1, 0, 0, 1)
    # glRotatef(0.5, 0, 1, 0)

def draw_fan():
    global fan_rotation_angle
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glPushMatrix()
    glRotatef(fan_rotation_angle, 0, 0, 1)
    draw_fan_blades_spinning()
    glPopMatrix()

    precision = 35
    radius = 1.22
    glBegin(GL_LINE_LOOP)
    for i in range(precision):
        angle = 2 * math.pi * i / precision
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        glVertex3f(x, y, 0)
    glEnd()

    glPushMatrix()
    glRotatef(0.5, 1, 0, 0)
    draw_fan_arm()
    glPopMatrix()

    glutSwapBuffers()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        global fan_rotation_angle
        fan_rotation_angle += 1

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_fan()

        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
