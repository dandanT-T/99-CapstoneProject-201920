import math
import random
import time
import rosebot

class Game(object):
    def __init__(self,robot):
        """
        :type robot: rosebot.RoseBot
        """

        self.robot = robot
        self.need_to_stop = False

########################################################################################################################


def m3_start_game(robot, parameter_box):
    #robot = rosebot.RoseBot()
    #print('start')
    while True:
        if robot.sensor_system.color_sensor.get_reflected_light_intensity() > parameter_box.color_threshold:  ### Might be a redundant conditional statement
            for k in range(2):
                robot.sound_system.beeper.beep().wait()
        time.sleep(0.01)

'''def m3_forward(self, speed):
    print("go forward", speed, speed)
    self.robot.drive_system.go(int(speed), int(speed))

def m3_backward(self, speed):
    print("go backward", speed, speed)
    self.robot.drive_system.go(int(speed)*-1, int(speed)*-1)

def m3_left(self, speed):
    print("going left", speed, speed)
    self.robot.drive_system.go(int(0), int(speed))

def m3_right(self, speed):
    print("going right", speed, speed)
    self.robot.drive_system.go(int(speed), int(0))

def m3_stop(self):
    print('stopping...')
    self.robot.drive_system.stop()'''