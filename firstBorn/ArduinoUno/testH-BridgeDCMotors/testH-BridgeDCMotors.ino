/*
 * Silicon Derby Delaware League
 * First Born v0.1
 * 
 * Test H-bridge & DC motors
 * 
 */

const byte spdL = 3; // analog output pins 3,5,6,9,10,11
const byte dirL = 4; // analog output pins 3,5,6,9,10,11
const byte spdR = 6; // analog output pins 3,5,6,9,10,11
const byte dirR = 7; // analog output pins 3,5,6,9,10,11
const byte LED = LED_BUILTIN;// 13; // on-board LED

// Set motor speed (if using PWM)
const float s = 1.0; // 1.0 = full speed
const int spd = int(255 * s);

// Set time duration of motor command
const int d = 2000; // in milliseconds

void setup() {
  // put your setup code here, to run once:
  // comment out if using PWM
  //pinMode(spdL,OUTPUT);
  pinMode(dirL,OUTPUT);
  //pinMode(spdR,OUTPUT);
  pinMode(dirR,OUTPUT);
  pinMode(LED, OUTPUT);
  Serial.begin(9600);
  randomSeed(analogRead(0)); // Get a random seed from noise on analog input 0
  //STOP();
}

void loop() {
  // put your main code here, to run repeatedly:
  STOP();
// Pick a random number & execute a corresponding function
  //int randNum = random(9); // uncomment this line for a random walk
  for (int randNum = 0; randNum < 9; randNum++) { // comment out this for loop for a random walk
  switch (randNum) {
    case 0:
      STOP();
      break;
    case 1:
      straightFwd();
      STOP();
      break;
    case 2:
      straightRev();
      STOP();
      break;
    case 3:
      fwdLeft();
      STOP();
      break;
    case 4:
      fwdRight();
      STOP();
      break;
    case 5:
      revLeft();
      STOP();
      break;
    case 6:
      revRight();
      STOP();
      break;
    case 7:
      cwSpin();
      STOP();
      break;
    case 8:
      ccwSpin();
      STOP();
      break;
    default:
      Serial.print("ERROR");
      break;
  } // end switch-case
  
  } // end for loop -- comment out this for loop for a random walk
  
  //Serial.print("\n ******************** STARTING OVER ******************** \n");
}

void STOP() {
  analogWrite(spdL,0);    // Set speed of left motor to zero
  digitalWrite(dirL,LOW);
  analogWrite(spdR,0);    // Set speed of right motor to zero
  digitalWrite(dirR,LOW);
  heartBeat();
  Serial.print("STOPPED\n");
  delay(d);

}

void straightFwd() {
  analogWrite(spdL,spd);
  digitalWrite(dirL,LOW); // Set direction to forward
  analogWrite(spdR,spd);
  digitalWrite(dirR,LOW); // Set direction to forward
  Serial.print("STRAIGHT FORWARD\n");
  delay(d);
  
}

void straightRev() {
  analogWrite(spdL,spd);
  digitalWrite(dirL,HIGH); // Set direction to reverse
  analogWrite(spdR,spd);
  digitalWrite(dirR,HIGH); // Set direction to reverse
  Serial.print("STRAIGHT REVERSE\n");
  delay(d);

}

void fwdRight() {
  analogWrite(spdL,spd);
  digitalWrite(dirL,LOW); // Set direction to forward
  analogWrite(spdR,0);
  digitalWrite(dirR,LOW);
  Serial.print("FORWARD RIGHT\n");
  delay(d);

}

void fwdLeft() {
  analogWrite(spdL,0);
  digitalWrite(dirL,LOW);
  analogWrite(spdR,spd);
  digitalWrite(dirR,LOW); // Set direction to forward
  Serial.print("FORWARD LEFT\n");
  delay(d);

}

void revLeft() {
  analogWrite(spdL,spd);
  digitalWrite(dirL,HIGH); // Set direction to reverse
  analogWrite(spdR,0);
  digitalWrite(dirR,LOW);
  Serial.print("REVERSE LEFT\n");
  delay(d);
  
}

void revRight() {
  analogWrite(spdL,0);
  digitalWrite(dirL,LOW);
  analogWrite(spdR,spd);
  digitalWrite(dirR,HIGH); // Set direction to reverse
  Serial.print("REVERSE RIGHT\n");
  delay(d);
  
}

void cwSpin() {
  analogWrite(spdL,spd);
  digitalWrite(dirL,LOW); // Set direction to forward
  analogWrite(spdR,spd);
  digitalWrite(dirR,HIGH); // Set direction to reverse
  Serial.print("CW SPIN\n");
  delay(d);

}

void ccwSpin() {
  analogWrite(spdL,spd);
  digitalWrite(dirL,HIGH); // Set direction to reverse
  analogWrite(spdR,spd);
  digitalWrite(dirR,LOW); // Set direction to forward
  Serial.print("CCW SPIN\n");
  delay(d);

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
