import random
import numpy
from mdp import Mdp

class Simulator:
    
    def __init__(self, current, actions, num_games, alpha_value, gamma_value, epsilon_value):
        '''
        Setup the Simulator with the provided values.
        :param num_games - number of games to be trained on.
        :param alpha_value - 1/alpha_value is the decay constant.
        :param gamma_value - Discount Factor.
        :param epsilon_value - Probability value for the epsilon-greedy approach.
        '''
        LD = Mdp
        self.qtable  = {}                   # a qtable: (state, action) -> utility
        self.current    =  LD          # the current real state
        self.currentcp  =  LD          # copy of current real state, to retrain
#        self.rewards  = rewards
        self.actions  = actions             # a list of all possible actions

        self.num_games = num_games       
        self.epsilon_value = epsilon_value       
        self.alpha_value = alpha_value       
        self.gamma_value = gamma_value
        
        # Your Code Goes Here!

    def getQ(self, state, action):
        return self.qtable.get((state, action), 0.0)
        # return self.q.get((state, action), 1.0)

    #def myQ(self, state, action, reward, value):
    #    oldv = self.qtable.get((state, action), None)
    #    if oldv is None:
    #        self.qtable [(state, action)] = reward
    #    else:
    #        self.qtable [(state, action)] = oldv + self.alpha_value * (value - oldv)

    def chooseAction(self, state):
        dict = {}
        if random.random() < self.epsilon_value:  #choose arbitrary action
            action = random.choice(self.actions)
            return action
        else:                                      #choose max action
            for a in self.actions:
                oneQ = self.getQ(state, a)
                dict[oneQ] = a                    ##!!!!may map one to multiple action

        q = [self.getQ(state, a) for a in self.actions]
        maxQ = max(q)
        action = dict[maxQ]
        return action

    def myUpdate(self):   #current  #assume curState is normal
        if self.current.check_reward() == -1:
            curState = self.current.discretize_state()
            for a in self.actions:
                self.qtable[(curState,a)] = -1
                return

        curState  = self.current.discretize_state()                             #decretize curr val
        action    = self.chooseAction(curState)                                 #choose proper action
        flag      = self.current.simulate_one_time_step(action)                 #decretize curr val
        nextState = self.current.discretize_state()                             #check if we go to the new state
        while(curState == nextState):
            action = self.chooseAction(curState)
            flag = (self.current).simulate_one_time_step(action)
            nextState = (self.current).discretize_state()

        oldv  =  self.qtable.get((curState, action), 0.0)
        nextv =  self.qtable.get((nextState, action), 0.0)
        #print("currstat_re:", self.current.check_reward())
        self.qtable[(curState, action)] = oldv + self.alpha_value * (nextv + self.gamma_value * self.current.check_reward() - oldv)

    def train_once(self):      ##train our states once
        count = 10000
        self.current= Mdp()   #always start from the beginning
        curState = self.current.discretize_state()
        nexState = self.current.discretize_state()
        while  self.current.check_reward()!=-1 and count>=0 :
            curState = self.current.discretize_state()
            action = self.chooseAction(curState)
            flag = (self.current).simulate_one_time_step(action)
            nexState = self.current.discretize_state()
            if curState!=nexState :
                oldv = self.qtable.get((curState, action), 0.0)
                nextv = self.qtable.get((nexState, action), 0.0)
                self.qtable[(curState, action)] = oldv + self.alpha_value * (nextv + self.gamma_value * flag - oldv)
            #self.myUpdate()
            count=count-1 

    def train_agent(self):
        for i in range (self.num_games):
            self.train_once()


    def chooseBest(self, state):
        dict = {}                             #choose max action
        for a in self.actions:
            oneQ = self.getQ(state, a)
            dict[oneQ] = a                    ##!!!!may map one to multiple action

        q = [self.getQ(state, a) for a in self.actions]
        ##print("qchoice", q)
        maxQ = max(q)
        action = dict[maxQ]
        return action

    def printQ(self):
        for keys,values in self.qtable.items():
            print(keys)
            print(values)


    def letplay(self):
        score = 0
        count = 1000000000               # just avoid infinite loop
        self.current =  Mdp()            # always start from the beginning
        flag = 0
        while (flag != -1 and count >= 0):
            curState = (self.current).discretize_state()
            #print(curState)
            action = self.chooseBest(curState)
            flag = (self.current).simulate_one_time_step(action)
            ##print("mybarl:", self.current.paddle_yh)
           ## print("mybarh:", self.current.paddle_yh)

            if flag == 1:
                score = score + 1
            
            count= count-1
            
        print("x",  self.current.ball_x)
        print("y",  self.current.ball_y)
        print("yh", self.current.paddle_yh)
        print("yl", self.current.paddle_yl)
        return score 

#        self.ball_x = 0.5
#        self.ball_y = 0.5
#        self.velocity_x = 0.03
#        self.velocity_y = 0.01
#        self.paddle_yh = 0.9  # (0.5 - height/2)                 #I am the inital state #
#        self.paddle_yl = 0.4                                                            #
#        self.flag = 0                                                                   #
#        self.paddle_len = 0.9