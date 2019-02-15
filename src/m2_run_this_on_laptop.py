"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Yu Xin.
  Winter term, 2018-2019.
"""

import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
import shared_gui
import random


def main():
    """
    This code, which must run on a LAPTOP:
      1. Constructs a GUI for my part of the Capstone Project.
      2. Communicates via MQTT with the code that runs on the EV3 robot.
    """
    # -------------------------------------------------------------------------
    # Construct and connect the MQTT Client:
    # -------------------------------------------------------------------------
    mqtt_sender=com.MqttClient()
    mqtt_sender.connect_to_ev3()

    # -------------------------------------------------------------------------
    # The root TK object for the GUI:
    # -------------------------------------------------------------------------
    root=tkinter.Tk()
    root.title("GUI")


    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    main_frame=ttk.Frame(root,padding=10,borderwidth=5)
    main_frame.grid()

    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------
    teleop_frame,arm_frame,control_frame=get_shared_frames(main_frame,mqtt_sender)
    grid_frames(teleop_frame,arm_frame,control_frame)
    sound_frame=shared_gui.get_sound_frame(main_frame,mqtt_sender)
    sound_frame.grid(row=0,column=1)

    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # DO: Implement and call get_my_frames(...)
    tones_frame=make_higher_tones_frame(main_frame,mqtt_sender)
    camera_frame=get_camera_frame(main_frame,mqtt_sender)
    random_frame=get_random_frame(main_frame,mqtt_sender)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    tones_frame.grid(row=1, column=1)
    camera_frame.grid(row=2,column=1)
    random_frame.grid(row=0,column=2)

    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    root.mainloop()


def get_shared_frames(main_frame, mqtt_sender):
    '''
    get frames from shared_gui
    :param main_frame:
    :param mqtt_sender:
    :return:
    '''
    the_teleop_frame=shared_gui.get_teleoperation_frame(main_frame,mqtt_sender)
    the_control_frame=shared_gui.get_control_frame(main_frame,mqtt_sender)
    the_arm_frame=shared_gui.get_arm_frame(main_frame,mqtt_sender)
    return the_teleop_frame,the_arm_frame,the_control_frame


def grid_frames(teleop_frame, arm_frame, control_frame):
    '''
    grid the frames from shared_gui
    :param teleop_frame:
    :param arm_frame:
    :param control_frame:
    :return: Nothing
    '''
    teleop_frame.grid(row=0,column=0)
    arm_frame.grid(row=1,column=0)
    control_frame.grid(row=2,column=0)

def make_higher_tones_frame(main_frame,mqtt_sender):
    '''
    Make a frame about individual frame in feature 9.
    The robot should make tones as it moves, with the tones increasing in frequency as the robot gets closer to the
    object. The user should be able to set the initial and rate of increase of the frequencies via the GUI.
    :param main_frame:
    :param mqtt_sender:
    :return: frame
    '''
    make_tone_frame = ttk.Frame(main_frame, padding=10, borderwidth=5, relief="ridge")
    make_tone_frame.grid()
    make_tone_frame_label = ttk.Label(make_tone_frame, text="Frequency get higher when it is closer")
    make_tone_frame_label.grid(row=0, column=1)

    initial_frequency_label = ttk.Label(make_tone_frame, text="Initial Frequency")
    initial_frequency_label.grid(row=1, column=0)
    rate_of_increase_lable = ttk.Label(make_tone_frame, text="Rate of increase")
    rate_of_increase_lable.grid(row=1, column=1)

    initial_frequency_entry = ttk.Entry(make_tone_frame, width=9)
    initial_frequency_entry.grid(row=2, column=0)
    rate_of_increase_entry = ttk.Entry(make_tone_frame, width=9)
    rate_of_increase_entry.grid(row=2, column=1)

    make_higher_tones_when_get_closer_button = ttk.Button(make_tone_frame, text="Makes tones")
    make_higher_tones_when_get_closer_button.grid(row=2, column=2)
    make_higher_tones_when_get_closer_button["command"] = lambda: handle_higher_tones(initial_frequency_entry.get(),
        rate_of_increase_entry.get(),mqtt_sender)
    return make_tone_frame

def handle_higher_tones(initial_frequency,rate_of_increase,mqtt_sender):
    '''
    handle the message sent by the button and send the message to another function. Give a error when any of the entry
    is blank
    :param initial_frequency: int
    :param rate_of_increase: int
    :param mqtt_sender: mqtt_sender
    :return:
    '''
    print("I am make tones with initial frequency of",initial_frequency," and rate of increase of",rate_of_increase)
    mqtt_sender.send_message("make_higher_tones",[initial_frequency,rate_of_increase])

def get_camera_frame(window,mqtt_sender):
    '''
    provide the camera frame for the GUI
    :param window: ttk.frame
    :param mqtt_sender: mqtt_sender
    :return: None
    '''
    frame=ttk.Frame(window,padding=10, borderwidth=5, relief="ridge")
    frame.grid()
    frame_label=ttk.Label(frame,text="Camera Control")
    frame_label.grid(row=0,column=1)

    speed_of_spin_label = ttk.Label(frame, text="Speed of spin")
    speed_of_spin_label.grid(row=1, column=1)
    speed_of_spin_entry=ttk.Entry(frame,width=9)
    speed_of_spin_entry.grid(row=2,column=1)

    spin_clockwise_button=ttk.Button(frame,text="Camera spins clockwise")
    spin_counterclockwise_button=ttk.Button(frame,text="Camera spins counterclockwise")
    spin_clockwise_button.grid(row=2,column=0)
    spin_counterclockwise_button.grid(row=2,column=2)


    spin_clockwise_button["command"]=lambda: handle_spin_clockwise(speed_of_spin_entry.get(),mqtt_sender)
    spin_counterclockwise_button["command"]=lambda : handle_spin_counterclockwise(speed_of_spin_entry.get(),mqtt_sender)
    return frame

def handle_spin_clockwise(speed,mqtt_sender):
    '''
    let the robot spin clockwise towards the object
    :param speed: int
    :param mqtt_sender: mqtt_sender
    :return: None
    '''
    print("camera spin clockwise")
    mqtt_sender.send_message("spin_clockwise_until_sees_object",[speed])

def handle_spin_counterclockwise(speed,mqtt_sender):
    '''
    let the robot spin counterclockwise towards the object
    :param speed: int
    :param mqtt_sender: mqtt_sender
    :return: None
    '''
    print("camera spin counterclockwise")
    mqtt_sender.send_message("spin_counterclockwise_until_sees_object",[speed])

def get_random_frame(window,mqtt_sender):
    '''
    establish a new frame for random functions
    :param window: ttk.frame
    :param mqtt_sender: mqtt_sender
    :return: None
    '''
    main_frame=ttk.Frame(window,padding=10, borderwidth=5, relief="ridge")
    main_frame.grid()
    frame_label=ttk.Label(main_frame,text="Random Choosing Functions")
    frame_label.grid(row=0,column=1)

    random_functions_button=ttk.Button(main_frame,text="Random functions!!")
    random_functions_button.grid(row=1,column=1)
    random_functions_button["command"]=lambda :handle_random_functions(mqtt_sender)

    return main_frame

def handle_random_functions(mqtt_sender):
    '''
    send messages to random functions in delegate
    :param mqtt_sender: mqtt_sender
    :return: None
    '''
    print("doing random things")
    a=random.randint(1,10)
    mqtt_sender.send_message("m2_random_functions",[a])
# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()