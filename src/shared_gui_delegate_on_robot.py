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
        self.need_to_stop = False
### Drive System Shared Delegate Kirk Preston ###



    def forward(self, left_wheel_speed, right_wheel_speed):
        print("go forward", left_wheel_speed, right_wheel_speed)
        self.robot.drive_system.go(int(left_wheel_speed), int(right_wheel_speed))

    def backward(self, left_wheel_speed, right_wheel_speed):
        print("go backward", left_wheel_speed, right_wheel_speed)
        self.robot.drive_system.go(int(left_wheel_speed)*-1, int(right_wheel_speed)*-1)

    def left(self, left_wheel_speed, right_wheel_speed):
        print("going left", left_wheel_speed, right_wheel_speed)
        self.robot.drive_system.go(int(left_wheel_speed), int(right_wheel_speed))

    def right(self, left_wheel_speed, right_wheel_speed):
        print("going right", left_wheel_speed, right_wheel_speed)
        self.robot.drive_system.go(int(left_wheel_speed), int(right_wheel_speed))

    def stop(self):
        print('stopping...')
        self.robot.drive_system.stop()

    def go_straight_for_seconds(self, seconds, speed):
        print("going for seconds", speed, seconds)
        self.robot.drive_system.go_straight_for_seconds(seconds,int(speed))

    def go_straight_for_inches_using_time(self, inches,speed):
        print("going for inches by seconds", speed, inches)
        self.robot.drive_system.go_straight_for_inches_using_time(inches, int(speed))

    def go_straight_for_inches_using_encoder(self, inches,speed):
        print('going for inches by encoder', speed, inches)
        self.robot.drive_system.go_straight_for_inches_using_encoder(inches, int(speed))



### Arm & Claw Shared Delegate- Nelson ###

    def beeping(self,number):
        N = int(number)
        print('i am beeping')
        for k in range(N):
            self.robot.sound_system.beeper.beep().wait()

    def tone(self,frequency, duration):
        F = int(frequency)
        D = (duration)
        print('i am singing')
        self.robot.sound_system.tone_maker.play_tone(F,D)

    def phrase(self,phrase):
        P = str(phrase)
        print('i am speaking')
        self.robot.sound_system.speech_maker.speak(P).wait()

    def raise_arm(self):
        print('raising arm')
        self.robot.arm_and_claw.raise_arm()

    def lower_arm(self):
        print('lowering arm')
        self.robot.arm_and_claw.lower_arm()

    def calibrate_arm(self):
        print('calibrating arm')
        self.robot.arm_and_claw.calibrate_arm()

    def move_arm_to_position(self,position):
        P = position
        print('moving arm to position')
        self.robot.arm_and_claw.move_arm_to_position(int(P))

    def quit(self):
        print('quit')
        self.need_to_stop = True

