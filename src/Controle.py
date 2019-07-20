#!/usr/bin/env python
import rospy
from std_msgs.msg import UInt16MultiArray, Float32
from Tkinter import *

def controleThruster():
    valor = UInt16MultiArray()
    valor.data = [1500, 1500, 1500, 1500, 1500, 1500]
    pub = rospy.Publisher('controleThruster', UInt16MultiArray, queue_size=10)
    rospy.init_node('controleThruster', anonymous=True)
    while not rospy.is_shutdown():
        valor.data[0] = motor1.get()
        valor.data[1] = motor2.get()
        valor.data[2] = motor3.get()
        valor.data[3] = motor4.get()
        valor.data[4] = motor5.get()
        valor.data[5] = motor6.get()
        pub.publish(valor)
        pegandoData()
        root.update()

def pres1CB(data):
    global pressao1
    pressao1 = "%.2f" %data.data

def pres2CB(data):
    global pressao2
    pressao2 =  "%.2f" %data.data

def temp1CB(data):
    global temperatura1
    temperatura1 =  "%.2f" %data.data

def temp2CB(data):
    global temperatura2
    temperatura2 =  "%.2f" %data.data

def deph1CB(data):
    global depht1
    depht1 =  "%.2f" %data.data

def deph2CB(data):
    global depht2
    depht2 =  "%.2f" %data.data

def leakCB(data):
    global leak
    if data.data == 1:
        leak = "LEAK"
    else:
        leak = "DRY"

def pegandoData():
    try:
        rospy.Subscriber("pressao1", Float32, pres1CB)
        pressaoData1["text"] = pressao1
    except:
        pressaoData1["text"] = "---"
    try:
        rospy.Subscriber("pressao2", Float32, pres2CB)
        pressaoData2["text"] = pressao2
    except:
        pressaoData2["text"] = "---"
    try:
        rospy.Subscriber("temperatura1", Float32, temp1CB)
        tempData1["text"] = temperatura1
    except:
        tempData1["text"] = "---"
    try:
        rospy.Subscriber("temperatura2", Float32, temp2CB)
        tempData2["text"] = temperatura2
    except:
        tempData2["text"] = "---"
    try:
        rospy.Subscriber("depht1", Float32, deph1CB)
        dephtData1["text"] = depht1
    except:
        dephtData1["text"] = "---"
    try:
        rospy.Subscriber("depht2", Float32, deph2CB)
        dephtData2["text"] = depht2
    except:
        dephtData2["text"] = "---"
    try:
        rospy.Subscriber("leak", Float32, leakCB)
        leakData["text"] = leak
    except:
        leakData["text"] = "---"


def stopMotor(motor):
    if motor == "1":
        motor1.set(1500)
    if motor == "2":
        motor2.set(1500)
    if motor == "3":
        motor3.set(1500)
    if motor == "4":
        motor4.set(1500)
    if motor == "5":
        motor5.set(1500)
    if motor == "6":
        motor6.set(1500)

def stopTotal():
    for i in range(1, 7):
        stopMotor(str(i))

def sair():
    root.destroy()

root = Tk()
root.title("Teste Dos Motores")
root.geometry("404x800+0+0")
tituloMot1 = Label(root, text = "Motor 1, ESC 3", pady = 5)
#tituloMot1.pack()
tituloMot1.grid(row = 0, column = 0, columnspan=3)
motor1 = Scale(root, from_=1100, to=1900, resolution=50, length=400, orient = HORIZONTAL, tickinterval=200, relief=SOLID)
motor1.set(1500)
#motor1.pack()
motor1.grid(row = 1, column = 0, columnspan=3)
motor1.focus_set()
butMot1 = Button(root, text = "Parar motor 1", command = lambda: stopMotor("1"))
#butMot1.pack()
butMot1.grid(row = 2, column = 0, columnspan=3)

tituloMot2 = Label(root, text = "Motor 2, ESC 4", pady = 5)
#tituloMot2.pack()
tituloMot2.grid(row = 3, column = 0, columnspan=3)
motor2 = Scale(root, from_=1100, to=1900, resolution=50, length=400, orient = HORIZONTAL, tickinterval=200, relief=SOLID)
motor2.set(1500)
#motor2.pack()
motor2.grid(row = 4, column = 0, columnspan=3)
butMot2 = Button(root, text = "Parar motor 2", command = lambda: stopMotor("2"))
#butMot2.pack()
butMot2.grid(row = 5, column = 0, columnspan=3)

tituloMot3 = Label(root, text = "Motor 3, ESC 5", pady = 5)
#tituloMot3.pack()
tituloMot3.grid(row = 6, column = 0, columnspan=3)
motor3 = Scale(root, from_=1100, to=1900, resolution=50, length=400, orient = HORIZONTAL, tickinterval=200, relief=SOLID)
motor3.set(1500)
#motor3.pack()
motor3.grid(row = 7, column = 0, columnspan=3)
butMot3 = Button(root, text = "Parar motor 3", command = lambda: stopMotor("3"))
#butMot3.pack()
butMot3.grid(row = 8, column = 0, columnspan=3)

tituloMot4 = Label(root, text = "Motor 4, ESC 6", pady = 5)
#tituloMot4.pack()
tituloMot4.grid(row = 9, column = 0, columnspan=3)
motor4 = Scale(root, from_=1100, to=1900, resolution=50, length=400, orient = HORIZONTAL, tickinterval=200, relief=SOLID)
motor4.set(1500)
#motor4.pack()
motor4.grid(row = 10, column = 0, columnspan=3)
butMot4 = Button(root, text = "Parar motor 4", command = lambda: stopMotor("4"))
#butMot4.pack()
butMot4.grid(row = 11, column = 0, columnspan=3)

tituloMot5 = Label(root, text = "Motor 5, ESC 9", pady = 5)
#tituloMot5.pack()
tituloMot5.grid(row = 12, column = 0, columnspan=3)
motor5 = Scale(root, from_=1100, to=1900, resolution=50, length=400, orient = HORIZONTAL, tickinterval=200, relief=SOLID)
motor5.set(1500)
#motor5.pack()
motor5.grid(row = 13, column = 0, columnspan=3)
butMot5 = Button(root, text = "Parar motor 5", command = lambda: stopMotor("5"))
#butMot5.pack()
butMot5.grid(row = 14, column = 0, columnspan=3)

tituloMot6 = Label(root, text = "Motor 6, ESC 10", pady = 5)
#tituloMot6.pack()
tituloMot6.grid(row = 15, column = 0, columnspan=3)
motor6 = Scale(root, from_=1100, to=1900, resolution=50, length=400, orient = HORIZONTAL, tickinterval=200, relief=SOLID)
motor6.set(1500)
#motor6.pack()
motor6.grid(row = 16, column = 0, columnspan=3)
butMot6 = Button(root, text = "Parar motor 6", command = lambda: stopMotor("6"))
#butMot6.pack()
butMot6.grid(row = 17, column = 0, columnspan=3)

pressaoTitulo = Label(root, text = "Pressao: ")
#pressaoTitulo.pack()
pressaoTitulo.grid(row = 19, column = 0)
pressaoData1 = Label(root)
#pressaoData1.pack()
pressaoData1.grid(row = 19, column = 1)
pressaoData2 = Label(root)
#pressaoData2.pack()
pressaoData2.grid(row = 19, column = 2)

tempTitulo = Label(root, text = "Temperatura: ")
#tempTitulo.pack()
tempTitulo.grid(row = 20, column = 0)
tempData1 = Label(root)
#tempData1.pack()
tempData1.grid(row = 20, column = 1)
tempData2 = Label(root)
#tempData2.pack()
tempData2.grid(row = 20, column = 2)

dephtTitulo = Label(root, text = "Depht: ")
#dephtTitulo.pack()
dephtTitulo.grid(row = 21, column = 0)
dephtData1 = Label(root)
#dephtData1.pack()
dephtData1.grid(row = 21, column = 1)
dephtData2 = Label(root)
#dephtData2.pack()
dephtData2.grid(row = 21, column = 2)

leakTitulo = Label(root, text = "Leak: ")
#leakTitulo.pack()
leakTitulo.grid(row = 22, column = 0)
leakData = Label(root)
#leakData.pack()
leakData.grid(row = 22, column = 1)

butStop = Button(root, text = "Parar todos motores", command = stopTotal)
#butStop.pack()
butStop.grid(row = 18, column = 0, columnspan=3)

butQuit = Button(root, text = "Sair", command = sair)
#butQuit.pack()
butQuit.grid(row = 23, column = 0, columnspan=3)



if __name__ == "__main__":
    try:
        controleThruster()
    except rospy.ROSInterruptException:
        pass