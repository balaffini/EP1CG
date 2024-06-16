import math
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

fan_blades_rotation_angle = 0
fan_body_rotation_angle = 0


def draw_fan_blade(precision, radius):
    glBegin(GL_POLYGON)
    glVertex3f(0, 0, 0)
    glVertex3f(1, 0.5, -.2)
    glVertex3f(1, -0.5, 0)
    for i in range(precision):
        angle = 0.20 * math.pi * i / precision
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        glVertex3f(x, y, -.2)
    glEnd()


def draw_fan_arm():
    glColor3fv((1, 1, 1))
    # glTranslatef(0, 0, -2)
    glBegin(GL_POLYGON)
    glVertex3f(0, 0, 0)
    glVertex3f(-1, -2, 0)
    glVertex3f(1, -2, 0)
    glEnd()

def draw_fan_base():
    glColor3fv((1, 1, 1))
    glBegin(GL_POLYGON)
    glVertex3f(-2, -2, -1)
    glVertex3f(2, -2, -1)
    glVertex3f(2, -3, -1)
    glVertex3f(-2, -3, -1)
    glEnd()


def draw_fan_blades_spinning():
    precision = 35
    radius = 1.1
    fan_blades_count = 4
    glColor3fv((0, 1, 1))
    for _ in range(fan_blades_count):
        draw_fan_blade(precision, radius)
        glRotatef(360 / fan_blades_count, 0, 0, 1)
    glColor3fv((0, 1, 1))
    glutSwapBuffers()
    # glRotatef(1, 0, 0, 1)
    # glRotatef(0.5, 0, 1, 0)


def draw_blades_protection():
    glColor3fv((1, 0, 1))
    # glRotatef(fan_body_rotation_angle, 0, 1, 0)
    draw_circle(35, 1.22, GL_LINE_LOOP)
    draw_circle(35, 0.3, GL_POLYGON)



def draw_circle(precision, radius, mode):
    glBegin(mode)
    for i in range(precision):
        angle = 2 * math.pi * i / precision
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        glVertex3f(x, y, 0)
    glEnd()

def draw_fan():
    global fan_blades_rotation_angle
    global fan_body_rotation_angle

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glPushMatrix()
    glRotatef(fan_body_rotation_angle, 0, 1, 0)

    glPushMatrix()
    glRotatef(fan_blades_rotation_angle, 0, 0, 1)
    # glRotatef(fan_body_rotation_angle, 0, 1, 0)
    draw_fan_blades_spinning()
    glPopMatrix()

    glPushMatrix()
    draw_blades_protection()
    glPopMatrix()
    glPopMatrix()

    glPushMatrix()
    draw_fan_arm()
    glPopMatrix()

    draw_fan_base()

    glutSwapBuffers()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    crescendo = True
    rotation = 0.6

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    glTranslatef(-0.2, 0, 0)
                if event.key == pygame.K_LEFT:
                    glTranslatef(0.2, 0, 0)
                if event.key == pygame.K_UP:
                    glTranslatef(0, -0.2, 0)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0, 0.2, 0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0, 0, 0.2)
                if event.button == 5:
                    glTranslatef(0, 0, -0.2)

        global fan_blades_rotation_angle
        fan_blades_rotation_angle += 1

        global fan_body_rotation_angle
        is_in_angle = fan_body_rotation_angle < 120 if crescendo else fan_body_rotation_angle > 0

        if is_in_angle:
            fan_body_rotation_angle += rotation
        else:
            rotation = -rotation
            crescendo = not crescendo

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_fan()

        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
