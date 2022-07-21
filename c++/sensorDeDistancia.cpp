

#include <LiquidCrystal.h>
LiquidCrystal lcd (2, 4, 7, 8, 9, 10);

//Criei as variáveis pro sensor, pro piezo, uma pra cada led e uma pro delay.

int sensorPin = A0;
int song = 3;
int ledOne = 11;
int ledTwo = 12;
int ledThree = 13;
int emissionDelay = 25;

// Aqui no begin é a quantidade de colunas e linhas do lcd
// Clear pra limpar o lcd por completo
// setCursor é o local que escolhi que irá escrever o meu print “SENSOR DISTANC.”

void Setup()
{
	lcd.begin(16, 2);
	lcd.clear();
	lcd.print(“SENSOR DISTANC.”);
	pinMode (ledOne, OUTPUT);
	pinMode (ledTwo, OUTPUT);
	pinMode (ledThree, OUTPUT);
	pinMode (song, INPUT);
	digitalWrite(ledOne, LOW);
	digitalWrite(ledTwo, LOW);
	digitalWrite(ledThree, LOW);
}

// Criei duas variáveis, t = tempo e d = distancia
// Usei a fórmula ensinada em aula para calcular

void loop()
{
	long t;
	float d;

	pinMode (sensorPin, OUTPUT);
	digitalWrite (sensorPin, LOW);
	delayMicroseconds(10);
	digitalWrite (sensorPin, HIGH);
	delayMicroseconds (emissionDelay);
	digitalWrite (sensorPin, LOW);

	pinMode (sensorPin, INPUT);
	t = pulseIn(sensorPin, HIGH);

	d = t / 58.8;
	lcd.setCursor(2, 1);

// Aqui o primeiro IF vai fazer a primeira regra do exercício
// Caso a distancia for maior que 300cm, apresenta — no lcd
// e não emite nenhum som (coloquei 0 na função tone pra isso)

		if (d > 300)
		{
		lcd.clear();
		lcd.setCursor(0, 0);
		lcd.print(“SENSOR DISTANC.”);
		lcd.setCursor(7, 1);
		lcd.print(“—“);
		tone(song, 0, 1500);
		}

// Aqui para a segunda regra do exercício
// caso a distancia estiver entre 200 e 100, emite um som
// de 200hz por 0.5 segundos (tone) e repete a cada 1,5 segundos (delay)

		else if (d > 200)
		{
		lcd.clear();
		lcd.setCursor(0, 0);
		lcd.print(“SENSOR DISTANC.”);
		lcd.setCursor(0, 1);
		lcd.print(d);
		lcd.print(“ cm”);
		digitalWrite(ledOne, HIGH);
		delay(emissionDelay);
		digitalWrite(ledOne, LOW);
		tone(song, 200, 500);
		delay(1500);
		}

		else if (d > 100)
		{
		lcd.clear();
		lcd.setCursor(0, 0);
		lcd.print(“SENSOR DISTANC.”);
		lcd.setCursor(0, 1);
		lcd.print(d);
		lcd.print(“ cm”);
		digitalWrite(ledOne, HIGH);
		delay(emissionDelay);
		digitalWrite(ledOne, LOW);
		tone(song, 400, 500);
		delay(1000);
		}

		else if (d < 100)
		{
		lcd.clear();
		lcd.setCursor(0, 0);
		lcd.print(“SENSOR DISTANC.”);
		lcd.setCursor(0, 1);
		lcd.print(d);
		lcd.print(“ cm”);
		digitalWrite(ledOne, HIGH);
		delay(emissionDelay);
		digitalWrite(ledOne, LOW);
		digitalWrite(ledTwo, HIGH);
		delay(emissionDelay);
		digitalWrite(ledTwo, LOW);
		digitalWrite(ledThree, HIGH);
		delay(emissionDelay);
		digitalWrite(ledThree, LOW);
		tone(song, 600, 250);
		delay(500);
		}
