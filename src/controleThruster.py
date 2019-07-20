#!/usr/bin/env python
import rospy
from std_msgs.msg import UInt16MultiArray
from robosub_msgs.msg import thruster


def transformacao(x):
    if x == 0:
        return 1500
    elif x>0:
        return int(1500+(x*400))
    else:
        return int(1500-(abs(x)*400))

def regra3(data):
    valor.data = map(transformacao, data.data)
    

def thruster1():
    global valor
    valor = UInt16MultiArray()
    valor.data = [1500, 1500, 1500, 1500, 1500, 1500]
    pub = rospy.Publisher('controleThruster', UInt16MultiArray, queue_size=10)
    rospy.init_node('controleThruster', anonymous=True)
    pub.publish(valor)
    rospy.Subscriber("thruster", thruster, regra3)
    rospy.spin()

if __name__ == '__main__':
    try:
        thruster1()
    except rospy.ROSInterruptException:
        pass