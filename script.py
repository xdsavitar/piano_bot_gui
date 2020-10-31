import win32api,win32con
from pyautogui import *
import pyautogui
import time
import keyboard
import random
#############################################
#Tile 1 X:  711 Y:  718 RGB: (118, 190, 255)#
#Tile 2 X:  864 Y:  705 RGB: (  0,   0,   0)#
#Tile 3 X: 1014 Y:  700 RGB: (150, 157, 255)#
#Tile 4 X: 1151 Y:  740 RGB: (175, 155, 255)#
#############################################

delayforMouse = 0.0
ypixelpos = 700

time.sleep(3)


def mouse_event(x,y):
    global delayforMouse
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print("Clicked a TIle")



def main_loop_script(tilecolor):

    print("Waiting for detection... ")
    while keyboard.is_pressed("f") == False:
        if pyautogui.pixel(740,ypixelpos)[0] == int(tilecolor):
            mouse_event(740,ypixelpos)
        if pyautogui.pixel(864,ypixelpos)[0] == int(tilecolor):
            mouse_event(864,ypixelpos)
        if pyautogui.pixel(1014,ypixelpos)[0] == int(tilecolor):
            mouse_event(1014,ypixelpos)
        if pyautogui.pixel(1151,ypixelpos)[0] == int(tilecolor):
            mouse_event(1151,ypixelpos)
