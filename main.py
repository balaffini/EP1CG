import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_fan_blades():
    glBegin(GL_TRIANGLES)
    glVertex3f(0, 0, 0)
    glVertex3f(1, 0, 0)
    glVertex3f(0.5, 1, 0)
    glEnd()

def draw_fan():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glRotatef(1, 0, 0, 1)  # Rotaciona o ventilador

    # Desenha três pás do ventilador
    for _ in range(3):
        draw_fan_blades()
        glRotatef(120, 0, 0, 1)  # Próxima pá

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

        glRotatef(1, 0, 1, 0)  # Rotate the fan blades

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_fan()

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()