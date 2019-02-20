"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Yu Xin.
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
    robot=rosebot.RoseBot()
    delegate=shared_gui_delegate_on_robot.Handler(robot)
    mqtt_receiver=com.MqttClient(delegate)
    robot.drive_system.mqtt_sender = mqtt_receiver
    mqtt_receiver.connect_to_pc()
    while True:
        time.sleep(0.1)
        if delegate.need_to_stop:
            print('quit')
            break

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()