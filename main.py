import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '400,200'
import pygame
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import pyrr
from loadOBJ import ObjLoader
from texture_loader import *
from camera import Camera

# CAMERA settings
cam = Camera()
WIDTH, HEIGHT = 700, 700
lastX, lastY = WIDTH / 2, HEIGHT / 2
first_mouse = True


vertex_src = """
# version 330

layout(location = 0) in vec3 a_position;
layout(location = 1) in vec2 a_texture;
layout(location = 2) in vec3 a_normal;

uniform mat4 model;
uniform mat4 projection;
uniform mat4 view;

out vec2 v_texture;

void main()
{
    gl_Position = projection * view * model * vec4(a_position, 1.0);
    v_texture = a_texture;
}
"""

fragment_src = """
# version 330

in vec2 v_texture;

out vec4 out_color;

uniform sampler2D s_texture;

void main()
{
    out_color = texture(s_texture, v_texture);
}
"""


def mouse_look(xpos, ypos):
    global first_mouse, lastX, lastY

    if first_mouse:
        lastX = xpos
        lastY = ypos
        first_mouse = False

    xoffset = xpos - lastX
    yoffset = lastY - ypos

    lastX = xpos
    lastY = ypos

    cam.process_mouse_movement(xoffset, yoffset)


pygame.init()
pygame.display.set_mode((WIDTH, HEIGHT), pygame.OPENGL | pygame.DOUBLEBUF | pygame.RESIZABLE) # |pygame.FULLSCREEN
pygame.mouse.set_visible(False)
pygame.event.set_grab(True)

# load here the 3d meshes

village_indices, village_buffer = ObjLoader.load_model("model/VillageUnity1.obj")

shader = compileProgram(compileShader(vertex_src, GL_VERTEX_SHADER), compileShader(fragment_src, GL_FRAGMENT_SHADER))

# VAO and VBO
VAO = glGenVertexArrays(1)
VBO = glGenBuffers(1)
EBO = glGenBuffers(1)

glBindVertexArray(VBO)
# village Vertex Buffer Object
glBindBuffer(GL_ARRAY_BUFFER, VBO)
glBufferData(GL_ARRAY_BUFFER, village_buffer.nbytes, village_buffer, GL_STATIC_DRAW)

# village vertices
glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, village_buffer.itemsize * 8, ctypes.c_void_p(0))
# village textures
glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, village_buffer.itemsize * 8, ctypes.c_void_p(12))
# village normals
glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, village_buffer.itemsize * 8, ctypes.c_void_p(20))
glEnableVertexAttribArray(2)


textures = glGenTextures(1)
# load_textures
load_texture_pygame("model/historyvillagetex.png", textures)


glUseProgram(shader)
glClearColor(0, 0.1, 0.1, 1)
glEnable(GL_DEPTH_TEST)
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

projection = pyrr.matrix44.create_perspective_projection_matrix(45, 1280 / 720, 0.1, 100)
village_pos = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, 0, 0]))


model_loc = glGetUniformLocation(shader, "model")
proj_loc = glGetUniformLocation(shader, "projection")
view_loc = glGetUniformLocation(shader, "view")

glUniformMatrix4fv(proj_loc, 1, GL_FALSE, projection)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif  event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

        if event.type == pygame.VIDEORESIZE:
            glViewport(0, 0, event.w, event.h)
            projection = pyrr.matrix44.create_perspective_projection_matrix(45, event.w / event.h, 0.1, 100)
            glUniformMatrix4fv(proj_loc, 1, GL_FALSE, projection)

    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_a]:
        cam.process_keyboard("LEFT", 0.08)
    if keys_pressed[pygame.K_d]:
        cam.process_keyboard("RIGHT", 0.08)
    if keys_pressed[pygame.K_w]:
        cam.process_keyboard("FORWARD", 0.08)
    if keys_pressed[pygame.K_s]:
        cam.process_keyboard("BACKWARD", 0.08)


    mouse_pos = pygame.mouse.get_pos()
    mouse_look(mouse_pos[0], mouse_pos[1])

    # to been able to look around 360 degrees, still not perfect
    if mouse_pos[0] <= 0:
        pygame.mouse.set_pos((1279, mouse_pos[1]))
    elif mouse_pos[0] >= 1279:
        pygame.mouse.set_pos((0, mouse_pos[1]))


    ct = pygame.time.get_ticks() / 1000

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    view = cam.get_view_matrix()
    glUniformMatrix4fv(view_loc, 1, GL_FALSE, view)

    rot_y = pyrr.Matrix44.from_y_rotation(0.8 * ct)

    glBindVertexArray(VBO)
    glBindTexture(GL_TEXTURE_2D, textures)
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, village_pos)
    glDrawArrays(GL_TRIANGLES, 0, len(village_indices))

    pygame.display.flip()

pygame.quit()