"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Nelson Rainey.
  Winter term, 2018-2019.
"""

import rosebot
import mqtt_remote_method_calls as com
import time
import shared_gui_delegate_on_robot


def main():
    """
    This code, which must run on the EV3 ROBOT:
      1. Makes the EV3 robot to various things.
      2. Communicates via MQTT with the GUI code that runs on the LAPTOP.
    """
    #run_test_arm()
    #test_lower_arm()
    #test_calibrate()
    real_thing()

def run_test_arm():
    robot = rosebot.RoseBot()
    robot.arm_and_claw.raise_arm()

def test_lower_arm():
    robot = rosebot.RoseBot()
    robot.arm_and_claw.lower_arm()

def test_calibrate():
    robot = rosebot.RoseBot()
    robot.arm_and_claw.calibrate_arm()

def test_DriveSystem():
    robot = rosebot.RoseBot()
    robot.drive_system.go(100,100)
    robot.drive_system.stop()
    #robot.drive_system.go_straight_for_seconds(5,100)
    #robot.drive_system.go_straight_for_inches_using_time(12,100)
    #robot.drive_system.go_straight_for_inches_using_encoder(12,100)

def real_thing():
    robot = rosebot.RoseBot()
    delegate = shared_gui_delegate_on_robot.Handler(robot)
    mqtt_reciever = com.MqttClient(delegate)
    mqtt_reciever.connect_to_pc()

    while True:
        time.sleep(0.01)



# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()