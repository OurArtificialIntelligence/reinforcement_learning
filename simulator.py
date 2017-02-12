import random

class Simulator:
    
    def __init__(self, begin, states, terminates, trans, rewards, actions, num_games=0, alpha_value=0, gamma_value=0, epsilon_value=0):
        '''
        Setup the Simulator with the provided values.
        :param num_games - number of games to be trained on.
        :param alpha_value - 1/alpha_value is the decay constant.
        :param gamma_value - Discount Factor.
        :param epsilon_value - Probability value for the epsilon-greedy approach.
        '''

        self.qtable  = {}                   # a qtable: (state, action) -> utility
        self.begin    = begin               # the beginning state
        self.terminates = terminates        # a list of all terminating states

        self.trans  = trans                 # transion: (currState) -> nextState
        self.rewards  = rewards             # reward  : (currState) -> rewards
        self.actions  = actions             # a list of all possible actions

        self.num_games = num_games       
        self.epsilon_value = epsilon_value       
        self.alpha_value = alpha_value       
        self.gamma_val = gamma_value
        
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
            action = random(self.actions)
            return action
        else:                                      #choose max action
            for a in self.actions:
                oneQ = self.getQ(state, a)
                dict[oneQ] = a                    ##!!!!may map one to multiple action

        q = [self.getQ(state, a) for a in self.actions]
        maxQ = max(q)
        action = dict[maxQ]
        return action

    def myUpdate(self, state):
        action   = self.chooseAction(state)
        nextstate=self.trans[(state, action)]
        oldv =  self.qtable.get((state, action), 0.0)
        self.qtable[(state, action)] = oldv + self.alpha_value * (self.reward[nextstate] - oldv)
        return  nextstate


    def train_once(self):      ##train our states once

        currState = self.begin
        while (currState in self.terminates):
            currState = self.myUpdate(self.begin)   ##not sure, may cause bug




    def train_agent(self):
        '''
        Train the agent over a certain number of games.
        '''
        # Your Code Goes Here!
        for i in self.num_games:
            self.train_once(self)



    def play_game(self):
        '''
        Simulate an actual game till the agent loses.
        '''
        # Your Code Goes Here!
        pass