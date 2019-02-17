import math
import random
import time

class Handler(object):
    def __init__(self,robot):
        """
        :type robot: rosebot.RoseBot
        """

        self.robot = robot
        self.need_to_stop = False

########################################################################################################################


def m3_start_game(robot):
    print('start')