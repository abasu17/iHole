#include <Servo.h>

Servo lockController;         // create servo object to control a servo  

void setup() 
{ 
  lockController.attach(9);  // attaches the servo on pin 9 to the servo object 
  lockController.write(0);   // initially servo position in 0
  Serial.begin(9600);        // connect serial with baud rate 9600
} 
 
 
void loop() 
{ 
  if ((int)Serial.read() > 0){ // check if serial have some signal
    lockController.write(Serial.read() + 90); // write signal on servo
    delay(15000);  // wait for 15 secs after open lock
    lockController.write(0);  // again move servo to 0 position
  } 
}
