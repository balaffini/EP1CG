import math
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

fan_blades_rotation_angle = 0
fan_body_rotation_angle = 0


def setup_lighting():
    glEnable(GL_LIGHTING)

    # Luz ambiente
    glEnable(GL_LIGHT0)
    ambient_light = [0.2, 0.2, 0.2, 1.0]
    glLightfv(GL_LIGHT0, GL_AMBIENT, ambient_light)

    # Luz direcional
    glEnable(GL_LIGHT1)
    directional_light = [0.5, 0.5, 0.5, 1.0]
    light_position1 = [0.0, 5.0, 5.0, 0.0]  # Direcional
    glLightfv(GL_LIGHT1, GL_DIFFUSE, directional_light)
    glLightfv(GL_LIGHT1, GL_POSITION, light_position1)

    # Luz de ponto
    glEnable(GL_LIGHT2)
    point_light = [0.5, 0.5, 0.5, 1.0]
    light_position2 = [2.0, 5.0, -2.0, 1.0]  # De ponto
    glLightfv(GL_LIGHT2, GL_DIFFUSE, point_light)
    glLightfv(GL_LIGHT2, GL_POSITION, light_position2)

    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)

    glShadeModel(GL_SMOOTH)  # Sombreamento de Gouraud
    glEnable(GL_DEPTH_TEST)


def draw_circle(precision, radius, mode, z):
    glBegin(mode)
    for i in range(precision):
        angle = 2 * math.pi * i / precision
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        glVertex3f(x, y, z)
    glEnd()


def draw_fan_arm():
    glColor3fv((0, .5, .5))
    glBegin(GL_POLYGON)
    glVertex3f(0, 0, 0)
    glVertex3f(0.7, -2, 0)
    glVertex3f(-0.7, -2, 0)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(0, 0, 0)
    glVertex3f(0.7, -2, -.6)
    glVertex3f(0.7, -2, 0)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(0, 0, 0)
    glVertex3f(0.7, -2, -.6)
    glVertex3f(-0.7, -2, -.6)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(0, 0, 0)
    glVertex3f(-0.7, -2, 0)
    glVertex3f(-0.7, -2, -.6)
    glEnd()


def draw_fan_base():
    glColor3fv((1, 1, 1))
    glBegin(GL_POLYGON)
    glVertex3f(-1, -2, -1)
    glVertex3f(1, -2, -1)
    glVertex3f(1, -2.65, -1)
    glVertex3f(-1, -2.65, -1)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(-1, -2, .5)
    glVertex3f(1, -2, .5)
    glVertex3f(1, -2.65, .5)
    glVertex3f(-1, -2.65, .5)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(1, -2, -1)
    glVertex3f(1, -2, .5)
    glVertex3f(-1, -2, .5)
    glVertex3f(-1, -2, -1)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(-1, -2, -1)
    glVertex3f(-1, -2, .5)
    glVertex3f(-1, -2.65, .5)
    glVertex3f(-1, -2.65, -1)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(1, -2, -1)
    glVertex3f(1, -2, .5)
    glVertex3f(1, -2.65, .5)
    glVertex3f(1, -2.65, -1)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(1, -2.65, -1)
    glVertex3f(1, -2.65, .5)
    glVertex3f(-1, -2.65, .5)
    glVertex3f(-1, -2.65, -1)
    glEnd()


def draw_fan_blade(precision, radius):
    glBegin(GL_POLYGON)
    glVertex3f(0, 0, .3)
    glVertex3f(1, 0.5, .1)
    glVertex3f(1, -0.5, .3)
    for i in range(precision):
        angle = 0.20 * math.pi * i / precision
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        glVertex3f(x, y, .1)
    glEnd()


def draw_fan_blades_spinning():
    precision = 35
    radius = 1.1
    fan_blades_count = 4
    glColor3fv((0, 1, 1))
    for _ in range(fan_blades_count):
        draw_fan_blade(precision, radius)
        glRotatef(360 / fan_blades_count, 0, 0, 1)
    glutSwapBuffers()


def draw_blades_protection():
    glColor3fv((1, 0, 1))
    outer_radius = 1.22
    inner_radius = 0.3
    inner_z = 0.43
    outer_z = .3
    draw_circle(35, inner_radius, GL_POLYGON, inner_z)
    draw_circle(35, outer_radius, GL_LINE_LOOP, .1)
    draw_circle(35, outer_radius, GL_LINE_LOOP, .2)
    draw_circle(35, outer_radius, GL_LINE_LOOP, .3)
    glBegin(GL_LINES)
    lines = 15
    for i in range(lines):
        angle = 2 * math.pi * i / lines
        x = outer_radius * math.cos(angle)
        y = outer_radius * math.sin(angle)
        glVertex3f(0, 0, inner_z)
        glVertex3f(x, y, outer_z)
    for i in range(lines):
        angle = 2 * math.pi * i / lines
        x = outer_radius * math.cos(angle)
        y = outer_radius * math.sin(angle)
        glVertex3f(x, y, .1)
        glVertex3f(x, y, .3)
    glEnd()


def draw_blade_holder():
    width = .04
    glColor3fv((1, 1, 1))
    glBegin(GL_POLYGON)
    glVertex3f(-width, -width, 0)
    glVertex3f(-width, -width, 0.43)
    glVertex3f(width, -width, 0.43)
    glVertex3f(width, -width, 0)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(width, width, 0)
    glVertex3f(width, width, 0.43)
    glVertex3f(-width, width, 0.43)
    glVertex3f(-width, width, 0)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(-width, -width, 0)
    glVertex3f(-width, -width, 0.43)
    glVertex3f(-width, width, 0.43)
    glVertex3f(-width, width, 0)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(width, width, 0)
    glVertex3f(width, width, 0.43)
    glVertex3f(width, -width, 0.43)
    glVertex3f(width, -width, 0)
    glEnd()


def draw_blades_back_protection():
    glBegin(GL_LINES)
    lines = 15
    outer_radius = 1.22
    inner_z = 0
    outer_z = 0.1
    for i in range(lines):
        angle = 2 * math.pi * i / lines
        x = outer_radius * math.cos(angle)
        y = outer_radius * math.sin(angle)
        glVertex3f(0, 0, -inner_z)
        glVertex3f(x, y, outer_z)
    glEnd()
    draw_blade_holder()


def draw_fan():
    global fan_blades_rotation_angle
    global fan_body_rotation_angle

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glPushMatrix()
    draw_fan_base()
    glPopMatrix()

    glPushMatrix()
    draw_fan_arm()
    glPopMatrix()

    glPushMatrix()
    glRotatef(fan_body_rotation_angle, 0, 1, 0)

    glPushMatrix()
    draw_blades_back_protection()
    glPopMatrix()

    glPushMatrix()
    glRotatef(fan_blades_rotation_angle, 0, 0, 1)
    draw_fan_blades_spinning()
    glPopMatrix()

    glPushMatrix()
    draw_blades_protection()
    glPopMatrix()
    glPopMatrix()

    glutSwapBuffers()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0, 1, -6)
    glRotatef(10, 40, -200, 0)

    setup_lighting()  # Configura a iluminação

    blades_velocity = 0

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
                if event.key == pygame.K_0:
                    blades_velocity = 0
                if event.key == pygame.K_1:
                    blades_velocity = 1
                if event.key == pygame.K_2:
                    blades_velocity = 2
                if event.key == pygame.K_3:
                    blades_velocity = 3
                if event.key == pygame.K_4:
                    blades_velocity = 4
                if event.key == pygame.K_8:
                    blades_velocity = 25
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0, 0, 0.2)
                if event.button == 5:
                    glTranslatef(0, 0, -0.2)

            mouse_move = pygame.mouse.get_rel()
            glRotatef(mouse_move[0] * 0.1, 0.0, 1.0, 0.0)

        global fan_blades_rotation_angle
        fan_blades_rotation_angle -= blades_velocity

        global fan_body_rotation_angle
        is_in_angle = fan_body_rotation_angle < 60 if crescendo else fan_body_rotation_angle > -60

        if blades_velocity != 0:
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
