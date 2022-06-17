from math import *

import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *


def init():
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glClearColor(0.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)


def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 1.0, 0.0)

    glBegin(GL_POINTS)

    glVertex2f(0.0, 0.0)

    glEnd()
    glFlush()
def circle(x, y, r):

    glBegin(GL_POLYGON)

    for i in range(0, 200):

        pi = 3.1416
        A = (i*2*pi)/25
        x1 = x+ ((r-0.03)* cos(A))
        y1 = y + ((r)*sin(A))
        glVertex2f(x1, y1)
    glEnd()

def sky():
    glColor3f(0.110, 0.565, 1.000)
    glBegin(GL_QUADS)
    glVertex2f(-1.0, 0.2)
    glVertex2f(-1.0, 1.0)
    glVertex2f(1.0, 1.0)
    glVertex2f(1.0, 0.2)
    glEnd()

def field():
    glColor3f(0.420, 0.557, 0.137)
    glBegin(GL_QUADS)
    glVertex2f(-1.0, 0.2)
    glVertex2f(-1.0, -0.5)
    glVertex2f(1.0, -1.0)
    glVertex2f(1.0, 0.2)
    glEnd()
def river():
    glColor3f(0.255, 0.412, 0.882)
    glBegin(GL_QUADS)
    glVertex2f(-1.0, -1.0)
    glVertex2f(-1.0, -0.5)
    glVertex2f(1.0, -0.1)
    glVertex2f(1.0, -1.0)
    glEnd()

def hill():
    glColor3f(0.627, 0.322, 0.176)
    glBegin(GL_POLYGON)
    glVertex2f(-0.20, 0.20)
    glVertex2f(0.03, 0.50)
    glVertex2f(0.20, 0.20)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(-0.05, 0.20)
    glVertex2f(-0.38, 0.45)
    glVertex2f(-0.60, 0.20)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(-0.90, 0.20)
    glVertex2f(-0.65, 0.38)
    glVertex2f(-0.50, 0.20)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(-1.3, 0.20)
    glVertex2f(-0.98, 0.35)
    glVertex2f(-0.90, 0.40)
    glVertex2f(-0.75, 0.20)


    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.56, 0.20)
    glVertex2f(0.38, 0.45)
    glVertex2f(0.10, 0.20)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.82, 0.20)
    glVertex2f(0.67, 0.40)
    glVertex2f(0.43, 0.20)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(1.3, 0.20)
    glVertex2f(0.89, 0.40)
    glVertex2f(0.71, 0.20)
    glEnd()
def sun():
    glColor3f(1.000, 0.843, 0.000)
    circle(-0.25, 0.75,0.18)

def moon():
    glPushMatrix()
    glColor3f(1.0, 1.0, 1.0)
    circle(0.75, 0.75, 0.18)
    glPopMatrix()

def cloud1():
    glColor3f(0.80, 0.80, 0.80)
    circle(-0.85, 0.77, 0.15)
    circle(-0.79, 0.70, 0.15)
    circle(-0.70, 0.70, 0.15)
    circle(-0.75, 0.77, 0.15)

def cloud2():
    glColor3f(0.80, 0.80, 0.80)
    circle(0.35, 0.77, 0.15)
    circle(0.45, 0.70, 0.15)
    circle(0.55, 0.75, 0.15)
    circle(0.45, 0.80, 0.15)

def tree1():
    glColor3f(0.38, 0.19, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(-0.25, -0.30)
    glVertex2f(-0.25, -0.12)
    glVertex2f(-0.27, -0.12)
    glVertex2f(-0.27, -0.30)
    glEnd()

    glColor3f(0.0, 0.43, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(-0.36, -0.12)
    glVertex2f(-0.26, 0.12)
    glVertex2f(-0.16, -0.12)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(-0.36, -0.04)
    glVertex2f(-0.26, 0.20)
    glVertex2f(-0.16, -0.04)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(-0.36, 0.04)
    glVertex2f(-0.26, 0.28)
    glVertex2f(-0.16, 0.04)
    glEnd()



def tree2():
    glColor3f(0.38, 0.19, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(-0.05, -0.20)
    glVertex2f(-0.05, 0.00)
    glVertex2f(-0.07, 0.00)
    glVertex2f(-0.07, -0.20)
    glEnd()

    glColor3f(0.0, 0.43, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(-0.18, 0.00)
    glVertex2f(-0.06, 0.24)
    glVertex2f(0.06, 0.00)
    glEnd()


    glBegin(GL_POLYGON)
    glVertex2f(-0.18, 0.08)
    glVertex2f(-0.06, 0.32)
    glVertex2f(0.06, 0.08)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(-0.18, 0.16)
    glVertex2f(-0.06, 0.40)
    glVertex2f(0.06, 0.16)
    glEnd()


def main():
    init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        sky()
        river()
        field()
        hill()
        sun()
        cloud1()
        cloud2()
        tree1()
        tree2()

        pygame.display.flip()

        pygame.time.wait(10)

main()