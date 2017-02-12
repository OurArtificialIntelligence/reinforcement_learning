import random
import numpy

from graphics import *
from simulator import Simulator
from mdp import Mdp



if __name__ == "__main__":
    '''
    Runner code to start the training and game play.
    state: 12*12 *(grid ball coord)
    	   2      (x speed)
    	   3      (y speed)
    	   12     (current x)
    '''

    alpha_value = 0
    gamma_value = 0
    epsilon_value = 0
    num_games = 0
    #                      x  y  vx vy  py
    mystate = numpy.zeros((13,12,2, 3,  12))
    for x in range(0, 13):
        for y in range(0, 12):
            for vx in range(0, 2):
                for vy in range(0, 3):
                    for py in range(0,12):
                        mystate[12][y][vx][vy][py] = -1    #out of bound, got negative reward
                        mystate[11][y][vx][vy][py] =  1    #bounce the ball, got positive reward




    alpha_value = 0
    gamma_value = 0
    epsilon_value = 0
    num_games = 0
    print(x)

    reward = []
    win = GraphWin("Pong Game", 200, 200)
    for i in range (0, 12):
        for j in range (0, 12):
            aRectangle = Rectangle(Point(i*10, j*10), Point(i*10+10, j*10+10))
            aRectangle.draw(win)

    myball = Circle(Point(35, 45), 5)
    myball.draw(win)

    win.getMouse()  # pause for click in window
    win.close()