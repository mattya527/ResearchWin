import RPi.GPIO as GPIO
import Adfruit_PCA9685
from time import sleep

set_freq = 50
PWM = Adfruit_PCA9685.PCA9685()
PWM.set_pwm_freq(set_freq)

def convert_deg(deg,freq):
    step = 4096
    max_pulse = 2.4
    min_pulse = 0.5

    center_pulse = (max_pulse - min_pulse) / 2 + min_pulse
    one_pulse = round((max_pulse - min_pulse) / 100,2)
    deg_pulse = center_pulse +deg *  one_pulse
    deg_num = int(deg_pulse / (1.0 / freq * 1000/step))
    print('deg:'+str(deg) + '(' + str(deg_num) +')')
    return deg_num

def palm():
    try:
        while True:
            pwm.set_pwm(0,0,convert_deg(0,set_freq))
            pwm.set_pwm(3,0,convert_deg(0,set_freq))
            pwm.set_pwm(5,0,convert_deg(-45,set_freq))
            pwm.set_pwm(8,0,convert_deg(-90,set_freq))
            pwm.set_pwm(12,0,convert_deg(-60,set_freq))
    except KeyboardInterrupt:
        pwm.set_pwm(0,0,0)
        pwm.set_pwm(3,0,0)
        pwm.set_pwm(5,0,0)
        pwm.set_pwm(8,0,0)
        pwm.set_pwm(12,0,0)
        pass

def l():
    try:
        while True:
            pwm.set_pwm(0,0,convert_deg(-90,set_freq))
            pwm.set_pwm(3,0,convert_deg(0,set_freq))
            pwm.set_pwm(5,0,convert_deg(-95,set_freq))
            pwm.set_pwm(8,0,convert_deg(-90,set_freq))
            pwm.set_pwm(12,0,convert_deg(60,set_freq))
    except KeyboardInterrupt:
        pwm.set_pwm(0,0,0)
        pwm.set_pwm(3,0,0)
        pwm.set_pwm(5,0,0)
        pwm.set_pwm(8,0,0)
        pwm.set_pwm(12,0,0)
        pass

def fist():
    try:
        while True:
            pwm.set_pwm(0, 0, convert_deg(0, set_freq))
            pwm.set_pwm(3, 0, convert_deg(-90, set_freq))
            pwm.set_pwm(5, 0, convert_deg(-95, set_freq))
            pwm.set_pwm(8, 0, convert_deg(-90, set_freq))
            pwm.set_pwm(12, 0, convert_deg(60, set_freq))
    except KeyboardInterrupt:
        pwm.set_pwm(0, 0, 0)
        pwm.set_pwm(3, 0, 0)
        pwm.set_pwm(5, 0, 0)
        pwm.set_pwm(8, 0, 0)
        pwm.set_pwm(12, 0, 0)
        pass

def thumb():
    try:
        while True:
            pwm.set_pwm(0, 0, convert_deg(-90, set_freq))
            pwm.set_pwm(3, 0, convert_deg(-90, set_freq))
            pwm.set_pwm(5, 0, convert_deg(-90, set_freq))
            pwm.set_pwm(8, 0, convert_deg(-90, set_freq))
            pwm.set_pwm(12, 0, convert_deg(60, set_freq))
    except KeyboardInterrupt:
        pwm.set_pwm(0, 0, 0)
        pwm.set_pwm(3, 0, 0)
        pwm.set_pwm(5, 0, 0)
        pwm.set_pwm(8, 0, 0)
        pwm.set_pwm(12, 0, 0)
        pass

def ok():
    try:
        while True:
            pwm.set_pwm(0, 0, convert_deg(0, set_freq))
            pwm.set_pwm(3, 0, convert_deg(-90, set_freq))
            pwm.set_pwm(5, 0, convert_deg(-45, set_freq))
            pwm.set_pwm(8, 0, convert_deg(-90, set_freq))
            pwm.set_pwm(12, 0, convert_deg(-60, set_freq))
    except KeyboardInterrupt:
        pwm.set_pwm(0, 0, 0)
        pwm.set_pwm(3, 0, 0)
        pwm.set_pwm(5, 0, 0)
        pwm.set_pwm(8, 0, 0)
        pwm.set_pwm(12, 0, 0)
        pass

