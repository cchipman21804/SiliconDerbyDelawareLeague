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
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  STOP();
  Serial.print("STOPPED");
  delay(1000);
  Serial.print("STRAIGHT FORWARD");
  straightFwd();
  delay(1000);
  Serial.print("STRAIGHT REVERSE");
  straightRev();
  delay(1000);
}

void STOP() {
// on/off version
  digitalWrite(fwdL,LOW);
  digitalWrite(fwdR,LOW);
  digitalWrite(revL,LOW);
  digitalWrite(revR,LOW);

// PWM speed control version
//  analogWrite(fwdL,0);
//  analogWrite(fwdR,0);
//  analogWrite(revL,0);
//  analogWrite(revR,0);

}

void straightFwd() {
// on/off version
  digitalWrite(fwdL,HIGH);
  digitalWrite(fwdR,HIGH);
  digitalWrite(revL,LOW);
  digitalWrite(revR,LOW);

// PWM speed control version
//  analogWrite(fwdL,255);
//  analogWrite(fwdR,255);
//  analogWrite(revL,0);
//  analogWrite(revR,0);
  
}

void straightRev() {
  // on/off version
  digitalWrite(fwdL,LOW);
  digitalWrite(fwdR,LOW);
  digitalWrite(revL,HIGH);
  digitalWrite(revR,HIGH);

// PWM speed control version
//  analogWrite(fwdL,0);
//  analogWrite(fwdR,0);
//  analogWrite(revL,255);
//  analogWrite(revR,255);
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
