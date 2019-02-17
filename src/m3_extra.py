import math
import random
import time

class Game(object):
    def __init__(self,robot):
        """
        :type robot: rosebot.RoseBot
        """

        self.robot = robot
        self.need_to_stop = False

########################################################################################################################


def m3_start_game(robot, parameter_box):
    print('start')
    while True:
        if robot.sensor_system.get_reflected_light_intensity() > parameter_box.color_threshold:  ### Might be a redundant conditional statement
            for k in range(2):
                robot.sound_system.beeper.beep().wait()

