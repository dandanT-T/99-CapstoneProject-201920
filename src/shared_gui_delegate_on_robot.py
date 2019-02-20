"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    Yu Xin, Kirk Preston, Nelson Rainey and Zhicheng Kai.
  Winter term, 2018-2019.
"""
import math
import random
import time
import m3_extra

class Handler(object):
    def __init__(self,robot):
        """
        :type robot: rosebot.RoseBot
        """

        self.robot = robot
        self.need_to_stop = False
        self.color_threshold = 50
        self.timer_countdown = 10
        self.need_to_start = False
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
        self.robot.drive_system.go_straight_for_seconds(float(seconds),int(speed))

    def go_straight_for_inches_using_time(self, inches,speed):
        print("going for inches by seconds", speed, inches)
        self.robot.drive_system.go_straight_for_inches_using_time(float(inches), int(speed))

    def go_straight_for_inches_using_encoder(self, inches,speed):
        print('going for inches by encoder', speed, inches)
        self.robot.drive_system.go_straight_for_inches_using_encoder(float(inches), int(speed))



### Arm & Claw Shared Delegate- Nelson ###

    def growl(self):
        print('i am using growl')
        P = str('grrrrr')
        self.robot.sound_system.speech_maker.speak(P).wait()

    def quick_attack(self):
        print('i am using quick_attack')
        while True:
            D = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
            print(D)
            self.robot.drive_system.go(100,100)
            if D <= 1:
                self.robot.drive_system.go_backward_until_distance_is_greater_than(7,100)
                break

    def take_down(self):
        print('i am using tackle')
        while True:
            D = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
            print(D)
            self.robot.drive_system.go(100,100)

    def seismic(self):
        print('i am using seismic slam')
        while True:
            D = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
            print(D)
            self.robot.drive_system.go(100,100)
            if D < 0.5:
                self.robot.drive_system.stop()
                self.robot.arm_and_claw.raise_arm()
                self.robot.arm_and_claw.lower_arm()
                self.robot.drive_system.go_backward_until_distance_is_greater_than(7,100)
                break



    def feature_9(self,speed, length, frequency):
        print('got to feature 9')
        print(speed,length, frequency)
        self.robot.drive_system.go(speed,speed)
        while True:
            D = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
            self.robot.led_system.flash_left(frequency)
            self.robot.led_system.flash_right(frequency)
            self.robot.led_system.flash_both(frequency)
            frequency = frequency - 1
            if frequency < 1:
                frequency = 10
            if D < length:
                self.robot.led_system.flash_off()
                self.robot.drive_system.stop()
                self.robot.arm_and_claw.raise_arm()
                break


    def left_flash(self, flash_rate):
        R = int(flash_rate)
        print('i am flashing left')
        self.robot.led_system.flash_left(R)

    def right_flash(self, flash_rate):
        R = int(flash_rate)
        print(' i am flashing right')
        self.robot.led_system.flash_right(R)

    def both_flash(self, flash_rate):
        R = int(flash_rate)
        print('i am flashing both')
        self.robot.led_system.flash_both(R)

    def LED_off(self):
        print('turning off')
        self.robot.led_system.flash_off()

    def getting_blob(self):
        print('getting blob')
        self.robot.drive_system.display_camera_data()

    def spin_clockwise_until_sees_object(self,speed,area):
        print('spinning clockwise')
        self.robot.drive_system.spin_clockwise_until_sees_object(speed, area)

    def spin_counterclockwise_until_sees_object(self,speed,area):
        print('spinning counterclockwise')
        self.robot.drive_system.spin_counterclockwise_until_sees_object(speed,area)

    def beeping(self,number):
        N = int(number)
        print('i am beeping')
        for k in range(N):
            self.robot.sound_system.beeper.beep().wait()

    def tone(self,frequency, duration):
        F = int(frequency)
        D = int(duration)
        print('i am singing')
        self.robot.sound_system.tone_maker.play_tone(F,D).wait()

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

    def make_higher_tones(self,initial_frequency,rate_of_increase):
        self.robot.drive_system.make_higher_tones_while_getting_closer(initial_frequency,rate_of_increase)

    def spin_clockwise_until_sees_object(self,speed):
        self.robot.drive_system.spin_clockwise_until_sees_object(int(speed),400)
        self.make_higher_tones(400,50)

    def spin_counterclockwise_until_sees_object(self,speed):
        self.robot.drive_system.spin_counterclockwise_until_sees_object(int(speed),400)
        self.make_higher_tones(400,50)

##############################################################################################################################3

    def m3_beep_move(self, initial_rate, rate_of_increase, speed):
        print('moving forward and beeping')
        initial_rate = int(initial_rate)
        rate_of_increase = int(rate_of_increase)
        self.robot.drive_system.go(speed, speed)
        while True:
            if self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 2.5:
                break
            distance = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
            beep_range = initial_rate + int(((rate_of_increase * 10/(math.sqrt(distance)))))
            for k in range(beep_range):
                self.robot.sound_system.beeper.beep()
        self.robot.drive_system.stop()
        self.robot.arm_and_claw.raise_arm()

    def m3_greater_intensity(self, intensity_entry):
        self.robot.drive_system.go_straight_until_intensity_is_greater_than(int(intensity_entry), 100)

    def m3_smaller_intensity(self, intensity_entry):
        self.robot.drive_system.go_straight_until_intensity_is_less_than(int(intensity_entry), 100)

    def m3_color_true(self, color):
        self.robot.drive_system.go_straight_until_color_is(color, 100)

    def m3_color_false(self, color):
        self.robot.drive_system.go_straight_until_color_is_not(color, 100)

    def m3_spin_until_object(self, spin_direction, speed):
        print('spinning at set speed')
        if spin_direction == 'CW':
            self.robot.drive_system.spin_clockwise_until_sees_object(int(speed), 200)
        elif spin_direction == 'CCW':
            self.robot.drive_system.spin_counterclockwise_until_sees_object(int(speed), 200)
        self.m3_beep_move(1, 1, int(speed))
#############################################################################################################################

#m3 Kirk Preston Capstone Functions

    '''def m3_beep_on_intensity(self, color_threshold):
        if self.robot.sensor_system.color_sensor.get_reflected_light_intensity() > color_threshold:  ### Might be a redundant conditional statement
            beeper = self.robot.sound_system.beeper.beep()
            beeper.beep().wait(0.5)  ### I only need it to beep twice in succession and then stop'''

    def m3_robot_die(self):
        self.robot.drive_system.stop()
        phrase = 'Surface is too bright! Shutting down!'
        self.robot.sound_system.speech_maker.speak(phrase)
        self.raise_arm()
        self.lower_arm()

    def m3_reset_game(self, intensity=100):
        self.m3_robot_die()
        while True:
            phrase = 'Please move me to a darker surface'
            self.robot.sound_system.speech_maker.speak(phrase)
            time.sleep(10)
            if self.robot.sensor_system.color_sensor.get_reflected_light_intensity() < intensity:  #### There's going to be a set intensity
                break

    def m3_forward(self, speed):
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
        self.robot.drive_system.stop()

    def m3_game_parameters(self, speed, timer_countdown, color_threshold):
        self.speed = int(speed)
        self.timer_countdown = int(timer_countdown)
        self.color_threshold = int(color_threshold)

    def m3_start_game(self):
        print('Starting the game')
        m3_extra.m3_start_game(self.robot, self)

    def m3_start_process(self):
        self.need_to_start = True

##################################################################################################################################

    def spin_and_find(self):
        print('spin and find object')
        self.robot.f_and_g.spin_and_find()

    def m2_random_functions(self,a):
        if a==1:
            print("You get the first function!")
            self.raise_arm()
        elif a==2:
            print("You get the second function!")
            self.move_arm_to_position(random.randint(1,5000))
        elif a==3:
            print("You get the third function!")
            self.go_straight_for_seconds(random.randint(3,7),random.randint(80,100))
        elif a==4:
            print("You get the fourth function!")
            self.go_straight_for_inches_using_time(random.randint(5,15),random.randint(50,100))
        elif a==5:
            print("You get the fifth function!")
            self.beeping(random.randint(1,6))
        elif a==6:
            print("You get the sixth function!")
            self.tone(random.randint(300,1500),random.randint(70,250))
        elif a==7:
            print("You get the seventh function!")
            self.phrase("Hello World!")
        elif a==8:
            print("You get the eighth function!")
            self.make_higher_tones(random.randint(300,1000),random.randint(30,100))
        else:
            print("You get the ninth function!")
            self.spin_counterclockwise_until_sees_object(random.randint(30,70))

    def m2_do_different_things(self):
        '''
        find certain color and do different things depending on color
        :return: None
        '''
        print("True")
        while True:
            self.robot.sensor_system.camera.set_signature("SIG1")
            b1 = self.robot.sensor_system.camera.get_biggest_blob()
            self.robot.sensor_system.camera.set_signature("SIG2")
            b2 = self.robot.sensor_system.camera.get_biggest_blob()
            self.robot.drive_system.go(70,-70)
            if b1.get_area()>=1000:
                self.robot.drive_system.stop()
                self.robot.drive_system.m2_send_message("Yellow Object")
                distance=self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
                self.robot.drive_system.go_straight_for_inches_using_time(distance,70)
                self.robot.arm_and_claw.move_arm_to_position(2000)
                break
            elif b2.get_area()>=1000:
                self.robot.drive_system.stop()
                self.robot.drive_system.m2_send_message("Blue Object")
                distance = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
                self.robot.drive_system.go_backward_until_distance_is_greater_than(2*distance,70)
                break

    def m1_turtle_turn(self, degree):
        print('I am turning.')
        self.robot.RoseTurtle.turn(degree)

    def m1_turtle_square(self,length,speed):
        print('I am drawing a square')
        while self.robot.RoseTurtle.square(float(length),int(speed)) is True:
            self.need_to_stop = True

    def m1_turtle_circle(self,radius,time):
        print('I am drawing a circle')
        self.robot.RoseTurtle.circle(int(radius),float(time))

    # def m3_line_intensity_follow(self):
    #     print('following surface with intensity')
    #     self.robot.drive_systempy