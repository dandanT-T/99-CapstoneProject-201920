# Put whatever you want in this module and do whatever you want with it.
# It exists here as a place where you can "try out" things without harm.

import mqtt_remote_method_calls
import math
import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
import shared_gui

'''def modular_pickup_frame(window, mqtt_sender):
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
    camera_pick_up_button = ttk.Button(frame, text='Lift Object')

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

    lift_button["command"] = lambda: handle_pick_up(mqtt_sender, initial_entry, rate_entry, speed_entry)
    camera_pick_up_button["command"] = lambda: handle_camera_pick_up(mqtt_sender, initial_entry, rate_entry, speed_entry, direction_entry)

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

    greater_intensity_button['command'] = lambda: handle_greater_int(mqtt_sender, intensity_entry)
    smaller_intensity_button['command'] = lambda: handle_smaller_int(mqtt_sender, intensity_entry)
    is_color_button['command'] = lambda: handle_is_color(mqtt_sender, color_entry)
    is_not_color_button['command'] = lambda: handle_is_not_color(mqtt_sender, color_entry)'''


########################################################################################################################

#### All code within the def real thing fall here, while loops to control internal timer and constant intensity measure

def real_thing():
    robot = rosebot.RoseBot()
    delegate = shared_gui_delegate_on_robot.Handler(robot)
    mqtt_reciever = com.MqttClient(delegate)
    mqtt_reciever.connect_to_pc()

    while True:
        # if delegate.stop():
        #     break
        time.sleep(0.1)

    while True:
        start = time.time()
        threshold = 60
        if self.sensor_system.color_sensor.get_reflected_light_intensity() > int(intensity): ### Pass in a set intensity
            ##### Insert Intensity beep function here
            self.m3_beep_on_intensity()
            if time.time() - start > threshold:
                self.m3_robot_die()
                self.m3_reset_game()
            else:



#### All code here represents the function: beep on intensity...., audible feedback alerting user to intensity change

def m3_beep_on_intensity():
    if self.sensor_system.get_reflected_light_intensity() > int(intensity): ### Might be a redundant conditional statement
        beeper = Beeper()
        beeper.beep() ### I only need it to beep twice in succession and then stop

#### This is the robot death sequence

def m3_robot_die():
    self.drive_system.stop()
    phrase = 'I am burning up on this lava, cant take the heat, life fading'
    self.speech_maker.speak(phrase)
    self.raise_arm()
    self.lower_arm()

#### this is the function that resets the game, merely alerts player to move robot back to desirable surface,
def m3_reset_game():
    while True:
        phrase = 'Please move me to a darker surface'
        self.speech_maker.speak(phrase)
        time.sleep(10)
        if self.sensor_system.get_reflected_light_intensity() < int(intensity): #### There's going to be a set intensity
            break

    ### perhaps after this I should call main to restart the game??? ####




