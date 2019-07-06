#!/usr/bin/env python
import rospy
from std_msgs.msg import UInt16MultiArray

def controleThruster():
    valor = UInt16MultiArray()
    valor.data = [1500, 1500, 1500, 1500, 1500, 1500]
    pub = rospy.Publisher('controleThruster', UInt16MultiArray, queue_size=10)
    rospy.init_node('controleThruster', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        try:
            valores = input()
        except:
            valores = [1500, 1500, 1500, 1500, 1500, 1500]
        for i in range(len(valores)):
            valor.data[i] = valores[i]
        for i in range(len(valor.data)):
            if valor.data[i] < 1100 or valor.data[i] > 1900:
                valor.data[i] = 1500
        pub.publish(valor)

if __name__ == '__main__':
    try:
        controleThruster()
    except rospy.ROSInterruptException:
        pass