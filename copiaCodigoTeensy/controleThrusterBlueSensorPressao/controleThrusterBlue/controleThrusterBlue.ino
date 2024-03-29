#include <ros.h>
#include <std_msgs/UInt16MultiArray.h>
#include <Servo.h>
#include <Wire.h>
#include "MS5837.h"

MS5837 sensor;

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

ros::NodeHandle  nh;

std_msgs::Float32 temperatura1;
ros::Publisher temp1("temperatura1", &temperatura1);

std_msgs::Float32 pressao1;
ros::Publisher pres1("pressao1", &pressao1);

std_msgs::Float32 depht1;
ros::Publisher deph1("depht1", &depht1);

float sensores[4] = {0, 0, 0};

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

  Wire.begin();

  while (!sensor.init()) {
    Serial.println("Init failed!");
    Serial.println("Are SDA/SCL connected correctly?");
    Serial.println("Blue Robotics Bar30: White=SDA, Green=SCL");
    Serial.println("\n\n\n");
    delay(5000);
  }

  sensor.setModel(MS5837::MS5837_30BA);
  sensor.setFluidDensity(997); // kg/m^3 (freshwater, 1029 for seawater)
  
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
  servo5.writeMicroseconds(1650);
  delay(1000);
  servo5.writeMicroseconds(1500);
  delay(7000); // delay to allow the ESC to recognize the stopped signal

  nh.initNode();
  nh.subscribe(sub);
}

void loop() {
  sensor.read();
  Serial.print("Pressure: "); 
  Serial.print(sensor.pressure()); 
  Serial.println(" mbar");
  Serial.print("Temperature: "); 
  Serial.print(sensor.temperature()); 
  Serial.println(" deg C");
  Serial.print("Depth: "); 
  Serial.print(sensor.depth()); 
  Serial.println(" m");
  sensores[0] = sensor.pressure();
  sensores[1] = sensor.temperature();
  sensores[2] = sensor.depth();
  
  temperatura1.data = sensores[1];
  temp1.publish( &temperatura1);
  
  pressao1.data = sensores[0];
  pres1.publish( &pressao1);
  
  depht1.data = sensores[2];
  deph1.publish( &depht1);
  nh.spinOnce();
  delay(1);
}
