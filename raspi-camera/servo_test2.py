#!/usr/bin/python

 
import pigpio
import time
 
pi = pigpio.pi()
#-90
pi.set_servo_pulsewidth(17, 1100)
time.sleep(3)
#0
pi.set_servo_pulsewidth(17, 1450)
time.sleep(3)
#90
pi.set_servo_pulsewidth(17, 1800)
time.sleep(3)

pi.set_servo_pulsewidth(17, 1450)
