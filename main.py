import math
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

fan_blades_rotation_angle = 0
fan_body_rotation_angle = 0
blades_velocity = 0


def draw_circle(precision, radius, mode, z, y_offset=0.0):
    glBegin(mode)
    for i in range(precision):
        angle = 2 * math.pi * i / precision
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        glVertex3f(x, y + y_offset, z)
    glEnd()


def draw_fan_arm():
    glColor3fv((1, 1, 1))
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

    glBegin(GL_LINES)
    glColor3fv((0, 0, 0))
    glVertex3f(0, 0, 0)
    glVertex3f(-0.7, -2, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(-0.7, -2, -.6)
    glVertex3f(-0.7, -2, 0)
    glVertex3f(-0.7, -2, -.6)

    glVertex3f(0, 0, 0)
    glVertex3f(0.7, -2, -.6)
    glVertex3f(0, 0, 0)
    glVertex3f(-0.7, -2, -.6)
    glVertex3f(0.7, -2, -.6)
    glVertex3f(-0.7, -2, -.6)

    glVertex3f(0, 0, 0)
    glVertex3f(0.7, -2, -.6)
    glVertex3f(0, 0, 0)
    glVertex3f(0.7, -2, 0)
    glVertex3f(0.7, -2, -.6)
    glVertex3f(0.7, -2, 0)

    glVertex3f(0, 0, 0)
    glVertex3f(0.7, -2, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(-0.7, -2, 0)
    glVertex3f(0.7, -2, 0)
    glVertex3f(-0.7, -2, 0)
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
    glBegin(GL_LINES)
    glColor3fv((0, 0, 0))
    glVertex3f(-1, -2, -1)
    glVertex3f(1, -2, -1)

    glVertex3f(1, -2.65, -1)
    glVertex3f(-1, -2.65, -1)

    glVertex3f(-1, -2, .5)
    glVertex3f(1, -2, .5)

    glVertex3f(1, -2.65, .5)
    glVertex3f(-1, -2.65, .5)

    glVertex3f(1, -2.65, .5)
    glVertex3f(1, -2, .5)

    glVertex3f(1, -2.65, -1)
    glVertex3f(1, -2, -1)

    glVertex3f(-1, -2.65, .5)
    glVertex3f(-1, -2, .5)

    glVertex3f(-1, -2.65, -1)
    glVertex3f(-1, -2, -1)

    glVertex3f(1, -2, -1)
    glVertex3f(1, -2, .5)

    glVertex3f(-1, -2, .5)
    glVertex3f(-1, -2, -1)

    glVertex3f(-1, -2, -1)
    glVertex3f(-1, -2, .5)

    glVertex3f(-1, -2.65, .5)
    glVertex3f(-1, -2.65, -1)

    glVertex3f(1, -2, -1)
    glVertex3f(1, -2, .5)

    glVertex3f(1, -2.65, .5)
    glVertex3f(1, -2.65, -1)

    glVertex3f(1, -2.65, -1)
    glVertex3f(1, -2.65, .5)

    glVertex3f(-1, -2.65, .5)
    glVertex3f(-1, -2.65, -1)
    glEnd()
    draw_knob()


def draw_knob():
    radius = 0.15
    glColor3fv((0, 0, 0))
    draw_circle(25, radius, GL_LINE_LOOP, .55, -2.3)
    draw_circle(25, radius, GL_LINE_LOOP, .5, -2.3)
    lines = 20
    glBegin(GL_LINES)
    for i in range(lines):
        angle = 2 * math.pi * i / lines
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        glVertex3f(x, y - 2.3, .55)
        glVertex3f(x, y - 2.3, .5)
    glEnd()
    glColor3fv((1, 1, 1))
    draw_circle(25, radius, GL_POLYGON, .55, -2.3)
    global blades_velocity
    glBegin(GL_LINES)
    glColor3fv((0, 0, 0))
    x = -0.02 - radius / 2 * math.cos(blades_velocity * .6)
    y = 0.02 + radius / 2 * math.sin(blades_velocity * .6)
    glVertex3f(x, y - 2.3, .55)
    glVertex3f(0, -2.3, .55)
    glEnd()


def draw_motor():
    radius = 0.25
    precision = 35
    circle_pts = []
    inner_z = 0
    outer_z = -.5
    for i in range(int(precision) + 1):
        angle = 2 * math.pi * (i / precision)
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        pt = (x, y)
        circle_pts.append(pt)
    glBegin(GL_TRIANGLE_STRIP)
    glColor(1, 1, 1)
    for (x, y) in circle_pts:
        glVertex(x, y, inner_z)
        glVertex(x, y, outer_z)
    glEnd()
    draw_circle(precision, radius, GL_POLYGON, outer_z)
    draw_circle(precision, radius, GL_POLYGON, inner_z)
    glBegin(GL_POLYGON)
    glColor(0, 0, 0)
    glVertex(.15, -.16, inner_z)
    glVertex(.1, .16, inner_z)
    glVertex(.13, .16, inner_z)
    glVertex(.18, -.16, inner_z)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex(.02, -.16, inner_z)
    glVertex(-.04, .16, inner_z)
    glVertex(0, .16, inner_z)
    glVertex(.06, -.16, inner_z)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex(-.1, -.16, inner_z)
    glVertex(-.15, .16, inner_z)
    glVertex(-.18, .16, inner_z)
    glVertex(-.13, -.16, inner_z)
    glEnd()
    draw_circle(precision, radius, GL_LINE_LOOP, inner_z)
    draw_circle(precision, radius, GL_LINE_LOOP, outer_z)
    lines = 5
    glBegin(GL_LINES)
    for i in range(lines):
        angle = 2 * math.pi * i / lines
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        glVertex3f(x, y, inner_z)
        glVertex3f(x, y, outer_z / 2)
        glVertex3f(x, y, outer_z / 2 - .05)
        glVertex3f(x, y, outer_z)
    glEnd()


def draw_fan_blade(precision):
    glBegin(GL_POLYGON)
    glColor3fv((1, 1, 1))
    glVertex3f(0, 0, .3)
    glVertex3f(.9, 0.5, .1)
    glVertex3f(.9, -0.5, .3)
    glEnd()

    glBegin(GL_POLYGON)
    z = .3
    x_radius = .5
    y_radius = .25
    offset = .9
    size = 18
    for i in range(size):
        angle = 2 * math.pi * i / (precision - 1)
        x = x_radius * math.cos(angle)
        y = y_radius * math.sin(angle)
        glVertex3f(x, y + offset, z)
        z -= .2 / (size - 1)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3fv((0, 0, 0))
    glVertex3f(0, 0, .3)
    glVertex3f(.9, 0.5, .1)
    glVertex3f(0, 0, .3)
    glVertex3f(.9, -0.5, .3)
    glEnd()
    glBegin(GL_LINE_STRIP)
    z = .3
    for i in range(size):
        angle = 2 * math.pi * i / (precision - 1)
        x = x_radius * math.cos(angle)
        y = y_radius * math.sin(angle)
        glVertex3f(x, y + offset, z)
        z -= .2 / (size - 1)
    glEnd()


def draw_fan_blades_spinning():
    precision = 35
    fan_blades_count = 4
    for _ in range(fan_blades_count):
        draw_fan_blade(precision)
        glRotatef(360 / fan_blades_count, 0, 0, 1)
    glutSwapBuffers()


def draw_blades_protection():
    outer_radius = 1.22
    inner_radius = 0.3
    inner_z = 0.43
    outer_z = .3
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
    glColor3fv((1, 1, 1))
    draw_circle(35, inner_radius, GL_POLYGON, inner_z)
    glColor3fv((0, 0, 0))
    draw_circle(35, inner_radius, GL_LINE_LOOP, inner_z)


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
    glBegin(GL_LINES)
    glColor3fv((0, 0, 0))
    glVertex3f(-width, -width, 0)
    glVertex3f(-width, -width, 0.43)
    glVertex3f(width, -width, 0.43)
    glVertex3f(width, -width, 0)
    glVertex3f(width, width, 0)
    glVertex3f(width, width, 0.43)
    glVertex3f(-width, width, 0.43)
    glVertex3f(-width, width, 0)
    glVertex3f(-width, -width, 0)
    glVertex3f(-width, -width, 0.43)
    glVertex3f(-width, width, 0.43)
    glVertex3f(-width, width, 0)
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

    draw_room()

    glPushMatrix()
    draw_fan_base()
    glPopMatrix()

    glPushMatrix()
    draw_fan_arm()
    glPopMatrix()

    glPushMatrix()
    draw_motor()
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


def draw_room():
    glColor3f(0.9, 0.9, 0.9)
    glBegin(GL_QUADS)
    # Floor
    glVertex3f(-5, -2.65, 5)
    glVertex3f(5, -2.65, 5)
    glVertex3f(5, -2.65, -5)
    glVertex3f(-5, -2.65, -5)

    # Ceiling
    glVertex3f(-5, 5, 5)
    glVertex3f(5, 5, 5)
    glVertex3f(5, 5, -5)
    glVertex3f(-5, 5, -5)

    # Back wall
    glVertex3f(-5, -2.65, -5)
    glVertex3f(5, -2.65, -5)
    glVertex3f(5, 5, -5)
    glVertex3f(-5, 5, -5)

    # Left wall
    glVertex3f(-5, -2.65, 5)
    glVertex3f(-5, -2.65, -5)
    glVertex3f(-5, 5, -5)
    glVertex3f(-5, 5, 5)

    # Right wall
    glVertex3f(5, -2.65, 5)
    glVertex3f(5, -2.65, -5)
    glVertex3f(5, 5, -5)
    glVertex3f(5, 5, 5)
    glEnd()

    glBegin(GL_LINES)
    glColor3f(0, 0, 0)
    # Floor
    glVertex3f(-5, -2.65, 5)
    glVertex3f(5, -2.65, 5)

    glVertex3f(5, -2.65, -5)
    glVertex3f(-5, -2.65, -5)

    glVertex3f(-5, 5, -5)
    glVertex3f(-5, -2.65, -5)

    glVertex3f(5, 5, 5)
    glVertex3f(5, -2.65, 5)

    glVertex3f(5, 5, -5)
    glVertex3f(5, -2.65, -5)

    glVertex3f(-5, 5, 5)
    glVertex3f(-5, -2.65, 5)

    glVertex3f(-5, 5, 5)
    glVertex3f(-5, -2.65, 5)

    glVertex3f(-5, 5, 5)
    glVertex3f(5, 5, 5)

    glVertex3f(5, 5, -5)
    glVertex3f(-5, 5, -5)

    glVertex3f(-5, -2.65, -5)
    glVertex3f(5, -2.65, -5)

    glVertex3f(5, 5, -5)
    glVertex3f(-5, 5, -5)

    glVertex3f(-5, -2.65, 5)
    glVertex3f(-5, -2.65, -5)

    glVertex3f(-5, 5, -5)
    glVertex3f(-5, 5, 5)

    glVertex3f(5, -2.65, 5)
    glVertex3f(5, -2.65, -5)

    glVertex3f(5, 5, -5)
    glVertex3f(5, 5, 5)
    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    glClearColor(0.7, 0.7, 0.7, 1)
    glClear(GL_COLOR_BUFFER_BIT)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0, 1, -6)
    glRotatef(10, 40, -200, 0)

    global blades_velocity

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
            glRotatef(mouse_move[1] * 0.1, 1.0, 0.0, 0.0)

        global fan_blades_rotation_angle
        fan_blades_rotation_angle -= blades_velocity * 5

        global fan_body_rotation_angle
        is_in_angle = fan_body_rotation_angle < 60 if crescendo else fan_body_rotation_angle > -60

        if blades_velocity != 0:
            if is_in_angle:
                fan_body_rotation_angle += rotation
            else:
                rotation = -rotation
                crescendo = not crescendo

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glPushMatrix()
        draw_fan()
        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
