/*
 * Silicon Derby Delaware League
 * First Born v0.1
 * 
 * Test H-bridge & DC motors
 * 
 */

const fwdL = 5; // analog output pins 5,6,10,11
const revL = 6; // analog output pins 5,6,10,11
const fwdR = 10; // analog output pins 5,6,10,11
const revR = 11; // analog output pins 5,6,10,11

void setup() {
  // put your setup code here, to run once:
  // comment out if using PWM
  pinMode(fwdL,OUTPUT);
  pinMode(revL,OUTPUT);
  pinMode(fwdR,OUTPUT);
  pinMode(revR,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  STOP();
  delay(1000);
  
}

void STOP() {
  digitalWrite(fwdL,LOW);
  digitalWrite(fwdR,LOW);
  digitalWrite(revL,LOW);
  digitalWrite(revR,LOW);  
}

void straightFwd() {
  
}

void straightRev() {
  
}

void fwdLeft() {
  
}

void fwdRight() {
  
}

void revLeft() {
  
}

void revRight() {
  
}

void cwSpin() {
  
}

void ccwSpin() {
  
}
