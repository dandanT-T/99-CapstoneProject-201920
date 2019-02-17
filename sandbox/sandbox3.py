# Put whatever you want in this module and do whatever you want with it.
# It exists here as a place where you can "try out" things without harm.

import mqtt_remote_method_calls
import math
import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
import shared_gui




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


#### this is the keyboard code

def controller_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief='groove')
    frame.grid()

    frame_label = ttk.Label(frame, text='Robot Controller')
    speed_label = ttk.Label(frame, text='Drive Speed')
    color_threshold_label = ttk.Label(frame, text='Color Intensity')
    timer_countdown_label = ttk.Label(frame, text='Timer Countdown')

    speed_entry = ttk.Entry(frame, width=9)
    timer_countdown_entry = ttk.Entry(frame, width=9)
    color_threshold_entry = ttk.Entry(frame, width=9)

    set_parameters_button = ttk.Button(frame, text='Set')
    quit_game_button = ttk.Button(frame, text='Quit Game')
    reset_game_button = ttk.Button(frame, text='Reset Game')

    ####these buttons are for controlling the robot####

    #### Interprets the Keyboard ####
    frame.bind('<Any-KeyPress>', frame.when_pressed)
    frame.bind('<Any-KeyPress>', frame.when_released)
    frame.bind('<1>', lambda event: frame.focus_set())

    w_button = ttk.Button(frame, text='W Forward', width=9)
    a_button = ttk.Button(frame, text='A Left', width=9)
    s_button = ttk.Button(frame, text='S Backward', width=9)
    d_button = ttk.Button(frame, text='D Right', width=9)

    # Controller Button Placement
    w_button.grid(row=6, column=1)
    a_button.grid(row=7, column=0)
    s_button.grid(row=7, column=1)
    d_button.grid(row=7, column=2)

    # Grid Placement
    frame_label.grid(row=0, column=1)
    speed_label.grid(row=1, column=0)
    speed_entry.grid(row=2, column=0)
    set_parameters_button.grid(row=2, column=1)
    color_threshold_label.grid(row=3, column=0)
    color_threshold_entry.grid(row=4, column=0)
    timer_countdown_label.grid(row=3, column=2)
    timer_countdown_entry.grid(row=4, column=2)
    ### Possible Turn Speed Button
    ### Possible Turn Speed Button
    quit_game_button.grid(row=10, column=1)
    reset_game_button.grid(row=11, column=1)


    #lift_button["command"] = lambda: handle_m3_beep_move( initial_entry, rate_entry, speed_entry, mqtt_sender)
    #camera_pick_up_button["command"] = lambda: handle_m3_spin_until_object(direction_entry, speed_entry, mqtt_sender)

def handle_release():
    #handles the key releases with movements
    speed = 0



def when_pressed(frame, event):
    alpha = {
        'w': frame.handle_go_forward(frame, mqtt_remote_method_calls)
        'a': frame.handle_left(frame, )
        's': frame.handle_backward(frame, )
        'd': frame.handle_right(frame, )
    }

def when_released(frame, event):
    frame.handle_release(frame.mqtt_client)
