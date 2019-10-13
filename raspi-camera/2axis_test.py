#!/usr/bin/python
# -*- coding: utf-8 -*-
import pigpio
import time
pi = pigpio.pi()
#x_move:range600-22250
#y_move:range1100-1800
def move(x_move, y_move):
    #print('x_move: ', x_move)
    #print('y_move: ', y_move)
    pi.set_servo_pulsewidth(4, x_move)
    pi.set_servo_pulsewidth(17, y_move)
 
#X,Yのサーボで稼働させる範囲。適当によさげな範囲を選んだ
X_MAX = 2050
X_MIN = 800
X_HOME = 1450
 
Y_MAX = 1800
Y_MIN = 1100
Y_HOME = 1450
 
if __name__ == '__main__':
    move(X_HOME, Y_HOME)
    time.sleep(2)
    move(X_MIN, Y_HOME)
    time.sleep(2)
    move(X_MAX, Y_HOME)
    time.sleep(2)
    move(X_HOME, Y_HOME)
    time.sleep(2)
    move(X_HOME, Y_MIN)
    time.sleep(2)
    move(X_HOME, Y_MAX)
    time.sleep(2)
    move(X_HOME, Y_HOME)