"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Constructs and returns Frame objects for the basics:
  -- teleoperation
  -- arm movement
  -- stopping the robot program

  This code is SHARED by all team members.  It contains both:
    -- High-level, general-purpose methods for a Snatch3r EV3 robot.
    -- Lower-level code to interact with the EV3 robot library.

  Author:  Your professors (for the framework and lower-level code)
    and Kirk Preston, Nelson Rainey, Zhicheng Kai, Yu Xin.
  Winter term, 2018-2019.
"""

import tkinter
from tkinter import ttk
import time
import math


def get_teleoperation_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's motion
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Teleoperation")
    left_speed_label = ttk.Label(frame, text="Left wheel speed (0 to 100)")
    right_speed_label = ttk.Label(frame, text="Right wheel speed (0 to 100)")
    number_of_seconds_label=ttk.Label(frame,text="Number of Seconds")
    given_number_of_inches_label=ttk.Label(frame,text="Go Straight for Number of Inches")
    given_speed_label=ttk.Label(frame,text="Go Straight at This Speed")

    left_speed_entry = ttk.Entry(frame, width=8)
    left_speed_entry.insert(0, "100")
    right_speed_entry = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.insert(0, "100")
    given_number_of_seconds_entry=ttk.Entry(frame,width=10)
    given_number_of_inches_entry=ttk.Entry(frame,width=10)
    given_speed_entry=ttk.Entry(frame,width=10)

    forward_button = ttk.Button(frame, text="Forward")
    backward_button = ttk.Button(frame, text="Backward")
    left_button = ttk.Button(frame, text="Left")
    right_button = ttk.Button(frame, text="Right")
    stop_button = ttk.Button(frame, text="Stop")
    go_straight_for_seconds_button=ttk.Button(frame,text="Go Straight for Seconds")
    time_approach_button=ttk.Button(frame,text="Time approach")
    encoder_approach_button=ttk.Button(frame,text="Encoder approach")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    left_speed_label.grid(row=1, column=0)
    right_speed_label.grid(row=1, column=2)
    left_speed_entry.grid(row=2, column=0)
    right_speed_entry.grid(row=2, column=2)

    forward_button.grid(row=3, column=1)
    left_button.grid(row=4, column=0)
    stop_button.grid(row=4, column=1)
    right_button.grid(row=4, column=2)
    backward_button.grid(row=5, column=1)

    given_speed_label.grid(row=6,column=1)
    given_speed_entry.grid(row=7,column=1)
    number_of_seconds_label.grid(row=8,column=0)
    given_number_of_seconds_entry.grid(row=9,column=0)
    given_number_of_inches_label.grid(row=10,column=1)
    go_straight_for_seconds_button.grid(row=9, column=2)
    given_number_of_inches_entry.grid(row=11,column=1)
    time_approach_button.grid(row=11,column=0)
    encoder_approach_button.grid(row=11,column=2)

    # Set the button callbacks:
    forward_button["command"] = lambda: handle_forward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    backward_button["command"] = lambda: handle_backward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    left_button["command"] = lambda: handle_left(
        left_speed_entry, right_speed_entry, mqtt_sender)
    right_button["command"] = lambda: handle_right(
        left_speed_entry, right_speed_entry, mqtt_sender)
    stop_button["command"] = lambda: handle_stop(mqtt_sender)
    go_straight_for_seconds_button["command"]=lambda: handle_go_straight_for_seconds(
        given_number_of_seconds_entry,given_speed_entry,mqtt_sender)
    time_approach_button["command"]=lambda: handle_go_straight_using_time_approach(
        given_number_of_inches_entry,given_speed_entry,mqtt_sender)
    encoder_approach_button["command"]=lambda: handle_go_straight_using_encoder_approach(
        given_number_of_inches_entry,given_speed_entry,mqtt_sender)


    return frame


def get_arm_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's Arm
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Arm and Claw")
    position_label = ttk.Label(frame, text="Desired arm position:")
    position_entry = ttk.Entry(frame, width=8)

    raise_arm_button = ttk.Button(frame, text="Raise arm")
    lower_arm_button = ttk.Button(frame, text="Lower arm")
    calibrate_arm_button = ttk.Button(frame, text="Calibrate arm")
    move_arm_button = ttk.Button(frame,
                                 text="Move arm to position (0 to 5112)")
    blank_label = ttk.Label(frame, text="")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    position_label.grid(row=1, column=0)
    position_entry.grid(row=1, column=1)
    move_arm_button.grid(row=1, column=2)

    blank_label.grid(row=2, column=1)
    raise_arm_button.grid(row=3, column=0)
    lower_arm_button.grid(row=3, column=1)
    calibrate_arm_button.grid(row=3, column=2)

    # Set the Button callbacks:
    raise_arm_button["command"] = lambda: handle_raise_arm(mqtt_sender)
    lower_arm_button["command"] = lambda: handle_lower_arm(mqtt_sender)
    calibrate_arm_button["command"] = lambda: handle_calibrate_arm(mqtt_sender)
    move_arm_button["command"] = lambda: handle_move_arm_to_position(
        position_entry, mqtt_sender)

    return frame


def get_control_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame has
    Button objects to exit this program and/or the robot's program (via MQTT).
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Control")
    quit_robot_button = ttk.Button(frame, text="Stop the robot's program")
    exit_button = ttk.Button(frame, text="Stop this and the robot's program")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    quit_robot_button.grid(row=1, column=0)
    exit_button.grid(row=1, column=2)

    # Set the Button callbacks:
    quit_robot_button["command"] = lambda: handle_quit(mqtt_sender)
    exit_button["command"] = lambda: handle_exit(mqtt_sender)

    return frame

def get_sound_frame(window,mqtt_sender):
    frame=ttk.Frame(window,padding=10,borderwidth=5,relief="ridge")
    frame.grid()

    frame_label=ttk.Label(frame,text="Sound System")
    frame_label.grid(row=0,column=1)

    number_of_times_entry=ttk.Entry(frame,width=9)
    number_of_times_entry.grid(row=2,column=0)
    beep_times_label=ttk.Label(frame,text="Times")
    beep_times_label.grid(row=1,column=0)
    beep_button=ttk.Button(frame,text="Beep for given times")
    beep_button.grid(row=2,column=2)

    frequency_label=ttk.Label(frame,text="Frequency")
    frequency_label.grid(row=3,column=0)
    duration_label=ttk.Label(frame,text="Duration")
    duration_label.grid(row=3,column=1)
    given_frequency_entry=ttk.Entry(frame,width=9)
    given_frequency_entry.grid(row=4,column=0)
    given_duration_entry=ttk.Entry(frame,width=9)
    given_duration_entry.grid(row=4,column=1)
    play_a_tone_button=ttk.Button(frame,text="Play a tone")
    play_a_tone_button.grid(row=4,column=2)

    phrase_label=ttk.Label(frame,text="Phrase")
    phrase_label.grid(row=5,column=0)
    given_phrase_entry=ttk.Entry(frame,width=9)
    given_phrase_entry.grid(row=6,column=0)
    speak_phrase_button=ttk.Button(frame,text="Speak a given phrase")
    speak_phrase_button.grid(row=6,column=2)

    beep_button["command"]=lambda: handle_beep_for_times(number_of_times_entry,mqtt_sender)
    play_a_tone_button["command"]=lambda: handle_play_a_tone(given_frequency_entry,given_duration_entry,
                                                             mqtt_sender)
    speak_phrase_button["command"]=lambda: handle_speak_phrase(given_phrase_entry,mqtt_sender)

    return frame


###############################################################################
###############################################################################
# The following specifies, for each Button,
# what should happen when the Button is pressed.
###############################################################################
###############################################################################

###############################################################################
# Handlers for Buttons in the Teleoperation frame.
###############################################################################
def handle_forward(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    with the speeds used as given.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print('Go forward',left_entry_box.get(),right_entry_box.get())
    mqtt_sender.send_message("forward",[left_entry_box.get(),right_entry_box.get()])

def handle_backward(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negatives of the speeds in the entry boxes.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print('Go backward',left_entry_box.get(),right_entry_box.get())
    mqtt_sender.send_message("backward",[left_entry_box.get(),right_entry_box.get()])

def handle_left(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the left entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    l = abs(int(left_entry_box.get()))
    r=abs(int(right_entry_box.get()))
    print('Go left',left_entry_box.get(),right_entry_box.get())
    mqtt_sender.send_message("left",[-l,r])


def handle_right(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the right entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    l = abs(int(left_entry_box.get()))
    r=abs(int(right_entry_box.get()))
    print('Go right',left_entry_box.get(),right_entry_box.get())
    mqtt_sender.send_message("right",[l,-r])


def handle_stop(mqtt_sender):
    """
    Tells the robot to stop.
      :type  mqtt_sender:  com.MqttClient
    """
    print('stop')
    mqtt_sender.send_message('stop')

def handle_go_straight_for_seconds(given_number_of_seconds_entry,given_speed_entry,mqtt_sender):
    print("go_straight_for_seconds")
    mqtt_sender.send_message("go_straight_for_seconds",[given_number_of_seconds_entry.get(),given_speed_entry.get()])

def handle_go_straight_using_time_approach(given_number_of_inches_entry,given_speed_entry,mqtt_sender):
    print("go_straight_using_time_approach")
    mqtt_sender.send_message("go_straight_for_inches_using_time",[given_number_of_inches_entry.get(),
                                                                  given_speed_entry.get()])

def handle_go_straight_using_encoder_approach(given_number_of_inches_entry,given_speed_entry,mqtt_sender):
    print("go_straight_using_encoder_approach")
    mqtt_sender.send_message("go_straight_for_inches_using_encoder",[given_number_of_inches_entry.get(),
                                                                  given_speed_entry.get()])
###next three done by Nelson Rainey###
def handle_beep_for_times(number_of_times_entry,mqtt_sender):
    print('i will beep', number_of_times_entry.get())
    mqtt_sender.send_message('beeping',[number_of_times_entry.get()])

def handle_play_a_tone(given_frequency_entry,given_duration_entry,mqtt_sender):
    print('i am playing', given_frequency_entry.get(), 'for', given_duration_entry.get())
    mqtt_sender.send_message('tone',[given_frequency_entry.get(),given_duration_entry.get()])

def handle_speak_phrase(given_phrase_entry,mqtt_sender):
    print('i am speaking', given_phrase_entry.get())
    mqtt_sender.send_message('phrase',[given_phrase_entry.get()])
###finish nelson work###

###############################################################################
# Handlers for Buttons in the ArmAndClaw frame.
###############################################################################
def handle_raise_arm(mqtt_sender):
    """
    Tells the robot to raise its Arm until its touch sensor is pressed.
      :type  mqtt_sender:  com.MqttClient
    """
    print('raise_arm')
    mqtt_sender.send_message('raise_arm')


def handle_lower_arm(mqtt_sender):
    """
    Tells the robot to lower its Arm until it is all the way down.
      :type  mqtt_sender:  com.MqttClient
    """
    print('lower_arm')
    mqtt_sender.send_message('lower_arm')


def handle_calibrate_arm(mqtt_sender):
    """
    Tells the robot to calibrate its Arm, that is, first to raise its Arm
    until its touch sensor is pressed, then to lower its Arm until it is
    all the way down, and then to mark taht position as position 0.
      :type  mqtt_sender:  com.MqttClient
    """
    print('calibrate_arm')
    mqtt_sender.send_message('calibrate_arm')


def handle_move_arm_to_position(arm_position_entry, mqtt_sender):
    """
    Tells the robot to move its Arm to the position in the given Entry box.
    The robot must have previously calibrated its Arm.
      :type  arm_position_entry  ttk.Entry
      :type  mqtt_sender:        com.MqttClient
    """
    print('move_arm_to_position')
    mqtt_sender.send_message('move_arm_to_position',[arm_position_entry.get()])
###############################################################################
# Handlers for Buttons in the Control frame.
###############################################################################
def handle_quit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
      :type  mqtt_sender:  com.MqttClient
    """
    print('quit')
    mqtt_sender.send_message('quit')



def handle_exit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
    Then exit this program.
      :type mqtt_sender: com.MqttClient
    """
    print('exit')
    handle_quit(mqtt_sender)
    exit()
