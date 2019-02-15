"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Zhicheng Kai.
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
    root.title('C$$E120 Capstone project,1819')
    # bgColor = "#EDEDED"
    # root.configure(bg=bgColor)

    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    main_frame = ttk.Frame(root,padding = 10, borderwidth = 5, relief = 'groove')
    main_frame.grid()

    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------
    teleop_frame,arm_frame,control_frame,=get_shared_frames(main_frame,mqtt_sender)
    sound_frame=shared_gui.get_sound_frame(main_frame,mqtt_sender)
    tone_frame = shared_gui.make_higher_tones_frame(main_frame,mqtt_sender)
    find_grab_frame = find_and_grab_frame(main_frame,mqtt_sender)
    Turtle_frame = turtle_frame(main_frame,mqtt_sender)
    grid_frames(teleop_frame, arm_frame, control_frame,sound_frame,tone_frame, find_grab_frame,Turtle_frame)

    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # DO: Implement and call get_my_frames(...)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    grid_frames(teleop_frame,arm_frame,control_frame,sound_frame,tone_frame,find_grab_frame,Turtle_frame)

    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    root.mainloop()


def get_shared_frames(main_frame, mqtt_sender):
    teleop_frame = shared_gui.get_teleoperation_frame(main_frame,mqtt_sender)
    arm_frame = shared_gui.get_arm_frame(main_frame,mqtt_sender)
    control_frame = shared_gui.get_control_frame(main_frame,mqtt_sender)
    return teleop_frame, arm_frame, control_frame


def grid_frames(teleop_frame, arm_frame, control_frame,sound_frame,tone_frame, find_and_grab_frame,new):
    teleop_frame.grid(row=0, column=0)
    arm_frame.grid(row=1, column=1)
    control_frame.grid(row=3,column=1)
    sound_frame.grid(row=1, column=0)
    tone_frame.grid(row=0, column=1)
    find_and_grab_frame.grid(row=1, column=2)
    new.grid(row=2,column=2)

    pass

def find_and_grab_frame(main_frame,mqtt_sender):
    frame = ttk.Frame(main_frame)
    frame.grid()

    frame_label = ttk.Label(frame,text='find and grab')
    frame_label.grid(row=0,column=0)
    grab_button = ttk.Button(frame, text='Finding an object and grab it')
    grab_button.grid(row=1,column=0)

    grab_button["command"] = lambda: handle_find_and_grab_frame(mqtt_sender)
    return frame

def handle_find_and_grab_frame(mqtt_sender):
    print("I am find things any trying to grab it")
    mqtt_sender.send_message("spin_and_find")
########################################################
# srint 3 project try
########################################################
def turtle_frame(window,mqtt_sender):
    frame = ttk.Frame(window,padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    turtle_lable = ttk.Label(frame,text='Turtle mode')
    turtle_button = ttk.Button(frame,text='start')

    turtle_lable.grid(row=0, column=0)
    turtle_button.grid(row=1, column=0)

    turtle_button["command"] = lambda: handle_turtle_frame(mqtt_sender)

    return frame

def handle_turtle_frame(mqtt_sender):
    print("I am a rose turtle now")
    mqtt_sender.send_message("rose_turtle")




# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()