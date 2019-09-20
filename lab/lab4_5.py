from math import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import tkinter as tk
import tkinter.simpledialog as tksd

root = tk.Tk()
#root.geometry('250x150+0+0')
approx = tksd.askinteger("Approximation", "Введите точность аппроксимации\n( 10 -многоугольник, 1000 - гладкий шар)",
                       parent=root, minvalue = 10)

lx = tksd.askfloat("Parameter x (Float)", "Введите параметр освещения(x):",
                   parent=root)
ly = tksd.askfloat("Parameter y (Float)", "Введите параметр освещения(y):",
                   parent=root)
lz = tksd.askfloat("Parameter z (Float)", "Введите параметр освещения(z):",
                   parent=root)

# approx = 10
user_theta = 0
user_phi = 0

# Direction of light

#direction = [0.0, 2.0, -1.0, 1.0]
direction = [lx, ly, lz, 1.0]

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
    glShadeModel(GL_FLAT)

    draw(approx, approx)
    glutSwapBuffers()


def draw(lats, longs):
    for i in range(0, lats + 1):
        lat0 = pi * (-0.5 + float(float(i - 1) / float(lats)))
        z0 = sin(lat0)
        zr0 = cos(lat0)

        lat1 = pi * (-0.5 + float(float(i) / float(lats)))
        z1 = sin(lat1)
        zr1 = cos(lat1)

        # Use Quad strips to draw the sphere
        glBegin(GL_QUAD_STRIP)

        for j in range(0, longs + 1):
            lng = 2 * pi * float(float(j - 1) / float(longs))
            x = cos(lng)
            y = sin(lng)
            glNormal3f(x * zr0, y * zr0, z0)
            glVertex3f(x * zr0, y * zr0, z0)
            glNormal3f(x * zr1, y * zr1, z1)
            glVertex3f(x * zr1, y * zr1, z1)

        glEnd()


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
        user_phi = 1
    if key == GLUT_KEY_DOWN:
        user_phi = -1

    # Rotate the cube
    if key == GLUT_KEY_LEFT:
        user_theta = 1
    if key == GLUT_KEY_RIGHT:
        user_theta = -1

    compute_location(user_theta, user_phi)
    glutPostRedisplay()


# Initialize the OpenGL pipeline
glutInit(sys.argv)

# Set OpenGL display mode
glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)

# Set the Window size and position
glutInitWindowSize(600, 600)
glutInitWindowPosition(0, 0)
# Create the window with given title
glutCreateWindow('Lebedev')

# Instantiate the sphere object

# Set the callback function for display
glutDisplayFunc(display)

# Set the callback function for the visibility
glutVisibilityFunc(visible)

# Set the callback for special function
glutSpecialFunc(special)

rotation = 0
width, height = 600, 600
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
glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient_intensity)

# Enable light number 0
glEnable(GL_LIGHT0)

# Set position and intensity of light
glLightfv(GL_LIGHT0, GL_POSITION, direction)
glLightfv(GL_LIGHT0, GL_DIFFUSE, intensity)

# Setup the material
glEnable(GL_COLOR_MATERIAL)
glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)

# Run the OpenGL main loop
glutMainLoop()
