// C++ code
//
int vermelho = 0;

int azul = 0;

int verde = 0;

int botao1 = 0;

int botao2 = 0;

int botao3 = 0;

int potenciometro = 0;

int estado = 0;

void setup()
{
  Serial.begin(9600);
  pinMode(2, INPUT);
  pinMode(3, INPUT);
  pinMode(4, INPUT);
  pinMode(8, INPUT);
  pinMode(9, INPUT);
  pinMode(7, INPUT);
  pinMode(A1, INPUT);
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
}

void loop()
{
  Serial.println(botao1);
  Serial.println(botao2);
  Serial.println(botao3);
  vermelho = digitalRead(2);
  azul = digitalRead(3);
  verde = digitalRead(4);
  botao1 = digitalRead(8);
  botao2 = digitalRead(9);
  botao3 = digitalRead(7);
  potenciometro = analogRead(A1);
  Serial.println(botao1);
  if (botao1 == HIGH) {
    estado = 1;
  }
  if (botao2 == HIGH) {
    estado = 2;
  }
  if (botao3 == HIGH) {
    estado = 3;
  }
  if (estado == 1) {
    if (potenciometro > 5 && potenciometro < 207) {
      digitalWrite(2, HIGH);
      digitalWrite(3, LOW);
      digitalWrite(4, LOW);
    } else {
    }
    if (potenciometro > 250 && potenciometro < 500) {
      digitalWrite(2, HIGH);
      digitalWrite(4, HIGH);
      digitalWrite(3, LOW);
    } else {
    }
    if (potenciometro > 500) {
      digitalWrite(4, HIGH);
      digitalWrite(3, LOW);
      digitalWrite(2, LOW);
    }
  }
  if (estado == 2) {
    digitalWrite(2, HIGH);
    digitalWrite(3, LOW);
    digitalWrite(4, LOW);
  }
  if (estado == 3) {
    digitalWrite(3, LOW);
    digitalWrite(2, LOW);
    digitalWrite(4, LOW);
  }
  delay(10); // Delay a little bit to improve simulation performance
}
