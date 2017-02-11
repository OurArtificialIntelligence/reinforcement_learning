import random
from Simulator.simulator import Simulator


if __name__ == "__main__":
    '''
    Runner code to start the training and game play.
    state: 12*12 *(grid ball coord)
    	   2      (x speed)
    	   3      (next action)
    	   12     (current x)
    '''



    alpha_value = 0
    gamma_value = 0
    epsilon_value = 0
    num_games = 0
    Simulator(num_games, alpha_value, gamma_value, epsilon_value)
    x = random.random()
    print(x)