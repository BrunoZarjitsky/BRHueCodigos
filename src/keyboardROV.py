#!/usr/bin/env python
from pynput.keyboard import Key, KeyCode, Listener
import rospy
from std_msgs.msg import UInt16MultiArray

front = 1900
back = 1100

def on_press(key):
    #print(key)
    if key == KeyCode.from_char("w"):
        valor.data = [front, 1500, front, front, 1500, front]
    elif key == KeyCode.from_char("s"):
        valor.data = [back, 1500, back, back, 1500, back]
    if key == KeyCode.from_char("a"):
        valor.data = [back, 1500, front, back, 1500, back]
    if key == KeyCode.from_char("d"):
        valor.data = [front, 1500, back, front, 1500, back]
    if key == KeyCode.from_char("q"): #yaw
        valor.data = [back, 1500, front, front, 1500, back]
    if key == KeyCode.from_char("e"): #yaw
        valor.data = [front, 1500, back, back, 1500, front]
    if key == KeyCode.from_char("z"):
        valor.data = [1500, back, 1500, 1500, back, 1500]
    if key == KeyCode.from_char("x"):
        valor.data = [1500, front, 1500, 1500, front, 1500]
    if key == KeyCode.from_char("r"): #pitch
        valor.data = [1500, back, 1500, 1500, front, 1500]
    if key == KeyCode.from_char("f"): #pitch
        valor.data = [1500, front, 1500, 1500, front, 1500]
    pub.publish(valor)

def on_release(key):
    valor.data = [1500, 1500, 1500, 1500, 1500, 1500]
    pub.publish(valor)
    if key == Key.esc:
        # Stop listener
        return False

valor = UInt16MultiArray()
valor.data = [1500, 1500, 1500, 1500, 1500, 1500]
pub = rospy.Publisher('mapeadorThruster', UInt16MultiArray, queue_size=10)
rospy.init_node('mapeadorThruster', anonymous=True)
with Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
