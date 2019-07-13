#include <ros.h>
#include <std_msgs/Float32.h>
#include <Wire.h>
#include "MS5837.h"
#include <Adafruit_BMP085.h>
#include <Adafruit_GFX.h>
#include <Adafruit_NeoMatrix.h>
#include <Adafruit_NeoPixel.h>
#ifndef PSTR
 #define PSTR // Make Arduino Due happy
#endif

#define DISPLAY_PIN A7

Adafruit_NeoMatrix matrix = Adafruit_NeoMatrix(32, 8, DISPLAY_PIN,
 NEO_MATRIX_TOP   + NEO_MATRIX_LEFT +
 NEO_MATRIX_COLUMNS + NEO_MATRIX_ZIGZAG,
 NEO_GRB      + NEO_KHZ800);

Adafruit_BMP085 bmp180;

MS5837 sensor;

ros::NodeHandle nh;

std_msgs::Float32 temperatura1;
std_msgs::Float32 temperatura2;
ros::Publisher temp1("temperatura1", &temperatura1);
ros::Publisher temp2("temperatura2", &temperatura2);

std_msgs::Float32 pressao1;
std_msgs::Float32 pressao2;
ros::Publisher pres1("pressao1", &pressao1);
ros::Publisher pres2("pressao2", &pressao2);

std_msgs::Float32 depht1;
std_msgs::Float32 depht2;
ros::Publisher deph1("depht1", &depht1);
ros::Publisher deph2("depht2", &depht2);

std_msgs::Float32 leak;
ros::Publisher leakS("leak", &leak);

float sensores[7] = {0, 0, 0, 0, 0, 0, 0};

#define SOSPIN A2
void setup() {

  nh.getHardware()->setBaud(115200);
  
  Serial.begin(9600);
  matrix.begin();
  matrix.setTextWrap(false);
  matrix.setBrightness(40);
  matrix.setTextColor(matrix.Color(0,0,255));
  pinMode(SOSPIN, INPUT); // sets the digital pin 3 as input


  Serial.println("Starting");
  
  Wire.begin();


  // Initialize pressure sensor
  // Returns true if initialization was successful
  // We can't continue with the rest of the program unless we can initialize the sensor
  if (!bmp180.begin()) 
  {
    Serial.println("Sensor nao encontrado !!");
    while (1) {}
  }
  
  while (!sensor.init()) {
    Serial.println("Init failed!");
    Serial.println("Are SDA/SCL connected correctly?");
    Serial.println("Blue Robotics Bar30: White=SDA, Green=SCL");
    Serial.println("\n\n\n");
    delay(5000);
  }
  
  sensor.setModel(MS5837::MS5837_30BA);
  sensor.setFluidDensity(997); // kg/m^3 (freshwater, 1029 for seawater)
  
  nh.initNode();
  nh.advertise(temp1);
  nh.advertise(temp2);
  nh.advertise(pres1);
  nh.advertise(pres2);
  nh.advertise(deph1);
  nh.advertise(deph2);
  nh.advertise(leakS);
}

void loop() {
  
  // Leak
  int leakState = digitalRead(SOSPIN); // read the input pin
  if (leakState == HIGH) { // prints “LEAK!” if input pin is high
    Serial.println("LEAK!");
    sensores[6] = 1;
  }
  
  else if (leakState == LOW) { // prints “Dry” if input pin is low
    Serial.println("Dry");
    sensores[6] = 0;
  }
  
  // Blue
  sensor.read();
  matrix.print((sensor.pressure())); 
  matrix.show();
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

  //bmp
  Serial.print("Temperatura : ");
  Serial.print(bmp180.readTemperature(),1);
  Serial.println(" C");
  Serial.print("Altitude : ");
  Serial.print(bmp180.readAltitude());
  Serial.println(" m");
  Serial.print("Pressao : "); 
  Serial.print(bmp180.readPressure());  
  Serial.println(" Pa");
  sensores[3] = bmp180.readTemperature();
  sensores[4] = bmp180.readAltitude();
  sensores[5] = bmp180.readPressure();

  temperatura1.data = sensores[1];
  temperatura2.data = sensores[3];
  temp1.publish( &temperatura1);
  temp2.publish( &temperatura2);
  
  pressao1.data = sensores[0];
  pressao2.data = sensores[5];
  pres1.publish( &pressao1);
  pres2.publish( &pressao2);
  
  depht1.data = sensores[2];
  depht2.data = sensores[4];
  deph1.publish( &depht1);
  deph2.publish( &depht2);
  
  leak.data = sensores[6];
  leakS.publish( &leak);

  nh.spinOnce();
}
