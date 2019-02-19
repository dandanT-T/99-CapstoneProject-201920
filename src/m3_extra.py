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
        if parameter_box.need_to_start == True:
            break
    while True:
        while True:
            if robot.sensor_system.color_sensor.get_reflected_light_intensity()>20:
                break
        m3_step_one(robot)

def m3_step_one(robot):
    k = time.time()
    while True:
        #print(robot.sensor_system.color_sensor.get_reflected_light_intensity())
        if robot.sensor_system.color_sensor.get_reflected_light_intensity() < 10:  # parameter_box.color_threshold:  ### Might be a redundant conditional statement
            for k in range(5):
                robot.sound_system.beeper.beep().wait()
            print('You made it!')
            robot.sound_system.tone_maker.play_tone_sequence([
                (392, 350, 100), (392, 350, 100), (392, 350, 100), (311.1, 250, 100),
                (466.2, 25, 100), (392, 350, 100), (311.1, 250, 100), (466.2, 25, 100),
                (392, 700, 100)])
            break
        if time.time() - k > 20:
            print('You Lose')
            robot.drive_system.stop()
            robot.sound_system.tone_maker.play_tone_sequence([
                (392, 350, 100), (392, 350, 100), (392, 350, 100), (311.1, 250, 100),
                (466.2, 25, 100), (392, 350, 100), (311.1, 250, 100), (466.2, 25, 100),
                (392, 700, 100), (587.32, 350, 100), (587.32, 350, 100),
                (587.32, 350, 100), (622.26, 250, 100), (466.2, 25, 100),
                (369.99, 350, 100), (311.1, 250, 100), (466.2, 25, 100),
                (392, 700, 100),
                (784, 350, 100), (392, 250, 100), (392, 25, 100), (784, 350, 100),
                (739.98, 250, 100), (698.46, 25, 100), (659.26, 25, 100),
                (622.26, 25, 100), (659.26, 50, 400), (415.3, 25, 200),
                (554.36, 350, 100),
                (523.25, 250, 100), (493.88, 25, 100), (466.16, 25, 100),
                (440, 25, 100),
                (466.16, 50, 400), (311.13, 25, 200), (369.99, 350, 100),
                (311.13, 250, 100), (392, 25, 100), (466.16, 350, 100),
                (392, 250, 100),
                (466.16, 25, 100), (587.32, 700, 100), (784, 350, 100),
                (392, 250, 100),
                (392, 25, 100), (784, 350, 100), (739.98, 250, 100),
                (698.46, 25, 100),
                (659.26, 25, 100), (622.26, 25, 100), (659.26, 50, 400),
                (415.3, 25, 200),
                (554.36, 350, 100), (523.25, 250, 100), (493.88, 25, 100),
                (466.16, 25, 100), (440, 25, 100), (466.16, 50, 400),
                (311.13, 25, 200),
                (392, 350, 100), (311.13, 250, 100), (466.16, 25, 100),
                (392.00, 300, 150), (311.13, 250, 100), (466.16, 25, 100), (392, 700)
                ]).wait()
            break

        time.sleep(0.01)



