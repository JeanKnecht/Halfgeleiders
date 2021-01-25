int voltagePin = 6;

int resistorPin = 0;

int ledPin = 1;

int resistance = 500; //Ohm

void setup() {

Serial.begin(9600);

}

void loop() {

Serial.println("Start");

// fade in from min to max in increments of 5 points:

for (int fadeValue = 0 ; fadeValue <= 255; fadeValue += 5) {

// sets the value (range from 0 to 255):

analogWrite(voltagePin, fadeValue);

// wait for 100 or 400 milliseconds to fill capacitor

delay(40);

int resistor = analogRead(resistorPin);

int led = analogRead(ledPin);

// 5 Volt is 1023 (10 bits analog registration)

float VoltageResistor = 5.0*resistor/1024;

float VoltageLed = 5.0*(led-resistor)/1024;

double Current = 1000 * VoltageResistor / resistance ;

Serial.print("U_R: ");

Serial.print(VoltageResistor);

Serial.print(" U_led: ");

Serial.print(VoltageLed);

Serial.print(" I_led: ");

Serial.print(Current);

Serial.println(" mA");

}

}
