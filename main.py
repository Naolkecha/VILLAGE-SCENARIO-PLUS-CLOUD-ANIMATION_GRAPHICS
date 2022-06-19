import pygame
import pyrr
from OpenGL.GL import *
from pygame.locals import *
from OpenGL.GL.shaders import *
import numpy as np
import os
from objloader import OBJ

class Object:
    def getFileContents(filename):
        p = os.path.join(os.getcwd(), "shaders", filename)
        return open(p, 'r').read()

    def __init__(self):
        global VBO, program, texture,indices,cube_faces
        pygame.init()
        display = (500, 500)
        pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
        glClearColor(.30, 0.20, 0.20, 1.0)
        glViewport(0, 0, 500, 500)

        vertexShader = compileShader(self.getFileContents("vertex.shader"), GL_VERTEX_SHADER)
        fragmentShader = compileShader(self.getFileContents("fragment.shader"), GL_FRAGMENT_SHADER)

        program = glCreateProgram()
        glAttachShader(program, vertexShader)
        glAttachShader(program, fragmentShader)
        glLinkProgram(program)
        glEnable(GL_DEPTH_TEST)



        obj = OBJ("model/VillageUnity.obj")
        tex = obj.loadTexture("model/historyvillage.png")
        vertices = obj.vertices
        self.vertex_count = len(self.vertices)

        self.vertices = np.array(self.vertices, dtype=np.float)

        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)

        self.vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(0))
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(12))

        # cameras matrix
        projection_transform = pyrr.matrix44.create_perspective_projection(
            fovy=45, aspect=640 / 480,
            near=0.1, far=10, dtype=np.float32
        )
        glUniformMatrix4fv(
            glGetUniformLocation(vertexShader, "projection"),
            1, GL_FALSE, projection_transform
        )
        modelMatrixLocation = glGetUniformLocation(vertexShader, "model")
        self.main()



    def main(self):
        running = True
        while (running):
            # check events
            for event in pygame.event.get():
                if (event.type == QUIT):
                    running = False

            # refresh screen
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glUseProgram(self.vertexShader)
            glUseProgram(self.fragmentShader)


            glUniformMatrix4fv(self.modelMatrixLocation, 1, GL_FALSE, self.model_transform)



            glBindVertexArray(self.vao)
            glDrawArrays(GL_TRIANGLES, 0, self.vertex_count)

            pygame.display.flip()

            # display.flip()

            # # timing
            # .clock.tick(60)
            # self.quit()
            # box = OBJ('./model/seoul_v2.obj')
            # #
            # glPushMatrix()
            # glTranslatef(2, 3, 4)
            # box.render()
            # glPopMatrix()
            # pygame.display.flip()
            # pygame.time.wait(10)
myApp = Object()


