#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <WiFi.h>
#include "time.h"

#define SCREEN_WIDTH 128 // Largura do OLED
#define SCREEN_HEIGHT 64 // Altura do OLED

const char* ssid     = "AMF";
const char* password = "amf@2025";

const char* ntpServer = "pool.ntp.org";
const long  gmtOffset_sec = -10800; // Fuso horário de Brasília (-3 horas)
const int   daylightOffset_sec = 0;

// Corrigido para &Wire com W maiúsculo
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

void mostrarHoraNoOLED() {
  struct tm timeinfo;
  if(!getLocalTime(&timeinfo)){
    display.clearDisplay();
    display.setCursor(0, 10);
    display.println("Erro ao obter hora");
    display.display();
    return;
  }

  display.clearDisplay();
  display.setTextSize(2); // Texto grande para a hora
  display.setTextColor(SSD1306_WHITE);
  
  // Formata a hora para HH:MM:SS
  display.setCursor(15, 20);
  display.printf("%02d:%02d:%02d", timeinfo.tm_hour, timeinfo.tm_min, timeinfo.tm_sec);
  
  display.display();
}

void setup() {
  Serial.begin(115200);

  // Inicializa o OLED no endereço I2C padrão 0x3C
  if(!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) { 
    Serial.println(F("Falha ao iniciar o OLED"));
    for(;;);
  }
  
  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(0, 10);
  display.print("Conectando ao WiFi...");
  display.display();

  // Conecta ao Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  // Configura o relógio interno com o servidor NTP
  configTime(gmtOffset_sec, daylightOffset_sec, ntpServer);
}

void loop() {
  delay(1000);
  mostrarHoraNoOLED(); // Atualiza a tela a cada 1 segundo
}
