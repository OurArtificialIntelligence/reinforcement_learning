import numpy
import random
import math

class Mdp:

    def __init__(self):

        self.ball_x = 0.5
        self.ball_y = 0.5
        self.velocity_x = 0.03
        self.velocity_y = 0.01
        self.paddle_yh = 0.6  # (0.5 - height/2)                 #I am the inital state #
        self.paddle_yl = 0.4                                                            #
        self.flag = 0                                                                   #
        self.paddle_len = 0.2
        # the agent can choose between 3 actions - stay, up or down respectively.
        self.actions = [0, 0.04, -0.04]

#------------------------------------------
    def peddleMove(self, action_selected):

        # move no --------------------------------------------
        if action_selected == 0:
            return
        # move up --------------------------------------------
        elif action_selected == 0.04:
            self.paddle_yh = min(self.paddle_yh + 0.04, 1)
            self.paddle_yl = self.paddle_yh- self.paddle_len
            return
        # #move down --------------------------------------------
        elif action_selected == -0.04:
            self.paddle_yl = max(self.paddle_yl - 0.04, 0)
            self.paddle_yh = self.paddle_yl + self.paddle_len
            return

#----------------------------------------------------------------------------
    def ballMove (self):
        #---------------update position---------------------
        self.ball_x = self.ball_x +  self.velocity_x
        self.ball_y = self.ball_y +  self.velocity_y

        #---------------check normal bounce---------------------

        if self.ball_y < 0:
            self.velocity_y = -self.velocity_y
            self.ball_y = -self.ball_y

        if self.ball_y > 1:
            self.velocity_y = 2 - self.velocity_y
            self.ball_y = 2 - self.ball_y

        if self.ball_x < 0:
            self.velocity_x = -self.velocity_x
            self.ball_x = -self.ball_x

        # ---------------check special bounce by peddle---------------------
        if self.ball_x >= 1:
            if self.ball_y >= self.paddle_yl and self.ball_y <= (self.paddle_yl + self.paddle_len):           ##hit the paddle
                U = random.uniform(-0.015,0.015)
                if (U-self.velocity_x) <= 0.03:
                    self.velocity_x = U -0.03
                elif (self.velocity_x-U) <= 0.03:
                    self.velocity_x = U + 0.03      
                elif (U-self.velocity_x) >= 1:
                    self.velocity_x = U - 1
                elif (self.velocity_x-U) >= 1:
                    self.velocity_x = U + 1    
                
                V = random.uniform(-0.03, 0.03)
                if (self.velocity_y + V) >= 1:
                    self.velocity_y = 1 - V 
                elif (-self.velocity_y - V) >= 1:
                    self.velocity_y = -V - 1    
                    
                self.ball_x = 2 * 1 - self.ball_x
                return 1  #reward!
            else:
                return -1 #fail

        return  0    #cont
# ----------------------------------------------------------------------------
    def check_reward(self):
        return self.flag

#-------------------------------------------------
    def simulate_one_time_step(self, action_selected):
        '''
        :param action_selected - Current action to execute.
        Perform the action on the current continuous state.
        '''
        # not move--------------------------------------------
        self.peddleMove(action_selected)
        self.flag = self.ballMove()
        return self.flag

    def discretize_state(self):
        '''
        Convert the current continuous state to a discrete state.
        '''
  
        paddle_height = 0.2
        if self.velocity_y > 0:
            velocity_y_dis = 1
        elif self.velocity_y < 0:
            velocity_y_dis = -1
        elif abs(self.velocity_y) <= 0.015:
            velocity_y_dis = 0
        if self.velocity_x < 0:
            velocity_x_dis = -1
        elif self.velocity_x >= 0:
            velocity_x_dis = 1
            
        if (self.paddle_yl == 1 - self.paddle_len):
            discrete_paddle = 11
        else:
            discrete_paddle = math.ceil((12 * self.paddle_yl / (1 - self.paddle_len)))

        ball_x_dis = math.floor(self.ball_x * 12)
        ball_y_dis = math.floor(self.ball_y * 12)

        return (ball_x_dis, ball_y_dis, velocity_x_dis, velocity_y_dis, discrete_paddle)

        # Your Code Goes Here!
        pass