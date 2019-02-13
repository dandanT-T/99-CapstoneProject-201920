"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Kirk Preston.
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
    root.title('CSSE 120 Capstone Project- Black Op')


    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    main_frame = ttk.Frame(root, padding=10, borderwidth=5, relief="groove")
    main_frame.grid()



    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------
    teleop_frame, arm_frame, control_frame, beep_faster_frame, spin_speed_frame, surface_light_frame = get_shared_frames(main_frame,mqtt_sender)



    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # DONE: Implement and call get_my_frames(...)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    grid_frames(teleop_frame, arm_frame, control_frame, beep_faster_frame, spin_speed_frame, surface_light_frame)


    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    root.mainloop()

    # return main_frame


def get_shared_frames(main_frame, mqtt_sender):
    teleop_frame = shared_gui.get_teleoperation_frame(main_frame, mqtt_sender)
    arm_frame = shared_gui.get_arm_frame(main_frame, mqtt_sender)
    control_frame = shared_gui.get_control_frame(main_frame, mqtt_sender)
    beep_faster_frame = get_more_beep_frame(main_frame,mqtt_sender)
    spin_speed_frame = spin_and_speed_frame(main_frame, mqtt_sender)
    surface_light_frame = line_intensity_follow_frame(main_frame, mqtt_sender)

    return teleop_frame, arm_frame, control_frame, beep_faster_frame, spin_speed_frame, surface_light_frame


def grid_frames(teleop_frame, arm_frame, control_frame, beep_faster_frame, spin_speed_frame, surface_light_frame):
    teleop_frame.grid(row=0, column=0)
    arm_frame.grid(row=1, column=0)
    control_frame.grid(row=2, column=0)
    beep_faster_frame.grid(row=3, column=0)
    spin_speed_frame.grid(row=4, column=0)
    surface_light_frame.grid(row=5, column=0)


    #Local laptop GUI has been implemented


def get_more_beep_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief='groove')
    frame.grid()

    frame_label = ttk.Label(frame, text="Beep with Proximity")
    frame_label.grid(row=0, column=1)

    initial_rate_entry = ttk.Entry(frame, width=9)
    initial_rate_entry.grid(row=2, column=0)
    initial_beeps_per_second_label = ttk.Label(frame, text="Initial Rate")
    initial_beeps_per_second_label.grid(row=1, column=0)
    beep_button = ttk.Button(frame, text="Beep at given rate")
    beep_button.grid(row=2, column=2)

    rate_of_increase_label = ttk.Label(frame, text="Rate of Increase")
    rate_of_increase_label.grid(row=3, column=0)
    rate_of_increase_entry = ttk.Entry(frame, width=9)
    rate_of_increase_entry.grid(row=4, column=0)

    beep_button["command"] = lambda: handle_m3_beep_move(initial_rate_entry, rate_of_increase_entry, mqtt_sender)

    return frame


def spin_and_speed_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief='groove')
    frame.grid()

    frame_label = ttk.Label(frame, text="Spin and Speed")
    frame_label.grid(row = 0, column=1)

    spin_direction_entry = ttk.Entry(frame, width=9)
    spin_direction_entry.grid(row=3, column=1)
    spin_direction_label = ttk.Label(frame, text='Spin Direction')
    spin_direction_label.grid(row=2, column=1)

    spin_speed_entry = ttk.Entry(frame, width=9)
    spin_speed_entry.grid(row=4, column=1)
    spin_speed_label = ttk.Label(frame, text='Spin Speed')
    spin_speed_label.grid(row=5, column=1)

    spin_button = ttk.Button(frame, text="Spin Direction w/ Speed")
    spin_button.grid(row=5, column=0)

    spin_button["command"] = lambda: handle_m3_spin_until_object(spin_direction_entry, spin_speed_entry, mqtt_sender)

    return frame


def line_intensity_follow_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief='groove')
    frame.grid()

    frame_label = ttk.Label(frame, text="Surface Light Intensity")
    frame_label.grid(row=0, column=2)

    line_light_intensity_entry = ttk.Frame(frame, width=9)
    line_light_intensity_entry.grid(row=6, column=2)
    line_light_intensity_label = ttk.Label(frame, text='Light Intensity Threshold')
    line_light_intensity_label.grid(row=7, column=2)

    intensity_button = ttk.Button(frame, text='light intensity threshold')
    intensity_button.grid(row=7, column=1)

    intensity_button["command"] = lambda: handle_m3_line_intensity_follow(line_light_intensity_entry,mqtt_sender)

    return frame


def handle_m3_beep_move(initial_rate_entry, rate_of_increase_entry, mqtt_sender):
    print('I am beeping and moving')
    mqtt_sender.send_message('m3_beep_move',[])


def handle_m3_spin_until_object(spin_direction_entry, spin_speed_entry, mqtt_sender):
    print('I am spinning at set speed')
    mqtt_sender.send_message('m3_spin_until_object', [spin_direction_entry.get(), spin_speed_entry.get()])


def handle_m3_line_intensity_follow(line_light_intensity_entry, mqtt_sender):
    print('I am following surface with set light intensity')
    mqtt_sender.send_message('m3_line_intensity_follow', [])




# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()