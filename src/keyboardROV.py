#!/usr/bin/env python
from pynput.keyboard import Key, KeyCode, Listener
import rospy
from std_msgs.msg import UInt16MultiArray

full = 1600
empt = 1400

def on_press(key):
    #print(key)
    if key == KeyCode.from_char("w"):
        valor.data = [full, 1500, full, full, 1500, full]
    elif key == KeyCode.from_char("s"):
        valor.data = [empt, 1500, empt, empt, 1500, empt]
    if key == KeyCode.from_char("a"):
        valor.data = [empt, 1500, full, full, 1500, empt]
    if key == KeyCode.from_char("d"): #Erro
        valor.data = [full, 1500, empt, full, 1500, empt]
    if key == KeyCode.from_char("q"): #Erro
        valor.data = [empt, 1500, full, full, 1500, empt]
    if key == KeyCode.from_char("e"):
        valor.data = [full, 1500, empt, empt, 1500, full]
    if key == KeyCode.from_char("z"):
        valor.data = [1500, empt, 1500, 1500, empt, 1500]
    if key == KeyCode.from_char("x"):
        valor.data = [1500, full, 1500, 1500, full, 1500]
    pub.publish(valor)

def on_release(key):
    valor.data = [1500, 1500, 1500, 1500, 1500, 1500]
    pub.publish(valor)
    if key == Key.esc:
        # Stop listener
        return False

valor = UInt16MultiArray()
valor.data = [1500, 1500, 1500, 1500, 1500, 1500]
pub = rospy.Publisher('controleThruster', UInt16MultiArray, queue_size=10)
rospy.init_node('controleThruster', anonymous=True)
with Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()

# def sla():
#     global valor
#     valor = UInt16MultiArray()
#     valor.data = [1500, 1500, 1500, 1500, 1500, 1500]
#     pub = rospy.Publisher('thruster', UInt16MultiArray, queue_size=10)
#     rospy.init_node('controleThruster', anonymous=True)
#     while not rospy.is_shutdown():
#         pub.publish(valor)