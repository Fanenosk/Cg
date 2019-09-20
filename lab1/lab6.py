from math import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import tkinter as tk
import tkinter.simpledialog as tksd


#approx = 1000
user_theta = 0
user_phi = 0
root = tk.Tk()
approx = tksd.askinteger("Approximation", "Введите точность аппроксимации\n( 10 -многоугольник, 1000 - гладкий шар)",
                         parent=root, minvalue=10)

sp_shininess = tksd.askfloat("shininess", "Введите коэффициент блеска фигуры от 0 до 1:",
                             parent=root, minvalue=0.1, maxvalue=1.0)
sp_shininess = sp_shininess * 1281

# Direction of light
direction = [2.0, 2.0, 2.0, 1.0]

# Intensity of light
intensity = [0.7, 0.7, 0.7, 1.0]

# Intensity of ambient light
ambient_intensity = [0.3, 0.3, 0.3, 1.0]


# counter for main loop
last_time = 0


# black background
glClearColor(0.0, 0.0, 0.0, 0.0)


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Set color to white
    glColor3f(1.0, 1.0, 1.0)

    # Shade model
    glShadeModel(GL_SMOOTH)

    draw(approx, approx)
    glutSwapBuffers()

# x = -10
# y = -10
# z = -10


def draw(lats, longs):
    glutSolidSphere(1, approx, approx)
    # global x
    # global y
    # global z

    # if x < 10:
    #     x += 0.1
    # elif y < 10:
    #     y += 0.1
    # else:
    #     z += 0.1
    # glLightfv(GL_LIGHT0, GL_POSITION, [x, y, z, 1.0])


def idle():
    global last_time
    time = glutGet(GLUT_ELAPSED_TIME)
    if last_time == 0 or time >= last_time + 40:
        last_time = time
        glutPostRedisplay()

# The visibility callback


def visible(vis):
    if vis == GLUT_VISIBLE:
        glutIdleFunc(idle)
    else:
        glutIdleFunc(None)


def compute_location(user_theta, user_phi):
    glMatrixMode(GL_MODELVIEW)
    glRotatef(user_theta, 0, 0, 1)  # вращения объекта вдоль оси Z
    glRotatef(user_phi, 1, 0, 0)  # вращения объекта вдоль оси Y


def special(key, x, y):
    global user_theta
    global user_phi
    user_theta = 0
    user_phi = 0
    # Scale the sphere up or down
    if key == GLUT_KEY_UP:
        user_phi = 0.5
    if key == GLUT_KEY_DOWN:
        user_phi = -0.5

    # Rotate the cube
    if key == GLUT_KEY_LEFT:
        user_theta = 0.5
    if key == GLUT_KEY_RIGHT:
        user_theta = -0.5

    compute_location(user_theta, user_phi)
    glutPostRedisplay()


# Initialize the OpenGL pipeline
glutInit(sys.argv)

# Set OpenGL display mode
glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)

# Set the Window size and position
glutInitWindowSize(300, 300)
glutInitWindowPosition(50, 100)
# Create the window with given title

# Instantiate the sphere object

# Set the callback function for display
glutDisplayFunc(display)

# Set the callback function for the visibility
glutVisibilityFunc(visible)

# Set the callback for special function
glutSpecialFunc(special)

rotation = 0
width, height = 300, 300
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
# set field of view
gluPerspective(10, float(width) / height, 1, 1000)

glMatrixMode(GL_MODELVIEW)
glLoadIdentity()  # считывает текущую матрицу GL_MODELVIEW
glTranslate(0, 0, -15)  # перемещение фигуры вглубь сцены


# освещение
# Set OpenGL parameters
glEnable(GL_DEPTH_TEST)

# Enable lighting
glEnable(GL_LIGHTING)

# Set light model
glLightModelfv(GL_LIGHT_MODEL_LOCAL_VIEWER, GL_TRUE)

# Enable light number 0
glEnable(GL_LIGHT0)

# Set position and intensity of light

light_green = [0.0, 1.0, 0.0, 1.0]
white = [1.0, 1.0, 1.0, 1.0]

glLightfv(GL_LIGHT0, GL_AMBIENT, ambient_intensity)
glLightfv(GL_LIGHT0, GL_DIFFUSE, intensity)
glLightfv(GL_LIGHT0, GL_SPECULAR, white)

glLightfv(GL_LIGHT0, GL_POSITION, direction)

# Setup the material
glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, light_green)
glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, light_green)
glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, white)
glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, sp_shininess)


# Run the OpenGL main loop
glutMainLoop()
