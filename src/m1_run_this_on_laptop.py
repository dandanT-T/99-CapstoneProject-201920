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
import math


def main():
    """
    This code, which must run on a LAPTOP:
      1. Constructs a GUI for my part of the Capstone Project.
      2. Communicates via MQTT with the code that runs on the EV3 robot.
    """
    # -------------------------------------------------------------------------
    # Construct and connect the MQTT Client:
    # -------------------------------------------------------------------------
    root = tkinter.Tk()
    delegate = Delegate_on_laptop(root)
    mqtt_sender = com.MqttClient(delegate)
    mqtt_sender.connect_to_ev3()
    # -------------------------------------------------------------------------
    # The root TK object for the GUI:
    # -------------------------------------------------------------------------

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
    # teleop_frame,arm_frame,control_frame,=get_shared_frames(main_frame,mqtt_sender)
    # sound_frame=shared_gui.get_sound_frame(main_frame,mqtt_sender)
    # tone_frame = shared_gui.make_higher_tones_frame(main_frame,mqtt_sender)
    # find_grab_frame = find_and_grab_frame(main_frame,mqtt_sender)
    control_frame = shared_gui.get_control_frame(main_frame, mqtt_sender)
    turtle_frames = turtle_frame(main_frame,mqtt_sender)
    grid_frames(control_frame, turtle_frames)

    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # DO: Implement and call get_my_frames(...)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    grid_frames(control_frame, turtle_frames)

    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    root.mainloop()


def get_shared_frames(main_frame, mqtt_sender):
    teleop_frame = shared_gui.get_teleoperation_frame(main_frame,mqtt_sender)
    arm_frame = shared_gui.get_arm_frame(main_frame,mqtt_sender)
    control_frame = shared_gui.get_control_frame(main_frame,mqtt_sender)
    return teleop_frame, arm_frame, control_frame


def grid_frames(control_frame, turtle_frame):
    # teleop_frame.grid(row=0, column=0)
    # sound_frame.grid(row=1, column=0)
    # tone_frame.grid(row=0, column=1)
    # find_and_grab_frame.grid(row=1, column=2)
    turtle_frame.grid(row=0,column=0)
    control_frame.grid(row=1, column=0)
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


def turtle_frame(main_frame, mqtt_sender):
    frame = ttk.Frame(main_frame, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    turtle_label = ttk.Label(frame, text='Turtle mode')
    turn_label = ttk.Label(frame, text='degree to turn')
    draw_square_length_label = ttk.Label(frame, text='side length')
    draw_square_speed_label = ttk.Label(frame, text='drawing speed')
    draw_circle_radius_label = ttk.Label(frame, text='radius')
    draw_circle_time_label = ttk.Label(frame, text='time')

    turn_entry = ttk.Entry(frame, width=8)
    draw_square_length_entry = ttk.Entry(frame, width=8)
    draw_square_speed_entry = ttk.Entry(frame, width=8)
    draw_circle_radius_spin = ttk.Spinbox(frame,values=(50, 60, 70, 80, 90))
    # draw_circle_radius_spin.pack()
    draw_circle_time_spin = ttk.Spinbox(frame, values=(2 * math.pi))
    # draw_circle_time_spin.pack()

    turn_button = ttk.Button(frame, text='turn')
    draw_square_button = ttk.Button(frame, text='draw a square')
    draw_circle_button = ttk.Button(frame, text='draw a circle')

    turtle_label.grid(row=0, column=1)
    turn_label.grid(row=1, column=0)
    turn_entry.grid(row=2, column=0)
    turn_button.grid(row=2, column=2)
    draw_square_length_label.grid(row=3, column=0)
    draw_square_speed_label.grid(row=3, column=1)
    draw_square_length_entry.grid(row=4, column=0)
    draw_square_speed_entry.grid(row=4, column=1)
    draw_square_button.grid(row=4, column=2)
    draw_circle_radius_label.grid(row=5, column=0)
    draw_circle_time_label.grid(row=5, column=1)
    draw_circle_radius_spin.grid(row=6, column=0, columnspan=4)
    draw_circle_time_spin.grid(row=7, column=0, columnspan=4)
    draw_circle_button.grid(row=8, column=1)

    turn_button["command"] = lambda: handle_turn_frame(mqtt_sender,turn_entry)
    draw_square_button["command"] = lambda: handle_draw_square_button(mqtt_sender,draw_square_length_entry,
                                                                      draw_square_speed_entry)
    draw_circle_button["command"] = lambda: handle_draw_circle_button(mqtt_sender,draw_circle_radius_spin,
                                                                      draw_circle_time_spin)



    return frame


def handle_turn_frame(mqtt_sender,turn_entry):
    print("I am turing")


def handle_draw_square_button(mqtt_sender,draw_square_length_entry,draw_square_speed_entry):
    print("I am drawing a square")
    mqtt_sender.send_message("m1_turtle_square",[draw_square_length_entry.get(),draw_square_speed_entry.get()])


def handle_draw_circle_button(mqtt_sender, draw_circle_radius_spin, draw_circle_time_spin):
    print("I am drawing a circle")
    mqtt_sender.send_message("m1_turtle_circle",[draw_circle_radius_spin.get(), draw_circle_time_spin.get()])


#
class Delegate_on_laptop(object):
    def __init__(self, root):
        self.root = root

    def quit(self):
        self.root.quit()




# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()