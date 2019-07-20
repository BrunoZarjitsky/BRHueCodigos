#include <ros.h>
#include <std_msgs/UInt16MultiArray.h>
#include <std_msgs/Float32.h>
#include <Servo.h>

int led = 13;

byte servoPin[] = {3, 4, 5, 6, 9, 10};
Servo servo0;
Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;
int signal;

//Motores
//3;4;5
//10;9;6

ros::NodeHandle nh;

void messageCB( const std_msgs::UInt16MultiArray& controle){
  servo0.writeMicroseconds(controle.data[0]);
  servo1.writeMicroseconds(controle.data[1]);
  servo2.writeMicroseconds(controle.data[2]);
  servo3.writeMicroseconds(controle.data[3]);
  servo4.writeMicroseconds(controle.data[4]);
  servo5.writeMicroseconds(controle.data[5]);
}

ros::Subscriber<std_msgs::UInt16MultiArray> sub("controleThruster", &messageCB);

void setup() {

  nh.getHardware()->setBaud(115200);

  pinMode(led, OUTPUT);
  digitalWrite(led, HIGH);
  
  servo0.attach(servoPin[0]);
  servo1.attach(servoPin[1]);
  servo2.attach(servoPin[2]);
  servo3.attach(servoPin[3]);
  servo4.attach(servoPin[4]);
  servo5.attach(servoPin[5]);

  servo0.writeMicroseconds(1500); // send "stop" signal to ESC.
  servo1.writeMicroseconds(1500);
  servo2.writeMicroseconds(1500);
  servo3.writeMicroseconds(1500);
  servo4.writeMicroseconds(1500);
  servo5.writeMicroseconds(1500);
  delay(100);
  servo5.writeMicroseconds(1500);
  delay(7000); // delay to allow the ESC to recognize the stopped signal

  nh.initNode();
}

void loop() {
  
  nh.spinOnce();
  delay(1);
}
