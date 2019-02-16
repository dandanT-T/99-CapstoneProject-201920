"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Nelson Rainey.
  Winter term, 2018-2019.
"""

import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
import shared_gui


def main():
    """
    This code, which must run on a LAPTOP:
      1. Constructs a GUI for my part of the Capstone Project.
      2. Communicates via MQTT with the code that runs on the EV3 robot.
    """
    # -------------------------------------------------------------------------
    # Construct and connect the MQTT Client:
    # -------------------------------------------------------------------------
    mqtt_sender = com.MqttClient()
    mqtt_sender.connect_to_ev3()

    # -------------------------------------------------------------------------
    # The root TK object for the GUI:
    # -------------------------------------------------------------------------
    root = tkinter.Tk()
    root.title("CS Project")

    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    main_frame = ttk.Frame(root, padding = 10, borderwidth = 5, relief= 'groove')
    main_frame.grid()

    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------
    teleop_frame, arm_frame, control_frame = get_shared_frames(main_frame,mqtt_sender)
    grid_frames(teleop_frame,arm_frame,control_frame)
    sound_frame=shared_gui.get_sound_frame(main_frame,mqtt_sender)
    sound_frame.grid(row=3,column=0)



    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # done: Implement and call get_my_frames(...)
    
###camera stuff
    camera_frame = ttk.Frame(main_frame,padding=10,borderwidth=5,relief="ridge" )
    camera_frame.grid(row = 0, column = 2)

    camera_print = ttk.Button(camera_frame,text = 'print blob')
    camera_print.grid(row = 1, column = 2)
    camera_print["command"]=lambda: handle_camera_print(mqtt_sender)

    camera_clockwise = ttk.Button(camera_frame, text = 'clockwise')
    camera_clockwise.grid(row = 2, column = 2)
    camera_clockwise["command"] = lambda: handle_counter_clockwise(mqtt_sender)

    camera_counterclockwise = ttk.Button(camera_frame,text = 'counter clockwise')
    camera_counterclockwise.grid(row = 3, column = 2)
    camera_counterclockwise['command'] = lambda: handle_counter_clockwise(mqtt_sender)

##LED stuff
    LED_frame = ttk.Frame(main_frame,padding = 10, borderwidth = 5, relief = 'ridge')
    LED_frame.grid(row = 0, column = 1)

    flash_left = ttk.Button(LED_frame, text = 'left flash')
    flash_left.grid(row = 1, column = 1)
    flash_left['command']=lambda: handle_flash_left(mqtt_sender)

    flash_right = ttk.Button(LED_frame, text = 'right flash')
    flash_right.grid(row = 1, column = 2)
    flash_right['command']=lambda: handle_flash_right(mqtt_sender)

    flash_both = ttk.Button(LED_frame, text = 'both flash')
    flash_both.grid(row = 1, column = 3)
    flash_both['command']=lambda: handle_both(mqtt_sender)

    LED_off = ttk.Button(LED_frame, text = 'flash off')
    LED_off.grid(row = 2, column = 1)
    LED_off['command']=lambda: handle_LED_off(mqtt_sender)

    LED_flash_frequency = ttk.Entry(LED_frame)
    LED_flash_frequency.grid(row = 5, column = 3)

    frequency = ttk.Label(LED_frame, text = 'frequency')
    frequency.grid(row = 5, column = 2)

    feature_9 = ttk.Button(LED_frame, text = 'feature_9')
    feature_9.grid(row = 7, column = 1)

    speed = ttk.Label(LED_frame, text = 'length')
    speed.grid(row = 6, column = 2)

    area = ttk.Label(LED_frame, text = 'speed')
    area.grid(row = 6, column = 3)

    feature_9_speed = ttk.Entry(LED_frame)
    feature_9_speed.grid(row = 7, column = 2)

    feature_9_length = ttk.Entry(LED_frame)
    feature_9_length.grid(row = 7, column = 3)

    feature_9['command'] = lambda: handle_feature_9(feature_9_length,feature_9_speed, LED_flash_frequency, mqtt_sender)




    def handle_feature_9(feature_9_length, feature_9_speed,LED_flash_frequency, mqtt_sender):
        print('i am doing feature 9')
        mqtt_sender.send_message('feature_9',[int(feature_9_length.get()),int(feature_9_speed.get()), int(LED_flash_frequency.get())])

    def handle_flash_left(mqtt_sender):
        print('flashing left')
        mqtt_sender.send_message('flash_left')

    def handle_flash_right(mqtt_sender):
        print('flashing right')
        mqtt_sender.send_message('flash_right')

    def handle_both(mqtt_sender):
        print('flashing both')
        mqtt_sender.send_message('flash_both')

    def handle_LED_off(mqtt_sender):
        print('turning off')
        mqtt_sender.send_message('LED_off')


    def handle_camera_print(mqtt_sender):
        print('getting_blob')
        mqtt_sender.send_message('getting_blob')

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    grid_frames(teleop_frame,arm_frame,control_frame)

    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    root.mainloop()

def handle_clockwise(mqtt_client):
    print('clockwise')
    mqtt_client.send_message('spin_clockwise_until_sees_object')

def handle_counter_clockwise(mqtt_client):
    print('counter-clockwise')
    mqtt_client.send_message('spin_counterclockwise_until_sees_object')

def get_shared_frames(main_frame, mqtt_sender):
    teleop_frame = shared_gui.get_teleoperation_frame(main_frame,mqtt_sender)
    arm_frame = shared_gui.get_arm_frame(main_frame,mqtt_sender)
    control_frame = shared_gui.get_control_frame(main_frame,mqtt_sender)
    return teleop_frame,arm_frame, control_frame


def grid_frames(teleop_frame, arm_frame, control_frame):
    teleop_frame.grid(row = 0, column = 0)
    arm_frame.grid(row = 1, column = 0)
    control_frame.grid(row = 2, column = 0)



# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()