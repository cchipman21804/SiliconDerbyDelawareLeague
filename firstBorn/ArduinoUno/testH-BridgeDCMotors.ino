/*
 * Silicon Derby Delaware League
 * First Born v0.1
 * 
 * Test H-bridge & DC motors
 * 
 */

const fwdLeft = 5; // analog output pins 5,6,10,11
const revLeft = 6; // analog output pins 5,6,10,11
const fwdRight = 10; // analog output pins 5,6,10,11
const revRight = 11; // analog output pins 5,6,10,11

void setup() {
  // put your setup code here, to run once:
  // comment out if using PWM
  pinMode(fwdLeft,OUTPUT);
  pinMode(revLeft,OUTPUT);
  pinMode(fwdRight,OUTPUT);
  pinMode(revRight,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:

}
