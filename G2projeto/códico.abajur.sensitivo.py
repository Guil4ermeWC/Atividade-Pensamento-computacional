#include <CapacitiveSensor.h>

CapacitiveSensor sensor(2, 4);

int led = 8;

bool estadoLed = false;
bool bloqueado = false;

void setup() {
  pinMode(led, OUTPUT);

  Serial.begin(9600);

  sensor.set_CS_AutocaL_Millis(0xFFFFFFFF);
}

void loop() {

  long valor = sensor.capacitiveSensor(100);

  Serial.println(valor);

  if (valor > 90 && !bloqueado) {

    estadoLed = !estadoLed;

    digitalWrite(led, estadoLed);

    bloqueado = true;
  }

  if (valor < 60) {
    bloqueado = false;
  }

  delay(20);
}
