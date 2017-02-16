import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

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

    LD = Mdp
    actions = [0, 0.04, -0.04]
    s = Simulator(LD, actions, 10000,0.5, 0.5, 0.3)
    s.train_agent()
    s.printQ()
    score = s.letplay()
    print (score)


