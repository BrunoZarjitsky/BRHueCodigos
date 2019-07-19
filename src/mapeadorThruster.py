#!/usr/bin/env python
import rospy
from std_msgs.msg import UInt16MultiArray

def iteracao(atual, anterior):
    if atual > anterior:
        return anterior + 1
    elif atual < anterior:
        return anterior - 1
    return anterior

def mapeador(data):
    valor.data = map(iteracao, data.data, valor.data)


def main():
    global valor
    valor = UInt16MultiArray()
    valor.data = [1500, 1500, 1500, 1500, 1500, 1500]
    pub = rospy.Publisher("controleThruster", UInt16MultiArray,  queue_size=10)
    rospy.init_node("controleThruster", anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        rospy.Subscriber("mapeadorThruster", UInt16MultiArray, mapeador) 
        rate.sleep()
        pub.publish(valor)
        

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass