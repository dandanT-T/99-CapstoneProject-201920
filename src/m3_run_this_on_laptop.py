"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Kirk Preston.
  Winter term, 2018-2019.
"""


#### THIS FILE IS DONE
#### NO MORE ACTION REQUIRED

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
    root.title('Robot Operation Console')


    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    main_frame = ttk.Frame(root, padding=10, borderwidth=5, relief="groove")
    main_frame.grid()



    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------
    teleop_frame, arm_frame, control_frame, modular_frame, surface_frame = get_shared_frames(main_frame,mqtt_sender)



    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # DONE: Implement and call get_my_frames(...)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    grid_frames(teleop_frame, arm_frame, control_frame, modular_frame, surface_frame)


    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    root.mainloop()

    # return main_frame


def get_shared_frames(main_frame, mqtt_sender):
    teleop_frame = shared_gui.get_teleoperation_frame(main_frame, mqtt_sender)
    arm_frame = shared_gui.get_arm_frame(main_frame, mqtt_sender)
    control_frame = shared_gui.get_control_frame(main_frame, mqtt_sender)
    modular_frame = modular_pickup_frame(main_frame,mqtt_sender)
    surface_frame = surface_color_frame(main_frame, mqtt_sender)


    return teleop_frame, arm_frame, control_frame, modular_frame, surface_frame


def grid_frames(teleop_frame, arm_frame, control_frame, modular_frame,surface_frame):
    teleop_frame.grid(row=0, column=0)
    arm_frame.grid(row=1, column=0)
    control_frame.grid(row=2, column=0)
    modular_frame.grid(row=1, column=2)
    surface_frame.grid(row=0, column=2)



    #Local laptop GUI has been implemented



def modular_pickup_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief='groove')
    frame.grid()

    frame_label = ttk.Label(frame, text='Pick Up Objects')
    speed_label = ttk.Label(frame, text='Speed')
    direction_label = ttk.Label(frame, text='Direction: CW or CWW')
    initial_label = ttk.Label(frame, text='Initial Rate:')
    rate_label = ttk.Label(frame, text='Increase Rate:')

    speed_entry = ttk.Entry(frame, width=9)
    direction_entry = ttk.Entry(frame, width=9)
    initial_entry = ttk.Entry(frame, width=9)
    rate_entry = ttk.Entry(frame, width=9)

    lift_button = ttk.Button(frame, text='Lift Object')
    camera_pick_up_button = ttk.Button(frame, text='Camera Lift Object')

    frame_label.grid(row=0, column=1)
    speed_label.grid(row=1, column=0)
    direction_label.grid(row=2, column=0)
    initial_label.grid(row=3, column=0)
    rate_label.grid(row=4, column=0)
    speed_entry.grid(row=1, column=2)
    direction_entry.grid(row=2, column=2)
    initial_entry.grid(row=3, column=2)
    rate_entry.grid(row=4, column=2)
    lift_button.grid(row=5, column=0)
    camera_pick_up_button.grid(row=5, column=2)

    lift_button["command"] = lambda: handle_m3_beep_move( initial_entry, rate_entry, speed_entry, mqtt_sender)
    camera_pick_up_button["command"] = lambda: handle_m3_spin_until_object(direction_entry, speed_entry, mqtt_sender)

    return frame


def surface_color_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief='groove')
    frame.grid()

    frame_label = ttk.Label(frame, text='Color Sensor')
    intensity_label = ttk.Label(frame, text='Intensity')
    color_label = ttk.Label(frame, text='Color')
    go_label = ttk.Label(frame, text='Go Until')
    blank_label= ttk.Label(frame, text='')
    go_to_label= ttk.Label(frame, text='Go Until')

    intensity_entry = ttk.Entry(frame, width=9)
    color_entry = ttk.Entry(frame, width=9)

    greater_intensity_button = ttk.Button(frame, text='Intensity Greater than:')
    smaller_intensity_button = ttk.Button(frame, text='Intensity Smaller than:')
    is_color_button = ttk.Button(frame, text='Color is')
    is_not_color_button = ttk.Button(frame, text='Color is Not')

    frame_label.grid(row=0, column=3)
    intensity_label.grid(row=1, column=0)
    intensity_entry.grid(row=1, column=1)
    color_label.grid(row=3, column=0)
    color_entry.grid(row=3, column=1)
    go_label.grid(row=1, column=2)
    go_to_label.grid(row=3, column=2)
    greater_intensity_button.grid(row=1, column=3)
    smaller_intensity_button.grid(row=1, column=4)
    is_color_button.grid(row=3, column=3)
    is_not_color_button.grid(row=3, column=4)
    blank_label.grid(row=2, column=0)

    greater_intensity_button['command'] = lambda: handle_m3_greater_intensity(mqtt_sender, intensity_entry)
    smaller_intensity_button['command'] = lambda: handle_m3_smaller_intensity(mqtt_sender, intensity_entry)
    is_color_button['command'] = lambda: handle_m3_color_true(mqtt_sender, color_entry)
    is_not_color_button['command'] = lambda: handle_m3_color_false(mqtt_sender, color_entry)

    return frame

def handle_m3_greater_intensity(mqtt_sender, intensity_entry):
    print('This color has intensity')
    mqtt_sender.send_message('m3_greater_intensity', [intensity_entry.get()])

def handle_m3_smaller_intensity(mqtt_sender, intensity_entry):
    print('This color has intensity')
    mqtt_sender.send_message('m3_smaller_intensity', [intensity_entry.get()])

def handle_m3_color_true(mqtt_sender, color_entry):
    print('This is the color wanted')
    mqtt_sender.send_message('m3_color_true', [color_entry.get()])

def handle_m3_color_false(mqtt_sender, color_entry):
    print('This is not the color wanted')
    mqtt_sender.send_message('m3_color_false', [color_entry.get()])

def handle_m3_beep_move(initial_entry, rate_entry, speed_entry, mqtt_sender):
    print('I am beeping and moving')
    mqtt_sender.send_message('m3_beep_move',[initial_entry.get(), rate_entry.get(), speed_entry.get()])


def handle_m3_spin_until_object(direction_entry, speed_entry, mqtt_sender):
    print('I am spinning at set speed')
    mqtt_sender.send_message('m3_spin_until_object', [direction_entry.get(), speed_entry.get()])





# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()