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
        self.robot.drive_system.go(int(left_wheel_speed), int(right_wheel_speed))

    def backward(self, left_wheel_speed, right_wheel_speed):
        print("go backward", left_wheel_speed, right_wheel_speed)
        self.robot.drive_system.go(int(left_wheel_speed*-1), int(right_wheel_speed*-1))

    def left(self, left_wheel_speed, right_wheel_speed):
        print("going left", left_wheel_speed, right_wheel_speed)
        self.robot.drive_system.go((int(left_wheel_speed))*-1, int(right_wheel_speed)*-1)

    def right(self, left_wheel_speed, right_wheel_speed):
        print("going right", left_wheel_speed, right_wheel_speed)
        self.robot.drive_system.go(int(left_wheel_speed), int(right_wheel_speed)*-1)

    def stop(self):
        print('stopping...')
        self.robot.drive_system.stop()

    def go_straight_for_seconds(self, left_wheel_speed, right_wheel_speed, seconds):
        print("going for seconds", left_wheel_speed, right_wheel_speed, seconds)
        while start < seconds:
            self.forward(int(right_wheel_speed), int(left_wheel_speed))
            break
        self.stop()

    def beeping(self,number):
        N = int(number)
        for k in range(N):
            print('beep')

    def tone(self,frequency, duration):
        F = int(frequency)
        D = (duration)
        for k in range(D):
            print('making tone F for time D')

    def phrase(self,phrase):
        P = str(phrase)
        print('saying phrase P')

    def raise_arm(self):
        print('raising arm')
        self.robot.arm_and_claw.raise_arm()

    def lower_arm(self):
        print('lowering arm')
        self.robot.arm_and_claw.lower_arm()

    def calibrate_arm(self):
        print('calibrating arm')
        self.robot.arm_and_claw.calibrate_arm()

    def move_arm_to_position(self):
        print('moving arm to position')
        self.robot.arm_and_claw.move_arm_to_position()

