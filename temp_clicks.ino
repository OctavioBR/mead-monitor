#include <OneWire.h>
#include <DallasTemperature.h>
#define ONE_WIRE_BUS 7
volatile int count;

// Setup a oneWire instance to communicate with any OneWire devices (not just Maxim/Dallas temperature ICs)
OneWire oneWire(ONE_WIRE_BUS);
// Pass our oneWire reference to Dallas Temperature.
DallasTemperature sensors(&oneWire);

void setup() {
  pinMode(13, OUTPUT);
  pinMode(2, INPUT);

  attachInterrupt(digitalPinToInterrupt(2), click, RISING);

  Serial.begin(9600);
  sensors.begin();
}

void loop() {
  sensors.requestTemperatures(); // Send the command to get temperatures
  Serial.print(sensors.getTempCByIndex(0));
  Serial.print(",");
  Serial.print(sensors.getTempCByIndex(1));
  Serial.print(",");
  Serial.println(count);

  count = 0;

  delay(5000);
}

void click() {
  count++;
}
