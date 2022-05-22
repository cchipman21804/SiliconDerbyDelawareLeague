/*
  Web Server

 A simple web server that shows the value of the analog input pins.
 using an Arduino Wiznet Ethernet shield.

 Circuit:
 * Ethernet shield attached to pins 10, 11, 12, 13
 * Analog inputs attached to pins A0 through A5 (optional)

 created 18 Dec 2009
 by David A. Mellis
 modified 9 Apr 2012
 by Tom Igoe
 modified 02 Sept 2015
 by Arturo Guadalupi
 modified 2022-02-22
 by Werner Rothschopf

https://werner.rothschopf.net/202003_arduino_webserver_post_en.htm
 
 modified 4/29/2022
 by Clifford A Chipman
 */

#include <SPI.h>
#include <Ethernet.h>
#include "ArduinoJson.h"

// https://www.arduino.cc/reference/en/libraries/arduinojson/
// https://arduinojson.org/v6/doc/

const String ver = "2.0b";
const int port = 8080;

// Enter a MAC address and IP address for your controller below.
// The IP address will be dependent on your local network:
byte mac[] = {
  0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED
};
IPAddress ip(192, 168, 1, 177);

// Initialize the Ethernet server library
// with the IP address and port you want to use
// (port 80 is default for HTTP):
EthernetServer server(port);

int tempSensor = A0;  // Temperature sensor connected to A0
// Temperature sensor is a 3K@77F NTC thermistor from BAPI
int lightSensor = A1; // CdS photoresistor connected to A1
int leftEye = A2;     // CdS photoresistor connected to A2
int centerEye = A3;   // CdS photoresistor connected to A3
int rightEye = A4;    // CdS photoresistor connected to A4
int pir = 8;          // PIR sensor connected to digital pin 8

// Measured electrical parameters:
const float supplyVoltage = 5.116; // volts
const int pullupResistor = 1196; // ohms

// variables needed to calculate temperature:
const float adcRes = supplyVoltage / 1024.0;  // resolution of the analog to digital converter in volts
float sensorInputVoltage;
float pullupResistorVoltageDrop;
float sensorResistance;
unsigned long timeStamp;
float degF;
float lightLevel;
float left;
float center;
float right;
boolean occ;
String data = "";

void setup() {
  // Set pir to input with internal pullup resistor
  pinMode(pir, INPUT_PULLUP);
  // You can use Ethernet.init(pin) to configure the CS pin
  Ethernet.init(10);  // Most Arduino shields
  //Ethernet.init(5);   // MKR ETH shield
  //Ethernet.init(0);   // Teensy 2.0
  //Ethernet.init(20);  // Teensy++ 2.0
  //Ethernet.init(15);  // ESP8266 with Adafruit Featherwing Ethernet
  //Ethernet.init(33);  // ESP32 with Adafruit Featherwing Ethernet

  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }
  //Serial.println("Ethernet WebServer Example");

  // start the Ethernet connection and the server:
  Ethernet.begin(mac, ip);

  // Check for Ethernet hardware present
  if (Ethernet.hardwareStatus() == EthernetNoHardware) {
    Serial.println("Ethernet shield was not found.  Sorry, can't run without hardware. :(");
    while (true) {
      delay(1); // do nothing, no point running without Ethernet hardware
    }
  }
  if (Ethernet.linkStatus() == LinkOFF) {
    Serial.println("Ethernet cable is not connected.");
  }

  // start the server & display splash screen
  server.begin();
  Serial.print("OfficeSensors v");
  Serial.println(ver);
  Serial.print("server is at http://");
  Serial.print(Ethernet.localIP());
  Serial.print(":");
  Serial.println(port);
  Serial.println("\r\nListening for connections...");
}

void loop() {
  checkForClient();
}

void checkForClient() {
  // listen for incoming clients
  EthernetClient client = server.available();
  //Serial.println("\r\nListening for connections..."); //This keeps SCROLLING
  if (client) {
    Serial.print(F("\n[server] client connected from "));
    Serial.print(client.remoteIP());
    Serial.print(":");
    Serial.println(client.remotePort());
    Serial.print("Timestamp: ");
    Serial.println(millis());
    uint8_t i = 0;                               // index / current read position
    const uint16_t buffersize = 100;             // size of read buffer (reads a complete line) (if larger than 255, modify i also!
    const uint16_t smallbuffersize = 30;         // a smaller buffer for results
    char lineBuffer[buffersize] {'\0'};          // buffer for incomming data
    char method[8];                              // largest one 7+1. HTTP request methods in RFC7231 + RFC5789: GET HEAD POST PUT DELETE CONNECT OPTONS TRACE PATCH
    char uri[smallbuffersize];                   // the requested page, shorter than smallbuffersize - method
    char requestParameter[smallbuffersize];      // parameter appended to the URI after a ?
    char postParameter[smallbuffersize];         // parameter transmitted in the body / by POST
    enum class Status {REQUEST, CONTENT_LENGTH, EMPTY_LINE, BODY};
    Status status = Status::REQUEST;

    while (client.connected()) {
      while (client.available()) {
        char c = client.read();
        Serial.print(c);     // Debug print received characters to Serial monitor
        if ( c == '\n' )
        {
          if (status == Status::REQUEST)         // read the first line
          {
            //Serial.print(F("lineBuffer="));Serial.println(lineBuffer);
            // now split the input
            char *ptr;
            ptr = strtok(lineBuffer, " ");       // strtok willdestroy the newRequest
            strlcpy(method, ptr, smallbuffersize);
            Serial.print(F("method=")); Serial.println(method);
            ptr = strtok(NULL, " ");
            strlcpy(uri, ptr, smallbuffersize);  // enthält noch evtl. parameter
            if (strchr(uri, '?') != NULL)
            {
              ptr = strtok(uri, "?");  // split URI from parameters
              strcpy(uri, ptr);
              ptr = strtok(NULL, " ");
              strcpy(requestParameter, ptr);
              Serial.print(F("requestParameter=")); Serial.println(requestParameter);
            }
            Serial.print(F("uri=")); Serial.println(uri);
            status = Status::EMPTY_LINE;                   // jump to next status
          }
          else if (status == Status::CONTENT_LENGTH)       // MISSING check for Content-Length
          {
            status = Status::EMPTY_LINE;
          }
          else if (status > Status::REQUEST && i < 2)      // check if we have an empty line
          {
            status = Status::BODY;
          }
          else if (status == Status::BODY)
          {
            strlcpy(postParameter, lineBuffer, smallbuffersize);
            break; // we have received one line payload and break out
          }
          i = 0;
          strcpy(lineBuffer, "");
        }
        else
        {
          if (i < buffersize)
          {
            lineBuffer[i] = c;
            i++;
            lineBuffer[i] = '\0';
          }
          // MISSING wenn status 3 und content-length --> abbrechen.
        }
      }
      if (status == Status::BODY)      // status 3 could end without linefeed, therefore we takeover here also
      {
        strlcpy(postParameter, lineBuffer, smallbuffersize);
      }
      Serial.println();                // start new line at the end of the browser input
      Serial.print(F("postParameter=")); Serial.println(postParameter);
      // more advanced evaluation of postParameter from body
      // post data looks like pinD2=On but number could have one, two or even three digits
      if ( strncmp( postParameter, "pinD", 4) == 0 ) {       // check the first 4 characters (= length of needle)
        byte pin = atoi(postParameter + 4);                  // Convert ASCII to byte from position 4 onwards
        //Serial.print(("pin=")); Serial.println(pin);
        const char * ptr = strchr(postParameter, '=');       // get a pointer to the first occurance of '='
        if (ptr != NULL)                                     // only continue when postParameter contains '='
        {
          size_t pos = ptr - postParameter +1;               // calculate from the pointer adress to the absolute position within postParameter
          if ( strncmp( postParameter + pos, "On", 2) == 0 ) {
            digitalWrite(pin, 1);
          }
          else if ( strncmp( postParameter + pos, "Off", 3) == 0 ) {
            digitalWrite(pin, 0);
          }
        }
      }

      // send back a response

      if (!strcmp(uri, "/") || !strcmp(uri, "/index.htm") || !strcmp(uri, "/index.html")) {       // the homepage
        sendrootpage(client);
      }
      else if (!strcmp(uri, "/favicon.ico")) {    // a favicon
        send204(client);                         // if you don't have a favicon, send 204
      }
      else {                                      // if the page is unknown, HTTP response code 404
        send404(client);
      }
      delay(1);
      client.stop();
      Serial.println(F("\n[server] client disconnected"));
      Serial.print("Timestamp: ");
      Serial.println(millis());
      Serial.println("\r\nListening for connections...");
   }
  }
}
void read_sensors() {
sensorInputVoltage = analogRead(tempSensor) * adcRes;
pullupResistorVoltageDrop = supplyVoltage - sensorInputVoltage;
/* 
The ratio of the voltage drops equals the ratio of the resistances
E1/E2 = R1/R2
pullupResistorVoltageDrop / sensorInputVoltage = PullupResistor / sensorResistance

Therefore:
 */  
sensorResistance = (sensorInputVoltage / pullupResistorVoltageDrop) * pullupResistor;

// This formula provided by an Excel spreadsheet trendline of the resistance vs temperature values from the BAPI 3K thermistor sensor specification sheet:
// Formula's R^2 value (accuracy) = 0.999607337118696
// 9.626480018 degF to 128.9844759 degF
timeStamp = millis();
degF = 8.55571062860957e-23 * pow(sensorResistance,6) - 5.68981649695037e-18 * pow(sensorResistance,5) + 1.50180247230692e-13 * pow(sensorResistance,4) - 2.01541522576944e-9 * pow(sensorResistance,3) + 1.47906738776888e-5 * pow(sensorResistance,2) - 6.2591776279401e-2 * sensorResistance + 1.74508163989243e2;
//lightLevel = map(analogRead(lightSensor),0,1023,0,100);
lightLevel = analogRead(lightSensor)/10.23;
left = analogRead(leftEye)/10.23;
center = analogRead(centerEye)/10.23;
right = analogRead(rightEye)/10.23;
occ = digitalRead(pir);
//Serial.print(degF);
//Serial.println(" degF");
//Serial.print(',');
//Serial.println(lightLevel);
//Serial.println(analogRead(A1));
//delay(100);
}

/*
void htmloutput(EthernetClient &client) {
    // HTML document begins here -- in future use JSON Library?
    // Using client.print in a subroutine causes a scope error
  client.print("<!DOCTYPE HTML><html><head><title>Office Sensors</title></head><body><table border=1>");
  client.print("<tr><th>Ambient Temperature (degF)</th><th>Ambient Light Level (%)</th><th>Left Eye (%)</th><th>Center Eye (%)</th><th>Right Eye (%)</th><th>Occupied</th></tr>");
  client.print("<tr><td align='right'>");
  client.print(degF);
  client.print("</td><td align='right'>");
  client.print(lightLevel);
  client.print("</td><td align='right'>");
  client.print(left);
  client.print("</td><td align='right'>");
  client.print(center);
  client.print("</td><td align='right'>");
  client.print(right);
  client.print("</td><td align='right'>");
  client.print(occ);
  client.print("</td></tr>");
  client.println("</table></body></html>");
}
*/

void jsonoutput(EthernetClient &client) {
  // JSON output
/*
  client.print("{\"sensors\":[{\"timestamp\":");
  client.print(timeStamp);
  client.print(", \"ambient_temp\": ");
  client.print(degF);
  client.print(", \"ambient_light\": ");
  client.print(lightLevel);
  client.print(", \"left_eye\": ");
  client.print(left);
  client.print(", \"center_eye\": ");
  client.print(center);
  client.print(", \"right_eye\": ");
  client.print(right);
  client.print(", \"occupancy\": ");
  // client.print(occ);  // this is the real data from the open collector
  client.print(!occ);    // this is NOT the real data, but it matches the environment
  client.print("}]}");
*/

StaticJsonDocument<256> doc;

JsonArray sensors = doc.createNestedArray("sensors");

JsonObject sensors_0_values = sensors[0].createNestedObject("values");
sensors_0_values["timestamp"] = timeStamp;
sensors_0_values["ambient_temp"] = degF;
sensors_0_values["ambient_light"] = lightLevel;
sensors_0_values["left_eye"] = left;
sensors_0_values["center_eye"] = center;
sensors_0_values["right_eye"] = right;
sensors_0_values["occupancy"] = !occ;

JsonObject sensors_1_units = sensors[1].createNestedObject("units");
sensors_1_units["timestamp"] = "milliseconds since boot";
sensors_1_units["ambient_temp"] = "degF";
sensors_1_units["ambient_light"] = "%";
sensors_1_units["left_eye"] = "%";
sensors_1_units["center_eye"] = "%";
sensors_1_units["right_eye"] = "%";
sensors_1_units["occupancy"] = "T/F";

//serializeJson(doc, output);

serializeJsonPretty(doc, Serial); // make JSON human-readable
Serial.print("\r"); // Send carriage return to place serial terminal cursor at first column after displaying JSON
serializeJson(doc, client);       // send one long string
//serializeJson(doc, client); // make JSON human-readable (does not work with client)
client.print("\r\n"); // Send carriage return/line feed sequence to client terminal to place terminal prompt at first column after displaying JSON

}

/*
void serialoutput() {
  // Serial output:
  Serial.println("{");
  Serial.println(" 'sensors':");
  Serial.println("           [");
  Serial.println("            {");
  Serial.print("            'timestamp': ");
  Serial.print(timeStamp);
  Serial.println(",");
  Serial.print("            'ambient_temp': ");
  Serial.print(degF);
  Serial.println(",");
  Serial.print("            'ambient_light': ");
  Serial.print(lightLevel);
  Serial.println(",");
  Serial.print("            'left_eye': ");
  Serial.print(left);
  Serial.println(",");
  Serial.print("            'center_eye': ");
  Serial.print(center);
  Serial.println(",");
  Serial.print("            'right_eye': ");
  Serial.print(right);
  Serial.println(",");
  Serial.print("            'occupancy': ");
  // client.print(occ);  // this is the real data from the open collector
  Serial.println(!occ);    // this is NOT the real data, but it matches the environment
  //Serial.println(",");
  Serial.println("            }");
  Serial.println("           ]");
  Serial.println("}");
}
*/

void sendrootpage(EthernetClient &client) {
  read_sensors();
  Serial.println("HTTP/1.1 200 OK");
  Serial.println("Content-Type: text/html");
  Serial.println("Connection: close");  // the connection will be closed after completion of the response
  Serial.println("Refresh: 15");  // refresh the page automatically every 15 sec
  Serial.println();
  client.println("HTTP/1.1 200 OK");
  client.println("Content-Type: text/html");
  client.println("Connection: close");  // the connection will be closed after completion of the response
  client.println("Refresh: 15");  // refresh the page automatically every 15 sec
  client.println();
  
  //serialoutput();
  jsonoutput(client);
  //htmloutput(client);
  client.stop();
}

void send204(EthernetClient &client)
{
  Serial.println("HTTP/1.0 204 no content\r\n");
  client.println("HTTP/1.0 204 no content\r\n");
  client.stop();
}

void send404(EthernetClient &client)
{
  Serial.println("HTTP/1.0 404 Not Found\r\n"
                   "Content-Type: text/plain\r\n"
                   "\r\n"
                   "File Not Found\n");
  client.println("HTTP/1.0 404 Not Found\r\n"
                   "Content-Type: text/plain\r\n"
                   "\r\n"
                   "File Not Found\n");
  client.stop();
}
