/*
 * Silicon Derby Delaware League
 * First Born v0.1
 * 
 * Test H-bridge & DC motors
 * 
 */

const byte fwdL = 5; // analog output pins 5,6,10,11
const byte revL = 6; // analog output pins 5,6,10,11
const byte fwdR = 10; // analog output pins 5,6,10,11
const byte revR = 11; // analog output pins 5,6,10,11
const byte LED = 13; // on-board LED

void setup() {
  // put your setup code here, to run once:
  // comment out if using PWM
  pinMode(fwdL,OUTPUT);
  pinMode(revL,OUTPUT);
  pinMode(fwdR,OUTPUT);
  pinMode(revR,OUTPUT);
  pinMode(LED, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  STOP();
  heartBeat();
  Serial.print("STOPPED\n");
  delay(1000);
  Serial.print("STRAIGHT FORWARD\n");
  straightFwd();
  delay(1000);
  STOP();
  heartBeat();
  Serial.print("STOPPED\n");
  delay(1000);
  Serial.print("STRAIGHT REVERSE\n");
  straightRev();
  delay(1000);
  STOP();
  heartBeat();
  Serial.print("STOPPED\n");
  delay(1000);
  Serial.print("FORWARD LEFT\n");
  fwdLeft();
  delay(1000);
  STOP();
  heartBeat();
  Serial.print("STOPPED\n");
  delay(1000);
  Serial.print("FORWARD RIGHT\n");
  fwdRight();
  delay(1000);
  STOP();
  heartBeat();
  Serial.print("STOPPED\n");
  delay(1000);
  Serial.print("CW SPIN\n");
  cwSpin();
  delay(1000);
  STOP();
  heartBeat();
  Serial.print("STOPPED\n");
  delay(1000);
  Serial.print("CCW SPIN\n");
  ccwSpin();
  delay(1000);
/*  
 *   Redundant code
 STOP();
  heartBeat();
  Serial.print("STOPPED\n");
  delay(1000);
 *
 */
  Serial.print("\n ******************** STARTING OVER ******************** \n");
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
// on/off version
  digitalWrite(fwdL,LOW);
  digitalWrite(fwdR,HIGH);
  digitalWrite(revL,LOW);
  digitalWrite(revR,LOW);

// PWM speed control version
//  analogWrite(fwdL,0);
//  analogWrite(fwdR,255);
//  analogWrite(revL,0);
//  analogWrite(revR,0);
}

void fwdRight() {
// on/off version
  digitalWrite(fwdL,HIGH);
  digitalWrite(fwdR,LOW);
  digitalWrite(revL,LOW);
  digitalWrite(revR,LOW);

// PWM speed control version
//  analogWrite(fwdL,255);
//  analogWrite(fwdR,0);
//  analogWrite(revL,0);
//  analogWrite(revR,0);
}

void revLeft() {
// on/off version
  digitalWrite(fwdL,LOW);
  digitalWrite(fwdR,LOW);
  digitalWrite(revL,LOW);
  digitalWrite(revR,HIGH);

// PWM speed control version
//  analogWrite(fwdL,0);
//  analogWrite(fwdR,0);
//  analogWrite(revL,0);
//  analogWrite(revR,255);
}

void revRight() {
// on/off version
  digitalWrite(fwdL,LOW);
  digitalWrite(fwdR,LOW);
  digitalWrite(revL,HIGH);
  digitalWrite(revR,LOW);

// PWM speed control version
//  analogWrite(fwdL,0);
//  analogWrite(fwdR,0);
//  analogWrite(revL,255);
//  analogWrite(revR,0);
}

void cwSpin() {
// on/off version
  digitalWrite(fwdL,HIGH);
  digitalWrite(fwdR,LOW);
  digitalWrite(revL,LOW);
  digitalWrite(revR,HIGH);

// PWM speed control version
//  analogWrite(fwdL,255);
//  analogWrite(fwdR,0);
//  analogWrite(revL,0);
//  analogWrite(revR,255);
}

void ccwSpin() {
// on/off version
  digitalWrite(fwdL,LOW);
  digitalWrite(fwdR,HIGH);
  digitalWrite(revL,HIGH);
  digitalWrite(revR,LOW);

// PWM speed control version
//  analogWrite(fwdL,0);
//  analogWrite(fwdR,255);
//  analogWrite(revL,255);
//  analogWrite(revR,0);
}

void heartBeat() {
  digitalWrite(LED,HIGH);
  delay(250);
  digitalWrite(LED,LOW);
  delay(250);
  digitalWrite(LED,HIGH);
  delay(250);
  digitalWrite(LED,LOW);
  delay(500);
  digitalWrite(LED,HIGH);
  delay(250);
  digitalWrite(LED,LOW);
  delay(250);
  digitalWrite(LED,HIGH);
  delay(250);
  digitalWrite(LED,LOW);
}
