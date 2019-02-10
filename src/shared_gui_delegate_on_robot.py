"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    Yu Xin, Kirk Preston, Nelson Rainey and Zhicheng Kai.
  Winter term, 2018-2019.
"""
class Handler(object):
    def __init__(self,robot):
        """
        :type robot: rosebot.RoseBot
        """

        self.robot = robot

    def forward(self, left_wheel_speed, right_wheel_speed):
        print("go forward", left_wheel_speed, right_wheel_speed)
        self. robot.drive_system.go(int(left_wheel_speed), int(right_wheel_speed))

    def beeping(self,number):
        N = int(number)
        for k in range(N):
            print('beep')

    def tone(self,frequency, duration):
        F = int(frequency)
        D = (duration)
        for k in range(D):
            print(F)

    def phrase(self,phrase):
        P = str(phrase)
        print(P)