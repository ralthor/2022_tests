#include <windows.h>
#include <GL/gl.h>
#include <GL/glu.h>
#include <GL/freeglut.h>
#include <math.h>

class Point
{
public:
    float x, y;
    Point(float x, float y)
    {
        this->x = x;
        this->y = y;
    }
};


Point rotate(Point p, float angle)
{
    float x = p.x * cos(angle) - p.y * sin(angle);
    float y = p.x * sin(angle) + p.y * cos(angle);
    return Point(x, y);
}

long int timeInSec()
{
    return glutGet(GLUT_ELAPSED_TIME) / 1000;
}

float angleInSec()
{
    return timeInSec() * 2 * M_PI / 60;
}

void display()
{
    Point p1(-0.5, -0.5);
    Point p2(0.5, -0.5);
    Point p3(0.0, 0.5);

    p1 = rotate(p1, angleInSec());
    p2 = rotate(p2, angleInSec());
    p3 = rotate(p3, angleInSec());

    glClear(GL_COLOR_BUFFER_BIT);
    glBegin(GL_TRIANGLES);
        glVertex2f(p1.x, p1.y);
        glVertex2f(p2.x, p2.y);
        glVertex2f(p3.x, p3.y);
    glEnd();
    glFlush();
}

int main(int argc, char** argv)
{
    glutInit(&argc, argv);
    glutCreateWindow("Triangle");
    glutDisplayFunc(display);
    glutMainLoop();
    return 0;
}

// to compile: g++ <this file's name> -o opengl.exe -lfreeglut -lopengl32 -lglu32
// before that, you need to install freeglut